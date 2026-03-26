import json

# Level 1 Part 68: (Slum - Smoothly)
L1_PART68 = {
    "slum": {"def": "貧民窟、貧民區", "ipa": "/slʌm/", "trans": "slums", "col": "slum dweller, slum clearance", "ex": "He grew up in a city slum."},
    "slump": {"def": "暴跌、衰落、消沉", "ipa": "/slʌmp/", "trans": "slumped", "col": "economic slump", "ex": "Sales have slumped this year."},
    "sly": {"def": "狡猾的、淘氣的", "ipa": "/slaɪ/", "trans": "slyly", "col": "on the sly", "ex": "He's a sly old fox."},
    "smack": {"def": "滋味、拍擊、掌摑", "ipa": "/smæk/", "trans": "smacked", "col": "smack one's lips", "ex": "She gave him a smack on the cheek."},
    "small": {"def": "小的、少的、細微的", "ipa": "/smɔːl/", "trans": "smallness", "col": "small talk, small change", "ex": "It's a small world."},
    "smart": {"def": "聰明的、時髦的、刺痛", "ipa": "/smɑːt/", "trans": "smartly, smarten", "col": "smart phone, smart aleck", "ex": "He is a very smart student."},
    "smash": {"def": "粉碎、猛擊、大成功", "ipa": "/smæʃ/", "trans": "smashed", "col": "smash hit, smash into", "ex": "The car smashed into a tree."},
    "smear": {"def": "塗抹、污點、誹謗", "ipa": "/smɪə/", "trans": "smeared", "col": "smear campaign", "ex": "The child had chocolate smeared on his face."},
    "smell": {"def": "嗅覺、氣味、聞", "ipa": "/smel/", "trans": "smelled, smelt, smelly", "col": "sense of smell, smell like", "ex": "I love the smell of fresh bread."},
    "smelly": {"def": "有臭味的、難聞的", "ipa": "/ˈsmeli/", "trans": "smell (名詞)", "col": "smelly socks", "ex": "The room was hot and smelly."},
    "smile": {"def": "微笑、笑容", "ipa": "/smaɪl/", "trans": "smiling", "col": "big smile, crack a smile", "ex": "She has a beautiful smile."},
    "smiling": {"def": "微笑的、陽光的", "ipa": "/ˈsmaɪlɪŋ/", "trans": "smile (動詞)", "col": "smiling face", "ex": "He greeted us with a smiling face."},
    "smog": {"def": "煙霧、煙霞", "ipa": "/smɒɡ/", "trans": "smoggy", "col": "thick smog", "ex": "The city was covered in smog."},
    "smoke": {"def": "煙、抽煙、冒煙", "ipa": "/sməʊk/", "trans": "smoking, smoky, smoker", "col": "go up in smoke, cigar smoke", "ex": "The fire produced a lot of smoke."},
    "smoker": {"def": "吸菸者、熏製者", "ipa": "/ˈsməʊkə/", "trans": "smoke (動詞)", "col": "heavy smoker", "ex": "He used to be a heavy smoker."},
    "smoking": {"def": "抽菸、冒煙", "ipa": "/ˈsməʊkɪŋ/", "trans": "smoke (動詞)", "col": "no smoking", "ex": "Smoking is not allowed here."},
    "smoky": {"def": "多煙的、冒煙的、燻製的", "ipa": "/ˈsməʊki/", "trans": "smoke (名詞)", "col": "smoky atmosphere", "ex": "The room was filled with smoky air."},
    "smooth": {"def": "光滑的、平穩的、使光滑", "ipa": "/smuːð/", "trans": "smoothly, smoothness", "col": "smooth surface, smooth skin", "ex": "The water was as smooth as glass."},
    "smoothly": {"def": "光滑地、平穩地、利落地", "ipa": "/ˈsmuːðli/", "trans": "smooth (形容詞)", "col": "run smoothly", "ex": "The meeting went very smoothly."},
}

with open("batch_l1_p68.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART68, f, ensure_ascii=False, indent=2)
