import json

# Level 1 Part 73: (South - Speaker)
L1_PART73 = {
    "south": {"def": "南方、南部", "ipa": "/saʊθ/", "trans": "southern, southeast, southwest", "col": "South Pole, face south", "ex": "Birds fly south for the winter."},
    "southeast": {"def": "東南、東南方的", "ipa": "/ˌsaʊθˈiːst/", "trans": "southeastern", "col": "southeast Asia", "ex": "The wind was blowing from the southeast."},
    "southern": {"def": "南方的、南部的", "ipa": "/ˈsʌðən/", "trans": "south (名詞)", "col": "southern hemisphere, southern accent", "ex": "I grew up in the southern part of the country."},
    "souvenir": {"def": "紀念品、伴手禮", "ipa": "/ˌsuːvəˈnɪə/", "trans": "souvenirs", "col": "buy a souvenir", "ex": "I bought this key ring as a souvenir of my trip."},
    "sovereign": {"def": "君主、元首", "ipa": "/ˈsɒvrɪn/", "trans": "sovereignty", "col": "sovereign state", "ex": "The Queen is the sovereign of the United Kingdom."},
    "sovereignty": {"def": "主權、統治權", "ipa": "/ˈsɒvrənti/", "trans": "sovereign (形容詞)", "col": "national sovereignty", "ex": "China claims sovereignty over the islands."},
    "space": {"def": "空間、太空、距離", "ipa": "/speɪs/", "trans": "spacing, spacious, spacecraft", "col": "outer space, parking space", "ex": "Is there enough space for the car?"},
    "spacecraft": {"def": "航天器、宇宙飛船", "ipa": "/ˈspeɪskrɑːft/", "trans": "space (名詞)", "col": "manned spacecraft", "ex": "The spacecraft was launched this morning."},
    "spacious": {"def": "寬敞的、廣大的", "ipa": "/ˈspeɪʃəs/", "trans": "spaciousness", "col": "spacious room", "ex": "The house has a spacious living room."},
    "spade": {"def": "鏟子、鐵鍬、黑桃", "ipa": "/speɪd/", "trans": "spades", "col": "call a spade a spade", "ex": "He used a spade to dig the hole."},
    "span": {"def": "跨度、一段時間", "ipa": "/spæn/", "trans": "spanned", "col": "attention span, life span", "ex": "The bridge has a span of 500 meters."},
    "spare": {"def": "備用的、多餘的", "ipa": "/speə/", "trans": "sparingly", "col": "spare tire, spare time", "ex": "I have no spare cash."},
    "spark": {"def": "火花、火星、閃光", "ipa": "/spɑːk/", "trans": "sparkle, sparkling", "col": "spark an interest", "ex": "The fire gave off small sparks."},
    "sparkle": {"def": "閃閃發光、閃耀", "ipa": "/ˈspɑːkl/", "trans": "sparkling", "col": "eyes sparkle", "ex": "Their eyes sparkled with joy."},
    "sparkling": {"def": "閃爍的、起泡沫的", "ipa": "/ˈspɑːklɪŋ/", "trans": "sparkle (動詞)", "col": "sparkling water", "ex": "She was wearing a sparkling diamond ring."},
    "sparrow": {"def": "麻雀", "ipa": "/ˈspærəʊ/", "trans": "sparrows", "col": "house sparrow", "ex": "A sparrow flew onto the balcony."},
    "sparse": {"def": "稀疏的、稀少的", "ipa": "/spɑːs/", "trans": "sparsely", "col": "sparse population", "ex": "Vegetation in the desert is very sparse."},
    "speak": {"def": "說話、演講、發言", "ipa": "/spiːk/", "trans": "spoke, spoken, speaker, speech", "col": "speak up, speak for", "ex": "Can I speak to you for a moment?"},
    "speaker": {"def": "說話者、演講者", "ipa": "/ˈspiːkə/", "trans": "speak (動詞)", "col": "native speaker, loud speaker", "ex": "The speaker was excellent."},
}

with open("batch_l1_p73.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART73, f, ensure_ascii=False, indent=2)
