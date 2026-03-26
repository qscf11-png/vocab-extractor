import json
import os
import glob

def merge_batches():
    merged_data = {}
    batch_files = glob.glob("batch_l1_p*.json")
    
    # Sort by part number for order consistency
    batch_files.sort(key=lambda x: int(x.split('_p')[1].split('.json')[0]))
    
    print(f"找到 {len(batch_files)} 個批次檔案。")
    
    for file_path in batch_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                merged_data.update(data)
                print(f"已合併: {file_path} ({len(data)} 詞)")
        except Exception as e:
            print(f"處理 {file_path} 時出錯: {e}")
            
    output_path = "merged_l1_data.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n合併完成！總計 {len(merged_data)} 個單字。")
    print(f"結果已儲存至: {output_path}")

if __name__ == "__main__":
    merge_batches()
