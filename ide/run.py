import subprocess
import os

def _get_params(lang, filename):
    return {
        'py': ["python3.8", filename],
        'c': [["gcc", filename, "-o", "output/a.out"], ["./output/a.out"]]
    }.get(lang)


def run(code, lang):
    filename = f"output/editor_code.{lang}"
    f = open(filename, "w").write(code)
    comps = []
    for param in _get_params(lang, filename):
        comps.append(subprocess.run(param, stdout=subprocess.PIPE, encoding="UTF-8"))
    output = comps[-1].stdout
    os.remove("output/a.out")
    os.remove(filename)
    return output
