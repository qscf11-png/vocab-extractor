import json
import os

def merge_l2_batches():
    all_l2_data = {}
    base_path = "C:/Users/TK_Tsai/.gemini/antigravity/scratch/vocab_extractor"
    
    # Merge all 13 batches
    for i in range(1, 14):
        filename = f"batch_l2_p{i}.json"
        full_path = os.path.join(base_path, filename)
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                batch_data = json.load(f)
                all_l2_data.update(batch_data)
                print(f"Merged {filename}: {len(batch_data)} words")
        else:
            print(f"Warning: {filename} not found.")

    output_file = os.path.join(base_path, "Level_2_Enriched_Master.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_l2_data, f, ensure_ascii=False, indent=2)
    
    print("-" * 30)
    print(f"Total Level 2 unique words merged: {len(all_l2_data)}")
    print(f"Master file saved to: {output_file}")

if __name__ == "__main__":
    merge_l2_batches()
