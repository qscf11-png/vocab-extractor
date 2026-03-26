import json

def check_count():
    with open("raw_levels.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for k, v in data.items():
            print(f"{k}: {len(v)} words")
        # 顯示 Level 1 的前 5 筆看資料結構
        print("Level 1 Sample:", data['第一級'][:5])

if __name__ == "__main__":
    check_count()
