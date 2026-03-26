import pdfplumber
import re

def detect_levels(pdf_path):
    levels = {}
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                # 尋找 "第一級", "第二級" 等字樣
                match = re.search(r'(第[一二三四五六]級)', text)
                if match:
                    level_name = match.group(1)
                    if level_name not in levels:
                        levels[level_name] = i + 1
    return levels

if __name__ == "__main__":
    pdf_path = r"C:\Users\TK_Tsai\Downloads\高中英文參考詞彙表(111學年度起適用).pdf"
    levels = detect_levels(pdf_path)
    print("Detected Levels and starting pages:")
    for l, p in levels.items():
        print(f"{l}: Page {p}")
