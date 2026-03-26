import json
import os

def merge_batches():
    master_file = 'l4_master.json'
    if os.path.exists(master_file):
        with open(master_file, 'r', encoding='utf-8') as f:
            master_data = json.load(f)
    else:
        master_data = {}

    # Merge newly created batches (p6 to p10)
    for i in range(6, 11):
        batch_file = f'batch_l4_p{i}.json'
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
                master_data.update(batch_data)
                print(f"Merged {batch_file} ({len(batch_data)} words)")

    with open(master_file, 'w', encoding='utf-8') as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    
    print(f"Master L4 JSON updated. Total words: {len(master_data)}")

if __name__ == "__main__":
    merge_batches()
