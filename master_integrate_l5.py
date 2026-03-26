import json
import os

def integrate_level(level_name, part_count, prefix="batch_l5_p"):
    master_path = "master_vocab.json"
    
    # Load Master JSON
    if os.path.exists(master_path):
        with open(master_path, "r", encoding="utf-8") as f:
            master_data = json.load(f)
    else:
        master_data = {}
    
    if level_name not in master_data:
        master_data[level_name] = {}
        
    # Integrate all parts
    for i in range(1, part_count + 1):
        batch_path = f"{prefix}{i}.json"
        if os.path.exists(batch_path):
            print(f"Integrating {batch_path}...")
            with open(batch_path, "r", encoding="utf-8") as f:
                batch_data = json.load(f)
                master_data[level_name].update(batch_data)
        else:
            print(f"Warning: {batch_path} not found.")
            
    # Save Master JSON
    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully integrated {len(master_data[level_name])} words into {level_name}.")

if __name__ == "__main__":
    integrate_level("L5", 11)
