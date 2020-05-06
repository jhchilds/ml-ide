import subprocess
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def _get_params(lang, filename):
    return {
        'py': [["python3.8", filename]],
        'c': [["gcc", filename, "-o", f"{dir_path}/output/a.out"], [f"{dir_path}/output/a.out"]]
    }.get(lang)


def run(code, lang):
    filename = f"{dir_path}/output/editor_code.{lang}"
    f = open(filename, "w").write(code)
    comps = []
    for param in _get_params(lang, filename):
        comps.append(subprocess.run(param, stdout=subprocess.PIPE, encoding="UTF-8"))
    output = comps[-1].stdout
    aoutpath = f"{dir_path}/output/a.out"
    if os.path.exists(aoutpath):
        os.remove(aoutpath)
    if os.path.exists(filename):
        os.remove(filename)
    return output
