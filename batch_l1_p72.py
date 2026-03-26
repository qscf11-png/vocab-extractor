import json

# Level 1 Part 72: (Soothe - Source)
L1_PART72 = {
    "soothe": {"def": "安慰、緩和、撫慰", "ipa": "/suːð/", "trans": "soothed, soothing", "col": "soothe a crying baby", "ex": "The music helped to soothe her nerves."},
    "soothing": {"def": "慰藉的、使人寬心的、鎮靜的", "ipa": "/ˈsuːðɪŋ/", "trans": "soothe (動詞)", "col": "soothing voice", "ex": "She has a very soothing voice."},
    "sophisticated": {"def": "精雜的、老練的、高級的", "ipa": "/səˈfɪstɪkeɪtɪd/", "trans": "sophistication", "col": "sophisticated technology", "ex": "The system is highly sophisticated."},
    "sophomore": {"def": "大學二年級生、高二學生", "ipa": "/ˈsɒfəmɔː/", "trans": "sophomores", "col": "college sophomore", "ex": "She is a sophomore at Yale."},
    "sore": {"def": "疼痛的、激怒的、痛處", "ipa": "/sɔː/", "trans": "sorely, soreness", "col": "sore throat, sore muscles", "ex": "My legs are sore after the long walk."},
    "sorrow": {"def": "悲哀、憂愁、遺憾", "ipa": "/ˈsɒrəʊ/", "trans": "sorrowful", "col": "deep sorrow", "ex": "He expressed his sorrow at the news."},
    "sorrowful": {"def": "悲傷的、受難的、慘淡的", "ipa": "/ˈsɒrəʊfl/", "trans": "sorrow (名詞)", "col": "sorrowful eyes", "ex": "She gave him a sorrowful look."},
    "sorry": {"def": "遺憾的、對不起的", "ipa": "/ˈsɒri/", "trans": "無", "col": "feel sorry for, say sorry", "ex": "I'm sorry I'm late."},
    "sort": {"def": "種類、類別、分選", "ipa": "/sɔːt/", "trans": "sorted, sorting", "col": "sort out, of some sort", "ex": "What sort of food do you like?"},
    "soul": {"def": "靈魂、心靈、核心", "ipa": "/səʊl/", "trans": "soulful, soulmate", "col": "soul music, lost soul", "ex": "She is the soul of the company."},
    "soulmate": {"def": "靈魂伴侶", "ipa": "/ˈsəʊlmeɪt/", "trans": "soul (名詞)", "col": "true soulmate", "ex": "I've finally found my soulmate."},
    "sound": {"def": "聲音、健康的、聽起來", "ipa": "/saʊnd/", "trans": "soundly, soundproof", "col": "safe and sound, ultrasound", "ex": "I heard a strange sound."},
    "soundproof": {"def": "隔音的、使隔音", "ipa": "/ˈsaʊndpruːf/", "trans": "sound (名詞)", "col": "soundproof room", "ex": "The studio is completely soundproof."},
    "soup": {"def": "湯、羹、濃霧", "ipa": "/suːp/", "trans": "soups", "col": "bowl of soup, tomato soup", "ex": "Would you like some soup?"},
    "sour": {"def": "酸的、發酵的、變酸", "ipa": "/ˈsʊə/", "trans": "sourly, sourness", "col": "sour grapes, go sour", "ex": "The milk has gone sour."},
    "source": {"def": "來源、水源、原始資料", "ipa": "/sɔːs/", "trans": "sources", "col": "energy source, primary source", "ex": "What is the source of the news?"},
}

with open("batch_l1_p72.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART72, f, ensure_ascii=False, indent=2)
