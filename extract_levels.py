import pdfplumber
import re
import pandas as pd
import json

def extract_by_level(pdf_path, levels):
    level_data = {l: [] for l in levels}
    sorted_levels = sorted(levels.items(), key=lambda x: x[1])
    
    # 建立頁碼範圍
    page_ranges = []
    for i in range(len(sorted_levels)):
        start = sorted_levels[i][1]
        end = sorted_levels[i+1][1] if i+1 < len(sorted_levels) else 116 # 假設總頁數 116
        page_ranges.append((sorted_levels[i][0], start, end))
    
    pattern = re.compile(r'([A-Za-z\-\(\)/]+)\s+([a-z\.\/\(\)]+)')
    
    with pdfplumber.open(pdf_path) as pdf:
        for lvl_name, start, end in page_ranges:
            print(f"Processing {lvl_name} (Pages {start}-{end-1})...")
            for p_idx in range(start-1, end-1):
                page = pdf.pages[p_idx]
                text = page.extract_text()
                if text:
                    for line in text.split('\n'):
                        matches = pattern.findall(line)
                        for word, pos in matches:
                            if len(word) > 1 and ('.' in pos or '/' in pos):
                                level_data[lvl_name].append({'單字': word, '詞類': pos})
    
    return level_data

if __name__ == "__main__":
    pdf_path = r"C:\Users\TK_Tsai\Downloads\高中英文參考詞彙表(111學年度起適用).pdf"
    levels = {
        '第一級': 7, '第二級': 21, '第三級': 29, 
        '第四級': 38, '第五級': 46, '第六級': 55
    }
    data = extract_by_level(pdf_path, levels)
    # 存成 JSON 以供後續分批補全
    with open("raw_levels.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Saved extraction results to raw_levels.json")
