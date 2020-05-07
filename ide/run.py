import subprocess
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def _get_params(lang, filename):
    return {
        'py': [["python3.8", filename]],
        'c': [["gcc", filename, "-o", f"{dir_path}/output/a.out"], [f"{dir_path}/output/a.out"]],
        'swift': [["swiftc", filename, "-o", f"{dir_path}/output/a.out"], [f"{dir_path}/output/a.out"]],
        'hs': [["stack", "runghc", filename]],
        'js': [["node", filename]],
        'java': [["javac", filename], ["java", "-cp", f"{dir_path}/output", "Main"]]
    }.get(lang) 


def run(code, lang):
    if lang == 'java':
        filename = _get_java_template(code)
    else:
        filename = f"{dir_path}/output/editor_code.{lang}"
        f = open(filename, "w").write(code)
    comps = []
    for param in _get_params(lang, filename):
        comps.append(subprocess.run(param, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="UTF-8"))
    response = {
        "output": comps[-1].stdout,
        "errors": comps[-1].stderr
    }
    aoutpath = f"{dir_path}/output/a.out"
    if os.path.exists(aoutpath):
        os.remove(aoutpath)
    # if os.path.exists(filename):
        # os.remove(filename)
    return response

def _get_java_template(code):
    filename = f"{dir_path}/output/Main.java"
    f = open(filename, "w")
    f.write("public class Main {" + code + "}")
    return filename