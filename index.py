from utils import read, save


# ----- setting ----- start

# sounds.json ファイルのパス
TARGET_PATH = "./sounds.json"
# 変換された sounds.json ファイルが生成されるパス
RESULT_PATH = "./result.json"

# 書き込まれるサウンド名
AFTER_SOUND_NAME = "minuma/iku001"

# ----- setting ----- end


sounds = read(TARGET_PATH)

for i in sounds:
    for j in range(len(sounds[i]["sounds"])):
        # "replace": true を追加
        sounds[i]["replace"] = True
        if type(sounds[i]["sounds"][j]) is str:
            print(f'{sounds[i]["sounds"][j]} -> {AFTER_SOUND_NAME}\n')
            sounds[i]["sounds"][j] = AFTER_SOUND_NAME
        else:
            print(f'{sounds[i]["sounds"][j]["name"]} -> {AFTER_SOUND_NAME}\n')
            sounds[i]["sounds"][j]["name"] = AFTER_SOUND_NAME


# 編集後の sounds.json ファイルを保存する
save(RESULT_PATH, sounds)
