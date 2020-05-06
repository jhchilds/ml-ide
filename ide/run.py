import subprocess


def _get_params(lang, filename):
    return {
        'py': ["python3.8", filename],
    }.get(lang)


def run(code, lang):
    filename = f"editor_code.{lang}"
    f = open(filename, "w").write(code)
    comp = subprocess.run(_get_params(lang, filename),
                          stdout=subprocess.PIPE, encoding="UTF-8")
    output = comp.stdout
    return output

# python, haskell, java, javascript, c, swift
