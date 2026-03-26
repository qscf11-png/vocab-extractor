import json

# Level 1 Part 52: (Raft - Rank)
L1_PART52 = {
    "raft": {"def": "木筏、救生橡皮艇、大量、用筏運送", "ipa": "/rɑːft/", "trans": "rafts", "col": "life raft, raft of measures", "ex": "They crossed the river on a raft."},
    "rag": {"def": "破布、碎布、低級報紙、戲弄、捉弄", "ipa": "/ræɡ/", "trans": "rags, ragged", "col": "rag and bone, in rags", "ex": "He wiped the oil with a rag."},
    "rage": {"def": "盛怒、狂暴、流行、發怒、狂吹", "ipa": "/reɪdʒ/", "trans": "raged", "col": "road rage, fly into a rage", "ex": "He was shaking with rage."},
    "ragged": {"def": "破爛的、衣衫襤褸的、參差不齊的", "ipa": "/ˈræɡɪd/", "trans": "raggedly", "col": "ragged clothes", "ex": "The beggar wore ragged clothes."},
    "raid": {"def": "襲擊、搜捕、劫掠、突襲", "ipa": "/reɪd/", "trans": "raided", "col": "air raid, police raid", "ex": "The police carried out a raid on the house."},
    "rail": {"def": "欄杆、扶手、鐵軌、鐵路", "ipa": "/reɪl/", "trans": "railing, railroad, railway", "col": "by rail, go off the rails", "ex": "He leaned against the rail."},
    "railing": {"def": "欄杆、圍欄", "ipa": "/ˈreɪlɪŋ/", "trans": "railings", "col": "iron railings", "ex": "She held onto the railings for support."},
    "railroad": {"def": "鐵路、強迫...做、急忙行事", "ipa": "/ˈreɪlrəʊd/", "trans": "railroads", "col": "transcontinental railroad", "ex": "The railroad connects the two cities."},
    "railway": {"def": "鐵路、鐵道", "ipa": "/ˈreɪlweɪ/", "trans": "railways", "col": "railway station", "ex": "Traveling by railway is very convenient."},
    "rain": {"def": "雨、下雨、雨點般落下", "ipa": "/reɪn/", "trans": "rains, rainy, rainfall", "col": "heavy rain, pour with rain", "ex": "It's starting to rain."},
    "rainbow": {"def": "彩虹", "ipa": "/ˈreɪnbəʊ/", "trans": "rainbows", "col": "double rainbow", "ex": "Look at the beautiful rainbow!"},
    "raincoat": {"def": "雨衣", "ipa": "/ˈreɪnkəʊt/", "trans": "raincoats", "col": "yellow raincoat", "ex": "Don't forget your raincoat."},
    "raindrop": {"def": "雨滴", "ipa": "/ˈreɪndrɒp/", "trans": "raindrops", "col": "patter of raindrops", "ex": "Raindrops were drumming on the roof."},
    "rainfall": {"def": "降雨、降雨量", "ipa": "/ˈreɪnfɔːl/", "trans": "無", "col": "annual rainfall", "ex": "The average annual rainfall is high."},
    "rainforest": {"def": "熱帶雨林", "ipa": "/ˈreɪnfɒrɪst/", "trans": "rainforests", "col": "tropical rainforest", "ex": "The Amazon is a vast rainforest."},
    "rainstorm": {"def": "暴雨", "ipa": "/ˈreɪnstɔːm/", "trans": "rainstorms", "col": "sudden rainstorm", "ex": "They were caught in a rainstorm."},
    "rainy": {"def": "下雨的、多雨的", "ipa": "/ˈreɪni/", "trans": "rain (名詞)", "col": "rainy day, rainy season", "ex": "I hate rainy weather."},
    "raise": {"def": "舉起、提高、養育、籌集、加薪", "ipa": "/reɪz/", "trans": "raised", "col": "raise money, raise children", "ex": "Raise your hand if you have a question."},
    "raisin": {"def": "葡萄乾", "ipa": "/ˈreɪzn/", "trans": "raisins", "col": "sun dried raisin", "ex": "I like raisins in my cereal."},
    "rally": {"def": "集會、重整旗鼓、反彈、召集", "ipa": "/ˈræli/", "trans": "rallied", "col": "political rally, car rally", "ex": "Thousands attended the peace rally."},
    "ram": {"def": "公羊、撞擊裝置、猛撞、填塞", "ipa": "/ræm/", "trans": "rammed", "col": "battering ram", "ex": "The car rammed into the wall."},
    "ramble": {"def": "漫步、漫談、閒逛、漫步(名詞)", "ipa": "/ˈræmbl/", "trans": "rambled, rambler", "col": "go for a ramble", "ex": "We went for a ramble in the woods."},
    "ramification": {"def": "後果、影響、分枝、衍生物", "ipa": "/ˌræmɪfɪˈkeɪʃn/", "trans": "ramifications", "col": "legal ramifications", "ex": "Think about the ramifications of your decision."},
    "ramp": {"def": "斜面、坡道、敲詐、亂跳", "ipa": "/ræmp/", "trans": "ramps", "col": "wheelchair ramp", "ex": "The building has a wheelchair ramp."},
    "rampant": {"def": "猖獗的、蔓延的、茂盛的、繁茂的", "ipa": "/ˈræmpənt/", "trans": "rampantly", "col": "run rampant", "ex": "Corruption is rampant in the country."},
    "rampart": {"def": "城牆、壁壘、防護、保護", "ipa": "/ˈræmpɑːt/", "trans": "ramparts", "col": "castle ramparts", "ex": "The soldiers stood on the ramparts."},
    "ranch": {"def": "大牧場、大農場、經營牧場", "ipa": "/rɑːntʃ/", "trans": "ranches, rancher", "col": "cattle ranch", "ex": "He works on a cattle ranch."},
    "rancher": {"def": "牧場主人、牧場工人", "ipa": "/ˈrɑːntʃə/", "trans": "ranch (名詞)", "col": "local rancher", "ex": "The rancher is breeding horses."},
    "rancid": {"def": "腐臭的、味道敗壞的、令人作嘔的", "ipa": "/ˈrænsɪd/", "trans": "rancidity", "col": "rancid butter", "ex": "The butter has gone rancid."},
    "rancor": {"def": "怨恨、深仇", "ipa": "/ˈræŋkə/", "trans": "rancorous", "col": "without rancor", "ex": "They parted without any rancor."},
    "random": {"def": "隨機的、任意的、胡亂的人物", "ipa": "/ˈrændəm/", "trans": "randomly", "col": "at random", "ex": "The winners were chosen at random."},
    "randomly": {"def": "隨機地、任意地", "ipa": "/ˈrændəmli/", "trans": "random (形容詞)", "col": "scattered randomly", "ex": "The names were listed randomly."},
    "range": {"def": "範圍、山脈、射程、爐灶", "ipa": "/reɪndʒ/", "trans": "ranged", "col": "mountain range, age range", "ex": "The price is within your range."},
    "ranger": {"def": "遊騎兵、護林員、漫遊者", "ipa": "/ˈreɪndʒə/", "trans": "rangers", "col": "park ranger", "ex": "The park ranger helped us find the trail."},
    "rank": {"def": "等級、軍階、行列、排列、評定", "ipa": "/ræŋk/", "trans": "ranks, ranked", "col": "high rank, rank and file", "ex": "He rose to the rank of captain."},
}

with open("batch_l1_p52.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART52, f, ensure_ascii=False, indent=2)
