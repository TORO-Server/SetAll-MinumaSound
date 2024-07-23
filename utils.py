import json


# 読み込み
def read(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


# 書き込み
def save(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
