"""Exporta sesiones de Claude Code y GitHub Copilot a Markdown legible y sanitizado.

Uso: python3 -I scripts/exportar_evidencias_ia.py <destino_repo>/evidencias_ia
"""
import json, re, sys, os
from datetime import datetime, timezone, timedelta

P = os.path.expanduser('~/.claude/projects/')
LIMA = timezone(timedelta(hours=-5))
MAX_OUT = 4000  # caracteres máximos por resultado de herramienta

# (carpeta destino, archivo de salida, proyecto, prefijo de sesión, título)
SESIONES = [
    ('mcp', '01_2026-10-28_prueba-mcp-bcrp-ipc.md', '-Users-susanmontalvo-Documents-GitHub-Diplomado-Su-2026-mcp-bcrp', '2f87fe35', 'Antecedente: consultas de prueba al MCP bcrp (Sesión 04)'),
    ('mcp', '02_2026-10-28_prueba-mcp-bcrp-recurso.md', '-Users-susanmontalvo-Documents-GitHub-Diplomado-Su-2026-mcp-bcrp', '3301fed6', 'Antecedente: lectura del recurso bcrp://serie del MCP'),
    ('skills', '01_2026-10-31_entorno-skills.md', '-Users-susanmontalvo-Documents-GitHub-skills-enaho', '4c192642', 'Preparación del entorno para las Skills ENAHO'),
    ('skills', '02_2026-10-31_desarrollo-skills.md', '-Users-susanmontalvo-Documents-GitHub-skills-enaho', 'c402dba6', 'Desarrollo de las Skills ENAHO'),
]
PRUEBAS_OCT31 = ['bb5ba63a', '2f2c4e6c', 'd0eee21d', '94da203a', '595f7549', 'b118fb4e', '1b429e59', '861f2591', '14feef4f',
                 'a947b0a5', '9dcfccef', 'd3122a25', 'ca2a9033', '542f7e5c', '43b9153f']
PRUEBAS_NOV05 = ['a07b8bf4', 'de8ca0aa', 'e55b28ea', '8aafaaa6', '979e26eb', 'c4f30267', '9c519b02']
EVAL = [
    ('evaluacion', '01_2026-11-04_traslado-preguntas.md', '-Users-susanmontalvo-Documents-GitHub-agente-datos-oficiales-Peru', '53a0d2bb', 'Traslado de preguntas.csv a una carpeta temporal'),
    ('evaluacion', '03_2026-11-05_diseno-preguntas-y-respuestas-esperadas.md', '-Users-susanmontalvo-Documents-GitHub-prueba-temporal-de-skills', '9babceaf', 'Diseño de las 10 preguntas y de las respuestas esperadas'),
    ('evaluacion', '04_2026-11-05_resultados-y-comparacion.md', '-Users-susanmontalvo-Documents-GitHub-agente-datos-oficiales-Peru', '5881871a', 'Registro de resultados, comparación y documentación de la Parte 4'),
    ('evaluacion', '05_2026-11-06_modo-a-sin-mcp-ni-skills.md', '-Users-susanmontalvo-Documents-GitHub-Modo-A', 'f1d37f5c', 'Ejecución Modo A (sin MCP ni Skills)'),
    ('evaluacion', '07_2026-11-06_modo-b-con-mcp-y-skills.md', '-Users-susanmontalvo-Documents-GitHub-Modo-B-firme', 'f11cbbaa', 'Ejecución Modo B (con MCP y Skills)'),
]

# Sesiones de GitHub Copilot (~/.copilot/session-state/<id>/events.jsonl).
# (carpeta, archivo, sesión, primer mensaje, último mensaje, título); los mensajes se cuentan desde 1.
C = os.path.expanduser('~/.copilot/session-state/')
COPILOT = [
    ('mcp', '03_2026-11-04_entorno-y-parte-1-servidor-mcp.md', '43cf96d4-bfbc-4438-8957-f418eee6bc7c', 1, 68, 'Preparación del entorno y Parte 1: servidor MCP del BCRP y pruebas'),
    ('skills', '04_2026-11-04_parte-2-adaptacion-e-integracion-skills.md', '43cf96d4-bfbc-4438-8957-f418eee6bc7c', 69, 116, 'Parte 2: adaptación, integración, activación y coordinación de las Skills'),
    ('integracion', '01_2026-11-05_parte-3-agente-e-informe.md', '43cf96d4-bfbc-4438-8957-f418eee6bc7c', 117, 188, 'Parte 3: pregunta de investigación, plan de análisis, ejecución, informe y verificación'),
    ('evaluacion', '02_2026-11-05_parte-4-planificacion.md', '43cf96d4-bfbc-4438-8957-f418eee6bc7c', 189, 10**6, 'Parte 4: planificación de la evaluación y de las sesiones independientes'),
    ('evaluacion', '06_2026-11-06_modo-b-primer-intento-copilot.md', '1de4297b-b913-490f-9a10-2b7522ecdc90', 1, 10**6, 'Modo B: primer intento con GitHub Copilot (descartado)'),
]


def exportar_copilot(sesion, desde, hasta, titulo):
    L = [json.loads(l) for l in open(C + sesion + '/events.jsonl', encoding='utf-8') if l.strip()]
    llamadas, out, n, dentro, ts, modelos, cwd = {}, [], 0, False, [], set(), ''
    for x in L:
        t, d = x.get('type'), x.get('data', {})
        if t == 'session.start':
            cwd = d.get('context', {}).get('cwd', '')
        if t == 'user.message':
            n += 1
            dentro = desde <= n <= hasta
        if not dentro:
            continue
        if x.get('timestamp'):
            ts.append(x['timestamp'])
        if t == 'user.message':
            txt = re.sub(r'<reminder>.*?</reminder>', '', d.get('content', ''), flags=re.S).strip()
            out += [f'## 🧑 Usuaria · {hora(x["timestamp"])}', '', txt or '_(mensaje vacío o solo con adjunto)_', '']
        elif t == 'assistant.message':
            if d.get('model'):
                modelos.add(d['model'])
            if (d.get('content') or '').strip():
                out += [f'## 🤖 Copilot · {hora(x["timestamp"])}', '', d['content'].strip(), '']
            for r in d.get('toolRequests') or []:
                a = r.get('arguments', {})
                cuerpo = a.get('command') if isinstance(a, dict) and 'command' in a else json.dumps(a, ensure_ascii=False, indent=1)
                desc = r.get('intentionSummary') or (a.get('description') if isinstance(a, dict) else '') or ''
                out += [f'**Herramienta `{r.get("name")}`**{" — " + desc if desc else ""}', '',
                        bloque(recortar(str(cuerpo or '')), 'bash' if r.get('name') == 'bash' else 'json'), '']
        elif t == 'tool.execution_complete':
            res = d.get('result') or {}
            r = res.get('content') if isinstance(res, dict) else res
            if not d.get('success', True):
                r = f'[error] {d.get("error") or r}'
            out += ['<details><summary>Resultado</summary>', '', bloque(recortar(str(r or ''))), '', '</details>', '']
    cab = [f'# {titulo}', '',
           f'- **Sesión:** `{sesion[:8]}` · GitHub Copilot (agente de VS Code)',
           f'- **Carpeta de trabajo inicial:** `{cwd}`',
           f'- **Modelo:** {", ".join(sorted(modelos))}',
           f'- **Mensajes de la usuaria:** {desde} a {min(hasta, n)} de {n} de la sesión',
           f'- **Inicio:** {hora(min(ts))} · **Fin:** {hora(max(ts))} (hora de Lima)', '',
           '> Exportación del registro local de GitHub Copilot. Se omiten las instrucciones de sistema, los hooks y los permisos; '
           f'las salidas de herramientas de más de {MAX_OUT:,} caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.', '']
    return sanitizar('\n'.join(cab + out)), hora(min(ts))


def sanitizar(s):
    s = re.sub(r'[\w.+-]+@(gmail\.com|pucp\.edu\.pe|hotmail\.com|outlook\.com|yahoo\.com)', '[correo oculto]', s)
    s = s.replace('/Users/susanmontalvo', '~')
    s = s.replace('susanmontalvo@', 'usuario@')
    s = re.sub(r'/private/tmp/claude-501/[^\s"\'`)]*', '[carpeta temporal]', s)
    s = re.sub(r'https://claude\.ai/artifact/[A-Za-z0-9_-]+', '[enlace privado de claude.ai]', s)
    s = re.sub(r'(ghp_|github_pat_|sk-)[A-Za-z0-9_-]{16,}', '[credencial oculta]', s)
    return s


def limpiar_usuario(t):
    t = re.sub(r'<system-reminder>.*?</system-reminder>', '', t, flags=re.S)
    t = re.sub(r'<ide_opened_file>The user opened the file (.*?) in the IDE.*?</ide_opened_file>', r'_(Archivo abierto en el editor: \1)_\n', t, flags=re.S)
    t = re.sub(r'<ide_selection>.*?</ide_selection>', '_(Selección en el editor)_\n', t, flags=re.S)
    t = re.sub(r'<command-name>(.*?)</command-name>', r'`\1`', t, flags=re.S)
    t = re.sub(r'<(command-message|command-args|local-command-stdout|local-command-caveat)>.*?</\1>', '', t, flags=re.S)
    return t.strip()


def bloque(texto, lang=''):
    texto = texto.replace('```', "'''")
    return f'```{lang}\n{texto}\n```'


def recortar(s):
    if len(s) > MAX_OUT:
        return s[:MAX_OUT] + f'\n… [salida recortada: {len(s) - MAX_OUT:,} caracteres más]'
    return s


def hora(ts):
    return datetime.fromisoformat(ts.replace('Z', '+00:00')).astimezone(LIMA).strftime('%Y-%m-%d %H:%M:%S')


def exportar(proyecto, prefijo, titulo):
    import glob
    f = glob.glob(P + proyecto + f'/{prefijo}*.jsonl')[0]
    L = []
    for l in open(f, encoding='utf-8'):
        try:
            L.append(json.loads(l))
        except Exception:
            pass
    ts = [x['timestamp'] for x in L if 'timestamp' in x]
    modelos = sorted({x['message'].get('model') for x in L if x.get('type') == 'assistant' and x['message'].get('model')} - {'<synthetic>'})
    cwd = next((x['cwd'] for x in L if x.get('cwd')), '')
    out = [f'# {titulo}', '',
           f'- **Sesión:** `{os.path.basename(f)[:8]}` · Claude Code',
           f'- **Carpeta de trabajo:** `{cwd}`',
           f'- **Modelo:** {", ".join(modelos)}',
           f'- **Inicio:** {hora(min(ts))} · **Fin:** {hora(max(ts))} (hora de Lima)', '',
           '> Exportación del registro local de la sesión. Se omiten el contexto de sistema y el razonamiento interno; '
           f'las salidas de herramientas de más de {MAX_OUT:,} caracteres se recortan. Correos, rutas personales y enlaces privados se ocultaron.', '']
    for x in L:
        t = x.get('type')
        if t == 'user' and not x.get('isMeta'):
            c = x['message'].get('content')
            if isinstance(c, str):
                txt = limpiar_usuario(c)
                if txt:
                    out += [f'## 🧑 Usuaria · {hora(x["timestamp"])}', '', txt, '']
            elif isinstance(c, list):
                for b in c:
                    if not isinstance(b, dict):
                        continue
                    if b.get('type') == 'text':
                        txt = limpiar_usuario(b['text'])
                        if txt:
                            out += [f'## 🧑 Usuaria · {hora(x["timestamp"])}', '', txt, '']
                    elif b.get('type') == 'image':
                        out += ['_(Imagen adjunta por la usuaria)_', '']
                    elif b.get('type') == 'tool_result':
                        r = b.get('content')
                        if isinstance(r, list):
                            r = '\n'.join(i.get('text', '[imagen]') if isinstance(i, dict) else str(i) for i in r)
                        out += ['<details><summary>Resultado</summary>', '', bloque(recortar(str(r or ''))), '', '</details>', '']
        elif t == 'assistant':
            for b in x['message'].get('content', []):
                if not isinstance(b, dict):
                    continue
                if b.get('type') == 'text' and b['text'].strip():
                    out += [f'## 🤖 Claude · {hora(x["timestamp"])}', '', b['text'].strip(), '']
                elif b.get('type') == 'tool_use':
                    i = b.get('input', {})
                    desc = i.get('description', '') if isinstance(i, dict) else ''
                    cuerpo = i.get('command') if b['name'] == 'Bash' and isinstance(i, dict) else json.dumps(i, ensure_ascii=False, indent=1)
                    out += [f'**Herramienta `{b["name"]}`**{" — " + desc if desc else ""}', '',
                            bloque(recortar(cuerpo or ''), 'bash' if b['name'] == 'Bash' else 'json'), '']
    return sanitizar('\n'.join(out)), hora(min(ts))


def main(dest):
    indice = []
    for carpeta, nombre, proy, pref, tit in SESIONES + EVAL:
        md, ini = exportar(proy, pref, tit)
        os.makedirs(os.path.join(dest, carpeta), exist_ok=True)
        open(os.path.join(dest, carpeta, nombre), 'w', encoding='utf-8').write(md)
        indice.append((carpeta, nombre, tit, ini))
    for carpeta, nombre, ses, a, b, tit in COPILOT:
        md, ini = exportar_copilot(ses, a, b, tit)
        os.makedirs(os.path.join(dest, carpeta), exist_ok=True)
        open(os.path.join(dest, carpeta, nombre), 'w', encoding='utf-8').write(md)
        indice.append((carpeta, nombre, tit, ini))
    for carpeta, nombre, proy, lista, tit in [
        ('skills', '03_2026-10-31_pruebas-activacion-skills.md', '-Users-susanmontalvo-Documents-GitHub-skills-enaho', PRUEBAS_OCT31, 'Pruebas de activación de las Skills en lenguaje natural'),
        ('skills', '05_2026-11-05_pruebas-coordinacion-skills.md', '-Users-susanmontalvo-Documents-GitHub-agente-datos-oficiales-Peru', PRUEBAS_NOV05, 'Pruebas de invocación individual y coordinación de las Skills')]:
        partes = [f'# {tit}', '', f'Reúne {len(lista)} sesiones cortas e independientes, en orden cronológico.', '']
        inis = []
        for pref in lista:
            md, ini = exportar(proy, pref, f'Sesión {pref}')
            inis.append(ini)
            partes += ['---', '', md.replace('\n# ', '\n## ', 1).replace('# Sesión', '## Sesión', 1), '']
        os.makedirs(os.path.join(dest, carpeta), exist_ok=True)
        open(os.path.join(dest, carpeta, nombre), 'w', encoding='utf-8').write('\n'.join(partes))
        indice.append((carpeta, nombre, tit, min(inis)))
    for c, n, t, i in sorted(indice, key=lambda r: (r[0], r[1])):
        print(f'{c}/{n}\t{i}\t{os.path.getsize(os.path.join(dest, c, n)) // 1024} KB\t{t}')


if __name__ == '__main__':
    main(sys.argv[1])
