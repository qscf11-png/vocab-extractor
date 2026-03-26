import json

# Level 6 Part 53: (Browbeat - Bubonic)
L6_PART53 = {
    "browbeat": {"def": "威嚇、嚇唬、恐嚇、嚇唬的人 (或物)、嚇唬地 (嚇)", "ipa": "/ˈbraʊbiːt/", "trans": "intimidate", "col": "browbeat into", "ex": "Don't let them browbeat you into doing something you don't want to.", "pos": "v./n./adv."},
    "brown": {"def": "褐色的、棕色的、褐色、曬黑、烤焦、褐色的人物、褐色地 (褐)", "ipa": "/braʊn/", "trans": "browned, brownish", "col": "brown sugar, brown bread, brown paper bag", "ex": "The leaves are starting to turn brown.", "pos": "adj./n./v./adv."},
    "brownie": {"def": "布朗尼(巧克力蛋糕)、(童軍)幼女童軍、家精的人物 (單數)", "ipa": "/ˈbraʊni/", "trans": "brownies (複數)", "col": "chocolate brownie, earn brownie points (討好/爭取表現)", "ex": "She baked a tray of chocolate brownies.", "pos": "n."},
    "browning": {"def": "變褐色、曬黑的人 (或物) (褐)", "ipa": "/ˈbraʊnɪŋ/", "trans": "brown (名詞/動詞/副詞)", "col": "browning reaction", "ex": "The browning of the fruit is caused by oxidation.", "pos": "n./adv."},
    "brownish": {"def": "帶褐色的", "ipa": "/ˈbraʊnɪʃ/", "trans": "brown", "col": "brownish grey", "ex": "The bird has brownish feathers with white spots.", "pos": "adj."},
    "brownout": {"def": "部分停電、電壓不足 (單數)", "ipa": "/ˈbraʊnaʊt/", "trans": "power dip", "col": "unplanned brownout", "ex": "The city suffered a brief brownout during the heavy storm.", "pos": "n."},
    "browse": {"def": "瀏覽、翻閱、(獸)吃草、吃草地 (閱)", "ipa": "/braʊz/", "trans": "browser, browsing", "col": "browse the web, browse through", "ex": "I was just browsing through some magazines.", "pos": "v./n./adv."},
    "browser": {"def": "瀏覽器、翻閱者、吃草的動物 (單數)", "ipa": "/ˈbraʊzə/", "trans": "browsers (複數)", "col": "web browser, safari browser", "ex": "Which web browser do you prefer to use?", "pos": "n."},
    "browsing": {"def": "瀏覽、翻閱的人 (或物) (閱)", "ipa": "/ˈbraʊzɪŋ/", "trans": "browse (名詞/動詞/副詞)", "col": "safe browsing", "ex": "Spending too much time browsing social media can be unproductive.", "pos": "n./adv."},
    "brr": {"def": "(感嘆詞) 哆嗦！(表示冷) (冷)", "ipa": "/brɜː/", "trans": "cold", "col": "brr, it's freezing!", "ex": "Brr! It's freezing in this wind.", "pos": "int."},
    "bruise": {"def": "青腫、擦傷、瘀傷、碰傷、受傷的人 (或物)、受傷地 (瘀)", "ipa": "/bruːz/", "trans": "bruised, bruising", "col": "bruised ego, bad bruise", "ex": "She has a nasty bruise on her leg.", "pos": "n./v./adv."},
    "bruised": {"def": "淤青的、碰傷的、受打擊的的人 (或物) (青)", "ipa": "/bruːzd/", "trans": "bruise (名詞/動詞/副詞)", "col": "bruised feelings", "ex": "He had a badly bruised shoulder from the fall.", "pos": "adj./adv."},
    "bruiser": {"def": "(口)彪形大漢、打手、拳擊者 (單數)", "ipa": "/ˈbruːzə/", "trans": "thug", "col": "hired bruiser", "ex": "A couple of big bruisers were guarding the entrance.", "pos": "n."},
    "bruising": {"def": "青腫、瘀傷、激烈的人 (或物) (瘀)", "ipa": "/ˈbruːzɪŋ/", "trans": "bruise (名詞/動詞/副詞)", "col": "extensive bruising, bruising encounter", "ex": "The doctor noted extensive bruising on the patient's arm.", "pos": "n./adj./adv."},
    "bruit": {"def": "散佈、傳播、傳聞、散佈的人 (或物)、傳聞地 (傳)", "ipa": "/bruːt/", "trans": "rumor", "col": "bruit about", "ex": "The news was bruited about the city throughout the day.", "pos": "v./n./adv."},
    "brunch": {"def": "早午餐、吃早午餐、早午餐地 (早午餐)", "ipa": "/brʌntʃ/", "trans": "brunches", "col": "Sunday brunch", "ex": "We had a long Sunday brunch at our favorite cafe.", "pos": "n./v./adv."},
    "brunette": {"def": "深褐色頭髮的、深褐色頭髮的女人 (單數)、褐色地 (褐)", "ipa": "/bruːˈnet/", "trans": "dark-haired", "col": "stunning brunette", "ex": "She is a stunning brunette with bright blue eyes.", "pos": "adj./n./adv."},
    "brunt": {"def": "衝擊、主力、矛頭、主要的力量的人、最重地 (衝)", "ipa": "/brʌnt/", "trans": "impact", "col": "bear the brunt of (承受...的衝擊)", "ex": "Small businesses bore the brunt of the recession.", "pos": "n./adv."},
    "brush": {"def": "刷子、筆、灌木叢、刷、拂、輕碰、刷的人、刷地 (刷)", "ipa": "/brʌʃ/", "trans": "brushes, brushing", "col": "toothbrush, paintbrush, hairbrush, brush aside (不理會), brush up on (溫習)", "ex": "He used a soft brush to clean his camera.", "pos": "n./v./adj./adv."},
    "brushed": {"def": "刷過的、有拉絨的的人 (或物) (刷)", "ipa": "/brʌʃt/", "trans": "brush (名詞/動詞/副詞)", "col": "brushed cotton, brushed aluminum", "ex": "The brushed aluminum finish looks very modern.", "pos": "adj./adv."},
    "brushing": {"def": "刷、輕拂的人 (或物) (刷)", "ipa": "/ˈbrʌʃɪŋ/", "trans": "brush (名詞/動詞/副詞)", "col": "brushing teeth", "ex": "Brushing your teeth twice a day is essential.", "pos": "n./adv."},
    "brush-off/brushoff": {"def": "(口)拒絕、冷落、不理睬的人物、不理睬地 (拒絕)", "ipa": "/ˈbrʌʃɒf/", "trans": "rejection", "col": "give the brush-off", "ex": "She gave me a complete brush-off when I tried to apologize.", "pos": "n./adv."},
    "brushwood": {"def": "灌木叢、柴薪 (單數)", "ipa": "/ˈbrʌʃwʊd/", "trans": "kindling", "col": "dry brushwood", "ex": "They gathered dry brushwood to start the campfire.", "pos": "n."},
    "brushwork": {"def": "(畫)筆觸、畫風 (單數)", "ipa": "/ˈbrʌʃwɜːk/", "trans": "technique", "col": "expert brushwork", "ex": "The painting is famous for its bold, expressive brushwork.", "pos": "n."},
    "brusque": {"def": "唐突的、魯莽的、無禮地 (莽)", "ipa": "/bruːsk/", "trans": "abrupt", "col": "brusque manner", "ex": "His brusque manner offended many of his colleagues.", "pos": "adj./adv."},
    "brusquely": {"def": "唐突地、魯莽地、無禮地", "ipa": "/ˈbruːskli/", "trans": "brusque (形容詞/副詞)", "col": "answered brusquely", "ex": "He answered brusquely and hung up the phone.", "pos": "adv."},
    "brusqueness": {"def": "唐突、魯莽、無禮", "ipa": "/ˈbruːsknəs/", "trans": "brusque (形容詞/副詞)", "col": "typical brusqueness", "ex": "We were surprised by the brusqueness of his reply.", "pos": "n."},
    "brutal": {"def": "殘忍的、獸性的、野蠻的、冷峻的、殘忍的人、殘忍地 (殘忍)", "ipa": "/ˈbruːtl/", "trans": "brutally, brutality", "col": "brutal murder, brutal attack, brutal honesty", "ex": "The movie depicts a brutal war in detail.", "pos": "adj./n./adv."},
    "brutality": {"def": "殘酷、暴行、獸性 (單數)", "ipa": "/bruːˈtæləti/", "trans": "brutalities (複數)", "col": "police brutality", "ex": "The report condemned the brutality of the regime.", "pos": "n."},
    "brutalize": {"def": "使殘忍、使獸化、殘忍地對待的人、殘忍地 (化)", "ipa": "/ˈbruːtəlaɪz/", "trans": "brutalizing", "col": "brutalize prisoners", "ex": "Years of war had brutalized the entire population.", "pos": "v./n./adv."},
    "brutally": {"def": "殘忍地、野蠻地、無情地 (殘忍)", "ipa": "/ˈbruːtəli/", "trans": "brutal (形容詞/名詞/副詞)", "col": "brutally honest", "ex": "He was brutally honest about her lack of talent.", "pos": "adv."},
    "brute": {"def": "畜生、禽獸、粗野的人、殘忍的、體力的、畜生的人、畜生地 (畜)", "ipa": "/bruːt/", "trans": "brutish", "col": "brute force (蠻力), complete brute", "ex": "His father was a drunken brute.", "pos": "n./adj./adv."},
    "brutish": {"def": "畜生般的、殘忍的、粗魯的", "ipa": "/ˈbruːtɪʃ/", "trans": "brute (名詞/形容詞/副詞)", "col": "brutish behavior", "ex": "His brutish behavior was criticized by everyone.", "pos": "adj."},
    "bubble": {"def": "泡泡、氣泡、幻想、起泡、在泡泡中人物、冒泡地 (泡)", "ipa": "/ˈbʌbl/", "trans": "bubbly", "col": "soap bubble, financial bubble, burst the bubble, bubble over with excitement", "ex": "The children enjoyed blowing soap bubbles.", "pos": "n./v./adv."},
    "bubble-bath/bubble bath": {"def": "泡泡浴 (單數)", "ipa": "/ˈbʌbl ˌbɑːθ/", "trans": "baths", "col": "relaxing bubble bath", "ex": "I like to have a relaxing bubble bath after a long day.", "pos": "n."},
    "bubble-gum/bubblegum": {"def": "泡泡糖 (單數)", "ipa": "/ˈbʌblɡʌm/", "trans": "candy", "col": "chew bubblegum", "ex": "The little boy was blowing big bubbles with his bubblegum.", "pos": "n."},
    "bubbly": {"def": "多泡的、(口)香檳酒、充滿活力的的人、多泡地 (泡)", "ipa": "/ˈbʌbli/", "trans": "bubble (名詞/動詞/副詞)", "col": "bubbly personality, glass of bubbly", "ex": "She has a very bubbly personality.", "pos": "adj./n./adv."},
    "bubonic": {"def": "腹股溝腺炎的、鼠疫的 (單數)", "ipa": "/bjuːˈbɒnɪk/", "trans": "plague", "col": "bubonic plague (黑死病)", "ex": "The bubonic plague killed millions of people in the Middle Ages.", "pos": "n./adj."},
}

with open("batch_l6_p53.json", "w", encoding="utf-8") as f:
    json.dump(L6_PART53, f, ensure_ascii=False, indent=2)
 Hillary (deleted)
...
Hillary (deleted)
