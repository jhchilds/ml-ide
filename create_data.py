import os
import json


REPOS_DIR = "repos-cloned"

data = []
file_types = ["py", "java"]

MAX_SAMPLES = 100000
counts = {}
index = 0

for root, dirs, files in os.walk(REPOS_DIR):
    for name in files:
        file_path = os.path.join(root, name)
        for file_type in file_types:
            if file_path.endswith("." + file_type):
                if file_type in counts:
                    counts[file_type] += 1
                else:
                    counts[file_type] = 1
                if counts[file_type] > MAX_SAMPLES:
                    continue

                try:
                    print(file_path)
                    with open(file_path) as source_file:
                        data.append({
                            "data": source_file.read(),
                            "source": file_path,
                            "target": file_type
                        })
                except Exception:
                    pass

with open("data.json", "w") as json_file:
    json.dump(data, json_file)
