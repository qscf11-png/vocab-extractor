import json

# Level 6 Part 47: (Brassiere - Bread)
L6_PART47 = {
    "brassiere": {"def": "胸罩 (正式)", "ipa": "/ˈbræziə/", "trans": "bra", "col": "formal brassiere", "ex": "The French term for bra is brassiere.", "pos": "n."},
    "brassy": {"def": "像黃銅的、厚臉皮的、刺耳的人、像黃銅地 (銅)", "ipa": "/ˈbrɑːsi/", "trans": "brass (名詞/形容詞/副詞)", "col": "brassy voice", "ex": "She has a loud and brassy voice.", "pos": "adj./n./adv."},
    "brat": {"def": "(口)頑童、惡少、乳臭未乾的小子、頑童的人物、頑童地 (頑)", "ipa": "/bræt/", "trans": "brats", "col": "spoiled brat", "ex": "He is such a spoiled brat!", "pos": "n./adv."},
    "brattish": {"def": "頑皮的、沒教養的、孩子氣的", "ipa": "/ˈbrætɪʃ/", "trans": "brat (名詞/副詞)", "col": "brattish behavior", "ex": "The movie star's brattish behavior alienated his fans.", "pos": "adj."},
    "bratty": {"def": "(俚)頑皮的、令人討厭的", "ipa": "/ˈbræti/", "trans": "brat (名詞/副詞)", "col": "bratty kid", "ex": "Stop being so bratty and share your toys.", "pos": "adj."},
    "bravado": {"def": "虛張聲勢、故作大膽、逞能的人物、虛飾地 (虛)", "ipa": "/brəˈvɑːdəʊ/", "trans": "swagger", "col": "empty bravado", "ex": "His show of courage was just empty bravado.", "pos": "n./adv."},
    "brave": {"def": "勇敢的、華麗的、勇敢地面對、勇士、勇敢的人 (或物)、勇敢地 (勇)", "ipa": "/breɪv/", "trans": "bravely, bravery", "col": "brave the elements, brave soul, as brave as a lion", "ex": "It was very brave of you to speak up.", "pos": "adj./v./n./adv."},
    "bravely": {"def": "勇敢地、剛毅地、華麗地", "ipa": "/ˈbreɪvli/", "trans": "brave (形容詞/動詞/名詞/副詞)", "col": "fought bravely", "ex": "The soldiers fought bravely against the enemy.", "pos": "adv."},
    "bravery": {"def": "勇敢、勇氣、華麗", "ipa": "/ˈbreɪvəri/", "trans": "brave (形容詞/動詞/名詞/副詞), courage", "col": "medal for bravery", "ex": "She was awarded a medal for bravery.", "pos": "n."},
    "bravo": {"def": "(感嘆詞)好哇！做的好！、喝彩、喝彩聲、擊掌的人物、擊掌地 (喝彩)", "ipa": "/ˈbrɑːvəʊ/", "trans": "well done", "col": "bravo for you", "ex": "Bravo! That was a wonderful performance.", "pos": "int./n./adv."},
    "brawl": {"def": "爭吵、打架、鬧事、爭吵的人 (或物)、爭吵地 (吵)", "ipa": "/brɔːl/", "trans": "brawling", "col": "barroom brawl", "ex": "A brawl broke out in the pub after the game.", "pos": "n./v./adv."},
    "brawler": {"def": "好爭吵者、爭吵的人 (單數)", "ipa": "/ˈbrɔːlə/", "trans": "brawl (名詞/動詞/副詞)", "col": "notorious brawler", "ex": "He is a notorious brawler who always starts trouble.", "pos": "n."},
    "brawling": {"def": "爭吵、打架的人 (或物) (吵)", "ipa": "/ˈbrɔːlɪŋ/", "trans": "brawl (名詞/動詞/副詞)", "col": "brawling crowd", "ex": "The police had to disperse the brawling crowd.", "pos": "n./adv."},
    "brawn": {"def": "肌肉、力量、筋力、肌肉的人、肌肉地 (力)", "ipa": "/brɔːn/", "trans": "brawny", "col": "brain and brawn", "ex": "He's all brawn and no brains.", "pos": "n./adv."},
    "brawny": {"def": "肌肉發達的、強壯的", "ipa": "/ˈbrɔːni/", "trans": "brawn (名詞/副詞)", "col": "brawny arms", "ex": "He has brawny arms from working in the construction.", "pos": "adj."},
    "bray": {"def": "(驢)叫、尖聲大笑、磨碎、尖叫的人 (或物)、尖叫地 (尖)", "ipa": "/breɪ/", "trans": "brays", "col": "loud bray", "ex": "The donkey let out a loud bray.", "pos": "v./n./adv."},
    "brazen": {"def": "黃銅製的、厚顏無恥的、使變得無恥、厚顏無恥地 (無恥)", "ipa": "/ˈbreɪzn/", "trans": "shameless", "col": "brazen lie, brazen behavior", "ex": "He told a brazen lie in court.", "pos": "adj./v./adv."},
    "brazenly": {"def": "無恥地、臉皮厚地、透明地 (無恥)", "ipa": "/ˈbreɪznli/", "trans": "brazen (形容詞/動詞/副詞)", "col": "lied brazenly", "ex": "He lied brazenly to his parents about where he'd been.", "pos": "adv."},
    "brazenness": {"def": "厚顏無恥、沈著氣", "ipa": "/ˈbreɪznəs/", "trans": "brazen (形容詞/動詞/副詞)", "col": "sheer brazenness", "ex": "The sheer brazenness of the theft was amazing.", "pos": "n."},
    "brazier": {"def": "火盆、火爐、黃銅匠 (單數)", "ipa": "/ˈbreɪziə/", "trans": "charcoal heater", "col": "charcoal brazier", "ex": "The travelers warmed themselves around a charcoal brazier.", "pos": "n."},
    "breach": {"def": "違反、破壞、缺口、違反法規的人、違反地 (違)", "ipa": "/briːtʃ/", "trans": "breaches", "col": "breach of contract, security breach, breach of trust", "ex": "The leak was a serious breach of security.", "pos": "n./v./adv."},
    "bread": {"def": "麵包、糧食、(俚)錢、在麵包上人物、在麵包地 (麵包)", "ipa": "/bred/", "trans": "breads", "col": "white bread, loaf of bread, daily bread, earn one's bread (謀生)", "ex": "I like to have fresh bread with my soup.", "pos": "n./v./adv."},
}