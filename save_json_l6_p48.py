import json

# Level 6 Part 48: (Breadcrumb - Breast)
L6_PART48 = {
    "breadcrumb": {"def": "麵包屑、(網)導航路徑 (單數)", "ipa": "/ˈbredkrʌm/", "trans": "breadcrumbs (複數)", "col": "coating of breadcrumbs", "ex": "Dip the fish in egg and then in breadcrumbs.", "pos": "n."},
    "breaded": {"def": "裹了麵包屑的", "ipa": "/ˈbredɪd/", "trans": "bread (名詞/動詞/副詞)", "col": "breaded chicken breast", "ex": "I'll have the breaded scampi, please.", "pos": "adj."},
    "breadfruit": {"def": "麵包樹果實", "ipa": "/ˈbredfruːt/", "trans": "fruit", "col": "ripe breadfruit", "ex": "Breadfruit is a staple food in many tropical regions.", "pos": "n."},
    "breadline": {"def": "領取救濟食物的隊伍、貧窮線", "ipa": "/ˈbredlaɪn/", "trans": "poverty line", "col": "on the breadline (生活極度貧困)", "ex": "Many families are living on the breadline.", "pos": "n."},
    "breadth": {"def": "寬度、幅度、廣博 (單數)", "ipa": "/bredθ/", "trans": "width", "col": "breadth of knowledge, breadth of experience", "ex": "The breadth of his knowledge is amazing.", "pos": "n."},
    "breadthways/breadthwise": {"def": "橫向地、寬度地", "ipa": "/ˈbredθweɪz/", "trans": "breadth (名詞)", "col": "folded breadthways", "ex": "The fabric was folded breadthways.", "pos": "adv."},
    "breadwinner": {"def": "負擔家計的人、養家活口者", "ipa": "/ˈbredwɪnə/", "trans": "provider", "col": "sole breadwinner", "ex": "He is the sole breadwinner for a family of six.", "pos": "n."},
    "break": {"def": "打破、弄碎、中斷、休息、突破、打破的人 (或物)、打破地 (破)", "ipa": "/breɪk/", "trans": "breaking, broken, broke", "col": "lunch break, break the law, break down, break even (收支平衡)", "ex": "Be careful not to break the glass.", "pos": "v./n./adv."},
    "breakable": {"def": "易碎的、易碎物品的、易碎的人 (或物) (易)", "ipa": "/ˈbreɪkəbl/", "trans": "break (名詞/動詞/副詞)", "col": "handle with care - breakable", "ex": "The box was marked 'Breakable - Handle with care'.", "pos": "adj./n./adv."},
    "breakage": {"def": "破碎、損壞、破碎物 (單數)", "ipa": "/ˈbreɪkɪdʒ/", "trans": "break (名詞/動詞/副詞)", "col": "cover for breakage", "ex": "The insurance policy covers accidental breakage.", "pos": "n."},
    "breakaway": {"def": "脫離、背叛、脫離的、背叛的人 (或物)、脫離地 (離)", "ipa": "/ˈbreɪkəweɪ/", "trans": "separation", "col": "breakaway group, breakaway republic", "ex": "He is a member of a breakaway political party.", "pos": "n./adj./adv."},
    "breakdown": {"def": "故障、崩潰、明細、分類的人 (或物)、崩潰地 (崩)", "ipa": "/ˈbreɪkdaʊn/", "trans": "failure", "col": "nervous breakdown, mechanical breakdown, cost breakdown", "ex": "The car suffered a mechanical breakdown on the motorway.", "pos": "n./adv."},
    "breaker": {"def": "破浪、斷路器、打破者 (單數)", "ipa": "/ˈbreɪkə/", "trans": "break (名詞/動詞/副詞)", "col": "circuit breaker, wave breaker", "ex": "The circuit breaker tripped because of the overload.", "pos": "n."},
    "breakfast": {"def": "早餐、吃早餐、早餐地 (早餐)", "ipa": "/ˈbrekfəst/", "trans": "breakfasts", "col": "English breakfast, have breakfast", "ex": "What did you have for breakfast today?", "pos": "n./v./adv."},
    "breaking": {"def": "破壞、打破、正在發生的人 (或物) (破)", "ipa": "/ˈbreɪkɪŋ/", "trans": "break (名詞/動詞/副詞)", "col": "breaking news, breaking point", "ex": "The news organization was the first to report the breaking news.", "pos": "adj./n./adv."},
    "breakneck": {"def": "極快的、危險的、斷頭台地 (快)", "ipa": "/ˈbreɪknek/", "trans": "dangerously fast", "col": "breakneck speed", "ex": "The car was traveling at a breakneck speed.", "pos": "adj./adv."},
    "breakout": {"def": "爆發、突圍、越獄、小組討論、爆發的人 (或物)、爆發地 (爆)", "ipa": "/ˈbreɪkaʊt/", "trans": "escape", "col": "prison breakout, breakout session, disease breakout", "ex": "There was a massive prison breakout last night.", "pos": "n./adj./adv."},
    "breakthrough": {"def": "突破、重大發現、突破性的、突破的人 (或物)、突破地 (突破)", "ipa": "/ˈbreɪkθruː/", "trans": "discovery", "col": "scientific breakthrough, major breakthrough", "ex": "Scientists have made a major breakthrough in cancer research.", "pos": "n./adj./adv."},
    "break-up/breakup": {"def": "破裂、解散、分手、終止的一個人、破裂地 (分)", "ipa": "/ˈbreɪkʌp/", "trans": "splitting up", "col": "marriage break-up, family break-up", "ex": "The break-up of the Soviet Union changed the world.", "pos": "n./adv."},
    "breakwater": {"def": "防波堤 (單數)", "ipa": "/ˈbreɪkwɔːtə/", "trans": "breakwaters (複數)", "col": "concrete breakwater", "ex": "The new concrete breakwater protects the harbor from storm waves.", "pos": "n."},
    "bream": {"def": "鯛魚、鯿魚、清船底、清船的人 (或物) (魚)", "ipa": "/briːm/", "trans": "fish", "col": "sea bream", "ex": "Sea bream can be delicious when grilled with herbs.", "pos": "n./v./adv."},
    "breast": {"def": "胸部、乳房、心情、挺胸面對、胸前、胸部地 (胸)", "ipa": "/brest/", "trans": "breasts", "col": "breast cancer, chicken breast, keep abreast of (保持聯繫), beat one's breast (捶胸頓足)", "ex": "She was diagnosed with breast cancer.", "pos": "n./v./adj./adv."},
}