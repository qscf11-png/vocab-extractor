import json

# Level 5 Part 7: (Mandate - Mortgage)
L5_PART7 = {
    "mandate": {"def": "授權、委託、指令、在外部、委任管理、強制執行、指令於、委託", "ipa": "/ˈmændeɪt/", "trans": "mandatory", "col": "popular mandate, mandatory requirement", "ex": "The government has a popular mandate for its reform program.", "pos": "n./v."},
    "myth": {"def": "神話、虛構的故事、迷信", "ipa": "/mɪθ/", "trans": "mythology, mythical", "col": "Greek myth, urban myth", "ex": "The Greek myths are full of gods and heroes.", "pos": "n."},
    "overturn": {"def": "翻轉、傾覆、推翻、瓦解、傾覆、瓦解、翻轉", "ipa": "/ˌəʊvəˈtɜːn/", "trans": "overturned", "col": "overturn a decision, overturn a boat", "ex": "The court overturned the original decision.", "pos": "v./n."},
    "manifest": {"def": "顯然的、明白的、清單、載貨清單、表明、顯示、證明、出現", "ipa": "/ˈmænɪfest/", "trans": "manifestation, manifesto", "col": "manifest truth, passenger manifest", "ex": "His anger was manifest to everyone.", "pos": "adj./n./v."},
    "naive": {"def": "天真的、嫩的、疏忽的、幼稚的", "ipa": "/naɪˈiːv/", "trans": "naivety", "col": "naive belief", "ex": "It's naive to think that there is no danger.", "pos": "adj."},
    "overwhelm": {"def": "壓倒、擊敗、使受不了、使陷入", "ipa": "/ˌəʊvəˈwelm/", "trans": "overwhelming", "col": "overwhelmed with work, overwhelmed with joy", "ex": "She was overwhelmed with joy when she heard the news.", "pos": "v."},
    "mortality": {"def": "死亡率、必死性、人類", "ipa": "/mɔːˈtæləti/", "trans": "mortal", "col": "infant mortality, mortality rate", "ex": "The infant mortality rate has decreased dramatically.", "pos": "n."},
    "outfit": {"def": "全套裝備、結構、機構、配備、供給、裝配", "ipa": "/ˈaʊtfɪt/", "trans": "outfitted", "col": "complete outfit", "ex": "She was wearing a very expensive outfit.", "pos": "n./v."},
    "pipeline": {"def": "管道、輸送管、在中、研發中", "ipa": "/ˈpaɪplaɪn/", "trans": "pipelines", "col": "oil pipeline, in the pipeline", "ex": "The oil is transported through an underground pipeline.", "pos": "n."},
    "mortgage": {"def": "抵押、抵押借款、抵押借款之權利、抵押、以...作擔保", "ipa": "/ˈmɔːɡɪdʒ/", "trans": "mortgaged", "col": "take out a mortgage, mortgage interest", "ex": "They took out a mortgage to buy the house.", "pos": "n./v."},
    "brilliant": {"def": "燦爛的、卓越的、聰明的、寶石、亮點、極好地、出色地", "ipa": "/ˈbrɪliənt/", "trans": "brilliance, brilliantly", "col": "brilliant idea, brilliant career", "ex": "She is a brilliant student.", "pos": "adj./n./adv."},
    "brim": {"def": "邊、緣、帽簷、滿溢、充盈、使滿溢", "ipa": "/brɪm/", "trans": "brimming", "col": "brim with confidence, brim of a hat", "ex": "The cup was filled to the brim.", "pos": "n./v."},
    "brine": {"def": "鹽水、海水、用鹽水醃、浸入鹽水中", "ipa": "/braɪn/", "trans": "briny", "col": "brine solution", "ex": "Olives are stored in brine.", "pos": "n./v."},
    "bring": {"def": "帶來、產生、促使、提起(訴訟)", "ipa": "/brɪŋ/", "trans": "brought", "col": "bring about, bring up, bring along", "ex": "Can you bring me a glass of water?", "pos": "v."},
    "brink": {"def": "邊、邊緣、始發點", "ipa": "/brɪŋk/", "trans": "brinks", "col": "on the brink of", "ex": "The country is on the brink of civil war.", "pos": "n."},
    "brisk": {"def": "活潑的、輕快的、涼爽的、使活潑、變得快、活潑地、輕快地", "ipa": "/brɪsk/", "trans": "briskly, briskness", "col": "brisk walk, brisk pace", "ex": "She set off at a brisk pace.", "pos": "adj./v./adv."},
    "bristle": {"def": "短而硬的毛、剛毛、發怒、(手等)豎起、充滿、生氣 (剛毛)", "ipa": "/ˈbrɪsl/", "trans": "bristly", "col": "hog bristle, bristle with anger", "ex": "The cat's fur bristled when it saw the dog.", "pos": "n./v."},
    "broad": {"def": "寬的、廣泛的、明顯的、概括的、寬闊地、明亮地、寬闊處、主要部分", "ipa": "/brɔːd/", "trans": "breadth, broaden", "col": "broad daylight, broad hint, broad-minded", "ex": "He has broad shoulders.", "pos": "adj./adv./n."},
    "broadcast": {"def": "廣播、散布、播送、廣播的、散布的、在廣播中、廣播、傳播", "ipa": "/ˈbɔːdkɑːst/", "trans": "broadcaster, broadcasting", "col": "radio broadcast, live broadcast", "ex": "The news is broadcast every hour.", "pos": "n./adj./adv./v."},
    "broaden": {"def": "變寬、擴大、使變寬、擴展", "ipa": "/ˈbrɔːdn/", "trans": "broad (形容詞/副詞/名詞)", "col": "broaden one's horizon", "ex": "Traveling helps to broaden your mind.", "pos": "v."},
    "brochure": {"def": "小冊子", "ipa": "/ˈbrəʊʃə/", "trans": "brochures", "col": "holiday brochure, informational brochure", "ex": "I picked up a holiday brochure from the travel office.", "pos": "n."},
    "broil": {"def": "烤、炙、爭吵、怒火、(在火上)烤、受酷熱", "ipa": "/brɔɪl/", "trans": "broiled", "col": "broiled chicken", "ex": "She broiled the chicken in the oven.", "pos": "n./v."},
    "broker": {"def": "經紀人、代理商、掮客、中介、安排(交易等)、做經紀人", "ipa": "/ˈbəʊkə/", "trans": "brokerage", "col": "stock broker, insurance broker", "ex": "He works as a stock broker.", "pos": "n./v."},
    "bronze": {"def": "青銅、青銅色、青銅製品、青銅色的、古銅色的、使成青銅色、鍍青銅 (青銅)", "ipa": "/brɒnz/", "trans": "bronzed", "col": "bronze medal, Bronze Age", "ex": "He won a bronze medal in the Olympics.", "pos": "n./adj./v."},
    "brooch": {"def": "胸針、領針", "ipa": "/bəʊtʃ/", "trans": "brooches", "col": "silver brooch", "ex": "She was wearing an elegant silver brooch.", "pos": "n."},
    "brood": {"def": "窩、同類、一群、沈思、孵蛋、盤算、沈思的、育雛用的 (窩)", "ipa": "/bruːd/", "trans": "brooding", "col": "brood over", "ex": "Don't brood over your mistakes.", "pos": "n./v./adj."},
    "brook": {"def": "小河、溪、忍受、容許", "ipa": "/brʊk/", "trans": "brooks", "col": "babbling brook", "ex": "The children were playing by the brook.", "pos": "n./v."},
    "broom": {"def": "掃帚、金雀花、掃除、打掃", "ipa": "/bruːm/", "trans": "brooms", "col": "new broom", "ex": "She is sweeping the floor with a broom.", "pos": "n./v."},
    "brotherhood": {"def": "兄弟關係、手足之情、兄弟會", "ipa": "/ˈbrʌðəhʊd/", "trans": "brother", "col": "spirit of brotherhood", "ex": "The organization promotes the spirit of brotherhood.", "pos": "n."},
    "brow": {"def": "額、眉、邊緣、臉色", "ipa": "/braʊ/", "trans": "brows", "col": "knit one's brows", "ex": "He wiped the sweat from his brow.", "pos": "n."},
}

with open("batch_l5_p7.json", "w", encoding="utf-8") as f:
    json.dump(L5_PART7, f, ensure_ascii=False, indent=2)
