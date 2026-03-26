import json
import os
import glob
import pandas as pd

def integrate_l6():
    working_dir = r"C:\Users\TK_Tsai\.gemini\antigravity\scratch\vocab_extractor"
    master_file = os.path.join(working_dir, "master_vocab.json")
    
    # 讀取現有數據，保留分層結構 (L1-L5)
    if os.path.exists(master_file):
        try:
            with open(master_file, "r", encoding="utf-8") as f:
                master_data = json.load(f)
        except Exception as e:
            print(f"Error reading master file, starting fresh: {e}")
            master_data = {}
    else:
        master_data = {}

    # 確保 L6 鍵值存在
    if "L6" not in master_data:
        master_data["L6"] = {}
    
    # 讀取所有 L6 batch 文件
    batch_files = glob.glob(os.path.join(working_dir, "batch_l6_p*.json"))
    print(f"Found {len(batch_files)} batch files for Level 6.")
    
    integrated_count = 0
    for bf in batch_files:
        try:
            with open(bf, "r", encoding="utf-8") as f:
                batch_data = json.load(f)
                # 只有當 batch_data 是 dict 時才更新
                if isinstance(batch_data, dict):
                    master_data["L6"].update(batch_data)
                    integrated_count += len(batch_data)
                else:
                    print(f"Skipping {bf}: Not a dictionary.")
        except Exception as e:
            print(f"Error reading {bf}: {e}")

    # 清理掉可能在先前錯誤整合中寫入根層級的 L6 單字 (如果它們不是 L1-L5 分類)
    # 我們假設 master_vocab 的合法根鍵只有 L1, L2, L3, L4, L5, L6
    valid_keys = {"L1", "L2", "L3", "L4", "L5", "L6", "第一級", "第二級", "第三級", "第四級", "第五級", "第六級"}
    keys_to_remove = [k for k in master_data.keys() if k not in valid_keys]
    for k in keys_to_remove:
        del master_data[k]

    # 寫回 JSON
    with open(master_file, "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    
    print(f"Level 6 count in master: {len(master_data.get('L6', {}))}")
    print(f"Total levels in master: {list(master_data.keys())}")
    return master_data

def export_to_excel(data):
    rows = []
    # 遍歷所有層級 (L1, L2, L3, L4, L5, L6)
    for level, words_dict in data.items():
        if isinstance(words_dict, dict):
            for word, details in words_dict.items():
                rows.append({
                    "Level": level,
                    "Word": word,
                    "IPA": details.get("ipa", ""),
                    "POS": details.get("pos", ""),
                    "Definition": details.get("def", ""),
                    "Translation": details.get("trans", ""),
                    "Collocation": details.get("col", ""),
                    "Example": details.get("ex", "")
                })
        else:
            print(f"Skipping level {level}: Data type is {type(words_dict)}")
    
    df = pd.DataFrame(rows)
    output_path = r"C:\Users\TK_Tsai\.gemini\antigravity\scratch\vocab_extractor\111學年度高中參考詞彙_全量補全版_Lv1-6.xlsx"
    df.to_excel(output_path, index=False)
    print(f"Exported {len(rows)} entries to {output_path}")

if __name__ == "__main__":
    data = integrate_l6()
    export_to_excel(data)
