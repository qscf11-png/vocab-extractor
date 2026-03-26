import json

# Level 1 Part 70: (Soap - Solar)
L1_PART70 = {
    "soap": {"def": "肥皂、肥皂劇", "ipa": "/səʊp/", "trans": "soapy", "col": "bar of soap, soap opera", "ex": "Wash your hands with soap."},
    "soar": {"def": "翱翔、飆升、高飛", "ipa": "/sɔː/", "trans": "soared", "col": "soaring prices", "ex": "The bird soared high in the sky."},
    "sob": {"def": "大哭、嗚咽", "ipa": "/sɒb/", "trans": "sobbing", "col": "sob bitterly", "ex": "She started to sob uncontrollably."},
    "sober": {"def": "清醒的、嚴肅的、冷靜的", "ipa": "/ˈsəʊbə/", "trans": "sobriety, sobering", "col": "stone cold sober", "ex": "He was quite sober when he left."},
    "soccer": {"def": "足球", "ipa": "/ˈsɒkə/", "trans": "football", "col": "soccer match", "ex": "They are playing soccer in the park."},
    "sociable": {"def": "好交際的、友善的", "ipa": "/ˈsəʊʃəbl/", "trans": "sociability", "col": "sociable person", "ex": "He is a very sociable man."},
    "social": {"def": "社會的、社交的、群居的", "ipa": "/ˈsəʊʃl/", "trans": "socially, socialize, society", "col": "social media, social welfare", "ex": "The Internet has changed our social lives."},
    "socialism": {"def": "社會主義", "ipa": "/ˈsəʊʃəlɪzəm/", "trans": "socialist", "col": "democratic socialism", "ex": "The political party advocates socialism."},
    "socialize": {"def": "交際、社會化", "ipa": "/ˈsəʊʃəlaɪz/", "trans": "socialization", "col": "socialize with friends", "ex": "It's important to socialize with your colleagues."},
    "socially": {"def": "在社交上", "ipa": "/ˈsəʊʃəli/", "trans": "social (形容詞)", "col": "socially acceptable", "ex": "Her behavior was not socially acceptable."},
    "society": {"def": "社會、社團、學會", "ipa": "/səˈsaɪəti/", "trans": "social (形容詞)", "col": "modern society, secret society", "ex": "We live in a multicultural society."},
    "sociology": {"def": "社會學", "ipa": "/ˌsəʊsiˈɒlədʒi/", "trans": "sociologist", "col": "professor of sociology", "ex": "She is studying sociology at university."},
    "sock": {"def": "短襪、重擊", "ipa": "/sɒk/", "trans": "socks", "col": "pair of socks", "ex": "He put on his socks and shoes."},
    "socket": {"def": "插座、孔、窩", "ipa": "/ˈsɒkɪt/", "trans": "sockets", "col": "wall socket, light socket", "ex": "Plug the lamp into the socket."},
    "soda": {"def": "蘇打、碳酸水、汽水", "ipa": "/ˈsəʊdə/", "trans": "baking soda", "col": "soda fountain", "ex": "I'll have a whiskey and soda."},
    "sodium": {"def": "鈉", "ipa": "/ˈsəʊdiəm/", "trans": "sodium (元素符號 Na)", "col": "sodium chloride", "ex": "Salt is made of sodium and chlorine."},
    "sofa": {"def": "沙發、長椅", "ipa": "/ˈsəʊfə/", "trans": "sofas", "col": "sit on the sofa", "ex": "We bought a new leather sofa."},
    "soft": {"def": "柔軟的、溫和的", "ipa": "/sɒft/", "trans": "softly, soften, softness", "col": "soft drink, soft music", "ex": "The bed was soft and comfortable."},
    "soften": {"def": "使變軟、使溫和", "ipa": "/ˈsɒfn/", "trans": "soft (形容詞)", "col": "soften the blow", "ex": "Wash the beans to soften them."},
    "softly": {"def": "柔軟地、溫和地、輕聲地", "ipa": "/ˈsɒftli/", "trans": "soft (形容詞)", "col": "speak softly", "ex": "She spoke softly to the child."},
    "software": {"def": "軟體", "ipa": "/ˈsɒftweə/", "trans": "hardware", "col": "computer software", "ex": "The software is easy to install."},
    "soil": {"def": "土壤、土地", "ipa": "/sɔɪl/", "trans": "soiled", "col": "fertile soil", "ex": "The plants grow well in this soil."},
    "solace": {"def": "慰藉、安慰", "ipa": "/ˈsɒləs/", "trans": "solaces", "col": "find solace", "ex": "Music was his only solace."},
    "solar": {"def": "太陽的、利用太陽光的", "ipa": "/ˈsəʊlə/", "trans": "solstice", "col": "solar energy, solar system", "ex": "We use solar power to heat the water."},
}

with open("batch_l1_p70.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART70, f, ensure_ascii=False, indent=2)
