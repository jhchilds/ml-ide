import subprocess

def run(code, lang):
    filename =  f"editor_code.{lang}"
    f = open(filename, "w").write(code)

    comp = subprocess.run(["python3.8", filename],
                          stdout=subprocess.PIPE, encoding="UTF-8")
    output = comp.stdout
    return output

print(run("print('hello')", 'py'))