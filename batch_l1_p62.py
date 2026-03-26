import json

# Level 1 Part 62: (Sheriff - Shoreline)
L1_PART62 = {
    "sheriff": {"def": "縣執法官、司法長官", "ipa": "/ˈʃerɪf/", "trans": "sheriffs", "col": "local sheriff", "ex": "The sheriff is responsible for law enforcement in the county."},
    "shield": {"def": "盾、盾狀物、保護者", "ipa": "/ʃiːld/", "trans": "shielded", "col": "human shield, shield from light", "ex": "He used his hand to shield his eyes from the sun."},
    "shift": {"def": "轉向、移動、轉移", "ipa": "/ʃɪft/", "trans": "shifted, shifting", "col": "night shift, shift focus", "ex": "Public opinion has begun to shift."},
    "shimmer": {"def": "闪烁、發微光、微光", "ipa": "/ˈʃɪmə/", "trans": "shimmering", "col": "shimmer in the moonlight", "ex": "The sea shimmered in the sunlight."},
    "shin": {"def": "脛部、脛骨、爬", "ipa": "/ʃɪn/", "trans": "shins", "col": "shin bone", "ex": "He kicked me in the shin."},
    "shine": {"def": "發光、閃耀、出眾", "ipa": "/ʃaɪn/", "trans": "shone, shiny, shining", "col": "rise and shine, rain or shine", "ex": "The sun is shining brightly."},
    "shingle": {"def": "鵝卵石、木瓦、小招牌", "ipa": "/ˈʃɪŋɡl/", "trans": "shingles", "col": "shingle beach", "ex": "The roof was covered with cedar shingles."},
    "shining": {"def": "光亮的、華麗的、優秀的", "ipa": "/ˈʃaɪnɪŋ/", "trans": "shine (動詞)", "col": "shining example", "ex": "He is a shining example of success."},
    "shiny": {"def": "光亮的、擦亮的、晴朗的", "ipa": "/ˈʃaɪni/", "trans": "shimmer", "col": "shiny new car", "ex": "She has shiny black hair."},
    "ship": {"def": "船、艦、宇宙飛船", "ipa": "/ʃɪp/", "trans": "shipped, shipping, shipment", "col": "by ship, passenger ship", "ex": "The goods were sent by ship."},
    "shipment": {"def": "裝船、裝運、貨物", "ipa": "/ˈʃɪpmənt/", "trans": "ship (動詞)", "col": "large shipment", "ex": "The first shipment of aid has arrived."},
    "shipping": {"def": "海運、航運、船舶", "ipa": "/ˈʃɪpɪŋ/", "trans": "ship (動詞)", "col": "shipping agent, shipping costs", "ex": "Shipping is a major industry in this country."},
    "shipwreck": {"def": "海難、船舶失事、失事", "ipa": "/ˈʃɪprek/", "trans": "shipwrecks", "col": "surivive a shipwreck", "ex": "The shipwreck lies on the ocean floor."},
    "shirt": {"def": "襯衫、內衣", "ipa": "/ʃɜːt/", "trans": "shirts", "col": "white shirt, T-shirt", "ex": "He wore a clean white shirt."},
    "shiver": {"def": "發抖、打顫、震碎", "ipa": "/ˈʃɪvə/", "trans": "shivered", "col": "shiver with cold", "ex": "The cold wind made me shiver."},
    "shoal": {"def": "淺灘、魚群、成群", "ipa": "/ʃəʊl/", "trans": "shoals", "col": "shoal of fish", "ex": "A large shoal of fish swam past."},
    "shock": {"def": "震驚、衝擊、休克", "ipa": "/ʃɒk/", "trans": "shocked, shocking", "col": "electric shock, culture shock", "ex": "The news came as a great shock to her."},
    "shocked": {"def": "震驚的、受驚的", "ipa": "/ʃɒkt/", "trans": "shock (名詞)", "col": "deeply shocked", "ex": "We were shocked by the sudden news."},
    "shocking": {"def": "令人震驚的、糟糕的", "ipa": "/ˈʃɒkɪŋ/", "trans": "shockingly", "col": "shocking news", "ex": "The conditions in the prison were shocking."},
    "shoddy": {"def": "劣質的、卑鄙的、贗品", "ipa": "/ˈʃɒdi/", "trans": "shoddiness", "col": "shoddy workmanship", "ex": "The house was built with shoddy materials."},
    "shoe": {"def": "鞋、鞋狀物、蹄鐵", "ipa": "/ʃuː/", "trans": "shoes, shoemaker", "col": "pair of shoes, in someone's shoes", "ex": "She put on her shoes and went out."},
    "shoemaker": {"def": "鞋匠", "ipa": "/ˈʃuːmeɪkə/", "trans": "shoe (名詞)", "col": "master shoemaker", "ex": "The shoemaker repaired my boots."},
    "shoot": {"def": "射擊、發射、攝影", "ipa": "/ʃuːt/", "trans": "shot, shooting", "col": "shoot a movie, shoot a goal", "ex": "Don't shoot the messenger."},
    "shooting": {"def": "射擊、狩獵、攝影", "ipa": "/ˈʃuːtɪŋ/", "trans": "shoot (動詞)", "col": "shooting star", "ex": "There was a shooting in the city center."},
    "shop": {"def": "商店、工廠、購物", "ipa": "/ʃɒp/", "trans": "shopper, shopping, shopkeeper", "col": "set up shop, window shopping", "ex": "I'm going to the shop for some milk."},
    "shopkeeper": {"def": "店主、零售商", "ipa": "/ˈʃɒpkiːpə/", "trans": "shop (名詞)", "col": "local shopkeeper", "ex": "The shopkeeper was very helpful."},
    "shopper": {"def": "購物者", "ipa": "/ˈʃɒpə/", "trans": "shop (動詞)", "col": "Christmas shoppers", "ex": "The mall was full of shoppers."},
    "shopping": {"def": "購物、買來的東西", "ipa": "/ˈʃɒpɪŋ/", "trans": "shop (動詞)", "col": "go shopping, shopping mall", "ex": "I like doing my shopping online."},
    "shore": {"def": "岸、濱、支撐", "ipa": "/ʃɔː/", "trans": "shoreline", "col": "on shore, offshore", "ex": "The waves crashed against the shore."},
    "shoreline": {"def": "海岸線、湖岸線", "ipa": "/ˈʃɔːlaɪn/", "trans": "shore (名詞)", "col": "rugged shoreline", "ex": "We walked along the rocky shoreline."},
}

with open("batch_l1_p62.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART62, f, ensure_ascii=False, indent=2)
