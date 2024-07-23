from utils import read, save

# sounds.json ファイルのパス
TARGET_PATH = "./sounds.json"

RESULT_PATH = "./result.json"

sounds = read(TARGET_PATH)

for i in sounds:
    for j in sounds[i]:
        print(i)
        print(j)
        print(sounds[i][j])
        print("\n")

# 編集後の sounds.json ファイルを保存する
save(RESULT_PATH, sounds)