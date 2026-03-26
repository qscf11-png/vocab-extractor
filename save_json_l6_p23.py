import json

# Level 6 Part 23: (Basically - Bated)
L6_PART23 = {
    "basically": {"def": "基本上、主要地、首要地", "ipa": "/ˈbeɪsɪkli/", "trans": "basic (形容詞/名詞/副詞), basis", "col": "basically the same", "ex": "The two plans are basically the same.", "pos": "adv."},
    "basil": {"def": "九層塔、羅勒", "ipa": "/ˈbeɪzl/", "trans": "herb", "col": "fresh basil", "ex": "I like to add fresh basil to my tomato sauce.", "pos": "n."},
    "basilica": {"def": "大教堂、長方形會堂", "ipa": "/bəˈzɪlɪkə/", "trans": "church", "col": "St. Peter's Basilica", "ex": "St. Peter's Basilica is a magnificent building.", "pos": "n."},
    "basilisk": {"def": "蛇怪、小蜥蜴", "ipa": "/ˈbæzɪlɪsk/", "trans": "creature", "col": "deadly basilisk", "ex": "In mythology, the basilisk's gaze could kill.", "pos": "n."},
    "basin": {"def": "盆、臉盆、流域、盆地、水池、盆狀的、水坑、水池的人、水池地 (盆)", "ipa": "/ˈbeɪsn/", "trans": "basins", "col": "wash basin, river basin, catch basin", "ex": "She filled the basin with warm water.", "pos": "n./adj./v./adv."},
    "basis": {"def": "基礎、基準、根據、原理、根據地 (根據)", "ipa": "/ˈbeɪsɪs/", "trans": "bases (複數), basic", "col": "daily basis, regular basis, on the basis that", "ex": "The decision was made on the basis of the new evidence.", "pos": "n./adv."},
    "bask": {"def": "曬太陽、沐浴於、取暖、曬的人 (或物)、曬地 (曬)", "ipa": "/bɑːsk/", "trans": "basking", "col": "bask in the sun, bask in glory", "ex": "The seals bask on the rocks in the summer sun.", "pos": "v./n./adv."},
    "basket": {"def": "籃子、簍、筐、籃框、一籃之量、籃狀的、一籃的人物、籃狀地 (籃)", "ipa": "/ˈbɑːskɪt/", "trans": "baskets", "col": "shopping basket, wastepaper basket, bread basket", "ex": "He put the apples in a basket.", "pos": "n./adj./v./adv."},
    "basketball": {"def": "籃球、籃球運動", "ipa": "/ˈbɑːskɪtbɔːl/", "trans": "basketballs", "col": "play basketball, basketball court", "ex": "He is a very good basketball player.", "pos": "n."},
    "basketry": {"def": "籃筐製作術、籃筐類", "ipa": "/ˈbɑːskɪtri/", "trans": "basketwork", "col": "primitive basketry", "ex": "Primitive basketry shows great skill.", "pos": "n."},
    "basketwork": {"def": "籃筐製品、編籃製品", "ipa": "/ˈbɑːskɪtwɜːk/", "trans": "basketry", "col": "fine basketwork", "ex": "The shop sells fine basketwork.", "pos": "n."},
    "bass": {"def": "低音、男低音、低音部、低音提琴、鱸魚、低音的、男低音的、低沉地 (低)", "ipa": "/beɪs/ (music) /bæs/ (fish)", "trans": "basses", "col": "bass guitar, double bass, bass voice, sea bass (鱸魚)", "ex": "He plays the bass guitar in a rock band.", "pos": "n./adj./adv."},
    "basset": {"def": "巴吉度獵犬、巴吉度", "ipa": "/ˈbæsɪt/", "trans": "dog", "col": "basset hound", "ex": "The basset hound has very long ears.", "pos": "n."},
    "bassoon": {"def": "低音管、巴松管", "ipa": "/bəˈsuːn/", "trans": "woodwind instrument", "col": "play the bassoon", "ex": "The bassoon provides a rich low sound in the orchestra.", "pos": "n."},
    "bassoonist": {"def": "低音管演奏者", "ipa": "/bəˈsuːnɪst/", "trans": "bassoon", "col": "professional bassoonist", "ex": "He is a professional bassoonist in the national orchestra.", "pos": "n."},
    "basswood": {"def": "椴木、菩提樹木", "ipa": "/ˈbeɪswʊd/", "trans": "linden", "col": "carved basswood", "ex": "The figure was carved from basswood.", "pos": "n."},
    "bastard": {"def": "私生子、混蛋、雜交、劣等貨、私生的、偽造的、粗俗地 (私)", "ipa": "/ˈbɑːstəd/", "trans": "illegitimate", "col": "poor bastard, lucky bastard", "ex": "Life can be a real bastard (太難了).", "pos": "n./adj./adv."},
    "baste": {"def": "塗油於、淋油、疏縫、毆打、被淋的人、疏縫地 (淋)", "ipa": "/beɪst/", "trans": "basting", "col": "baste the turkey", "ex": "Baste the turkey every 30 minutes to keep it moist.", "pos": "v./n./adv."},
    "bastion": {"def": "堡壘、要塞、捍衛者、稜堡的人物、捍衛地 (堡)", "ipa": "/ˈbæstiən/", "trans": "stronghold", "col": "last bastion of (最後陣地)", "ex": "The university is seen as a bastion of tradition.", "pos": "n./adv."},
    "bat": {"def": "蝙蝠、球棒、猛擊、眨眼、球棒的人物、猛擊地 (棒)", "ipa": "/bæt/", "trans": "bats", "col": "baseball bat, cricket bat, go to bat for (支持), blind as a bat", "ex": "He hit the ball with his bat.", "pos": "n./v./adv."},
    "batch": {"def": "一批、一組、一爐(麵包)、分批、一批的人物、分批地 (批)", "ipa": "/bætʃ/", "trans": "batches", "col": "large batch, batch of cookies, batch processing", "ex": "The first batch of cookies is ready.", "pos": "n./v./adv."},
    "bate": {"def": "減少、抑制、弱化地、抑制地 (縮)", "ipa": "/beɪt/", "trans": "bated", "col": "with bated breath (屏息地)", "ex": "They waited with bated breath for the results.", "pos": "v./adv."},
    "bated": {"def": "減少的、抑制的、屏息的", "ipa": "/ˈbeɪtɪd/", "trans": "bate (動詞/副詞)", "col": "with bated breath", "ex": "She spoke with bated breath.", "pos": "adj."},
}