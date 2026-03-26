import json

# Level 6 Part 22: (Barren - Basic)
L6_PART22 = {
    "barren": {"def": "貧瘠的、不生育的、缺乏的、荒地、不育地 (貧瘠)", "ipa": "/ˈbærən/", "trans": "infertile", "col": "barren land, barren woman", "ex": "The land was barren and could not support crops.", "pos": "adj./n./adv."},
    "barrenness": {"def": "貧瘠、不育、荒涼", "ipa": "/ˈbærənnəs/", "trans": "barren (形容詞/名詞/副詞)", "col": "spiritual barrenness", "ex": "He was struck by the barrenness of the landscape.", "pos": "n."},
    "barrette": {"def": "髮夾 (單數)", "ipa": "/bæˈret/", "trans": "barrettes (複數)", "col": "colorful barrette", "ex": "She used a colorful barrette to pin back her hair.", "pos": "n."},
    "barricade": {"def": "路障、街壘、設路障於、阻礙、阻礙的人物、阻礙地 (阻礙)", "ipa": "/ˌbærɪˈkeɪd/", "trans": "barricades", "col": "erect a barricade", "ex": "The protesters erected a barricade across the street.", "pos": "n./v./adv."},
    "barrier": {"def": "障礙、界線、柵欄、屏障、屏障的人物、屏障地 (屏障)", "ipa": "/ˈbæriə/", "trans": "barriers", "col": "trade barrier, language barrier, barrier reef", "ex": "Language is not a barrier to our friendship.", "pos": "n./adv."},
    "barring": {"def": "除...之外、除非、不准、除外地 (除外)", "ipa": "/ˈbɑːrɪŋ/", "trans": "except for", "col": "barring accidents", "ex": "Barring accidents, we should arrive by noon.", "pos": "prep./n./adv."},
    "barrister": {"def": "(英)辯護律師 (單數)", "ipa": "/ˈbærɪstə/", "trans": "barristers (複數)", "col": "senior barrister", "ex": "He is a senior barrister specializing in criminal law.", "pos": "n."},
    "barrow": {"def": "手推車、古塚、公豬 (單數)", "ipa": "/ˈbærəʊ/", "trans": "barrows (複數)", "col": "wheel barrow", "ex": "He used a wheel barrow to move the soil.", "pos": "n."},
    "bartender": {"def": "酒保、酒吧侍者", "ipa": "/ˈbɑːtendə/", "trans": "barman", "col": "friendly bartender", "ex": "The bartender served me a drink.", "pos": "n."},
    "barter": {"def": "以物易物、交易、易貨的人 (或物)、易貨地 (易貨)", "ipa": "/ˈbɑːtə/", "trans": "bartering", "col": "barter for", "ex": "The villagers used to barter their crops for salt.", "pos": "n./v./adv."},
    "basal": {"def": "基礎的、底部的、基本的", "ipa": "/ˈbeɪsl/", "trans": "base", "col": "basal metabolism (基礎代謝)", "ex": "The test measures your basal metabolism rate.", "pos": "adj."},
    "basalt": {"def": "玄武岩", "ipa": "/ˈbæsɔːlt/", "trans": "rock", "col": "columnar basalt (柱狀玄武岩)", "ex": "The island is largely composed of basalt.", "pos": "n."},
    "base": {"def": "基礎、底部、基地、壘、卑劣的、以...為基地、基礎的人、基礎地 (底)", "ipa": "/beɪs/", "trans": "basic, basement", "col": "knowledge base, base camp, air base, common base", "ex": "The cake has a sponge base.", "pos": "n./adj./v./adv."},
    "baseball": {"def": "棒球、棒球運動", "ipa": "/ˈbeɪsbɔːl/", "trans": "baseballs", "col": "play baseball, baseball cap", "ex": "He is a huge fan of baseball.", "pos": "n."},
    "baseless": {"def": "無根據的、無底的", "ipa": "/ˈbeɪsləs/", "trans": "unfounded", "col": "baseless accusation", "ex": "The charges against him were completely baseless.", "pos": "adj."},
    "baseline": {"def": "基準線、底線", "ipa": "/ˈbeɪslaɪn/", "trans": "baselines", "col": "establish a baseline", "ex": "We need to establish a baseline for comparison.", "pos": "n."},
    "basement": {"def": "地下室、建築物的底部、基部的人 (或物)、基部地 (基部)", "ipa": "/ˈbeɪsmənt/", "trans": "basements", "col": "basement apartment", "ex": "The laundry room is in the basement.", "pos": "n./adv."},
    "baseness": {"def": "卑鄙、下賤、偽劣", "ipa": "/ˈbeɪsnəs/", "trans": "base (形容詞/名詞/動詞/副詞)", "col": "moral baseness", "ex": "He was shocked by the moral baseness of the action.", "pos": "n."},
    "bases": {"def": "(base的複數)、(basis的複數)、基礎、底部、基地 (複數)", "ipa": "/ˈbeɪsiːz/", "trans": "base/basis", "col": "military bases", "ex": "The US has several military bases in Europe.", "pos": "n."},
    "bash": {"def": "猛擊、痛擊、狂歡會、猛擊的人 (或物)、猛擊地 (猛擊)", "ipa": "/bæʃ/", "trans": "bashed", "col": "birthday bash, bash in, bash on (繼續做)", "ex": "He gave the door a hard bash.", "pos": "n./v./adv."},
    "bashful": {"def": "羞怯的、害羞的", "ipa": "/ˈbæʃfl/", "trans": "shy", "col": "bashful smile", "ex": "She gave him a bashful smile.", "pos": "adj."},
    "bashfully": {"def": "羞怯地、害羞地", "ipa": "/ˈbæʃfli/", "trans": "bashful (形容詞)", "col": "looked bashfully", "ex": "She looked bashfully at the ground.", "pos": "adv."},
    "bashfulness": {"def": "羞怯、害羞", "ipa": "/ˈbæʃflnəs/", "trans": "bashful (形容詞/副詞)", "col": "natural bashfulness", "ex": "Her natural bashfulness made it hard for her to make friends.", "pos": "n."},
    "basic": {"def": "基礎的、基本的、核心的、基本的人、基本上地 (基本)", "ipa": "/ˈbeɪsɪk/", "trans": "basically, basis", "col": "basic needs, back to basics, basic training", "ex": "Every child has a right to a basic education.", "pos": "adj./n./adv."},
}