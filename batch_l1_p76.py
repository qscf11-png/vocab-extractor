import json

# Level 1 Part 76: (Spine - Spoon)
L1_PART76 = {
    "spine": {"def": "脊椎、書脊、刺", "ipa": "/spaɪn/", "trans": "spinal, spineless", "col": "bend one's spine", "ex": "The title is printed on the spine of the book."},
    "spirit": {"def": "精神、靈魂、酒精", "ipa": "/ˈspɪrɪt/", "trans": "spirited, spiritual, spirituality", "col": "team spirit, high spirits", "ex": "He is in good spirits today."},
    "spirited": {"def": "情緒飽滿的、勇敢的", "ipa": "/ˈspɪrɪtɪd/", "trans": "spirit (名詞)", "col": "spirited debate", "ex": "They had a spirited discussion about politics."},
    "spiritual": {"def": "精神的、心靈的、宗教的", "ipa": "/ˈspɪrɪtʃuəl/", "trans": "spirituality, spirit", "col": "spiritual leader, spiritual wealth", "ex": "I am interested in spiritual matters."},
    "spit": {"def": "吐痰、噴出、唾液", "ipa": "/spɪt/", "trans": "spat, spitting", "col": "spit it out", "ex": "He spat in the street."},
    "spite": {"def": "惡意、怨恨、刁難", "ipa": "/spaɪt/", "trans": "spiteful", "col": "in spite of, out of spite", "ex": "He did it out of spite."},
    "splash": {"def": "濺落、潑灑、斑點", "ipa": "/splæʃ/", "trans": "splashed, splashing", "col": "make a splash", "ex": "A car splashed mud on my dress."},
    "splendid": {"def": "輝煌的、華麗的、極好的", "ipa": "/ˈsplendɪd/", "trans": "splendor", "col": "splendid idea", "ex": "We had a splendid time at the party."},
    "splendor": {"def": "壯麗、輝煌、顯赫", "ipa": "/ˈsplendə/", "trans": "splendid (形容詞)", "col": "military splendor", "ex": "The splendor of the sunset was amazing."},
    "split": {"def": "分裂、裂開、分享", "ipa": "/splɪt/", "trans": "splitting", "col": "split the bill, split hairs", "ex": "The party split into two factions."},
    "spoil": {"def": "腐壞、溺愛、損壞", "ipa": "/spɔɪl/", "trans": "spoiled, spoilt, spoilage", "col": "spoil one's appetite", "ex": "Don't spoil your children too much."},
    "sponge": {"def": "海綿、揩拭", "ipa": "/spʌndʒ/", "trans": "spongy", "col": "bath sponge, sponge cake", "ex": "She wiped the table with a sponge."},
    "sponsor": {"def": "贊助者、發起人、保障人", "ipa": "/ˈspɒnsə/", "trans": "sponsorship", "col": "corporate sponsor", "ex": "The event was organized by a local sponsor."},
    "sponsorship": {"def": "贊助、發起書", "ipa": "/ˈspɒnsəʃɪp/", "trans": "sponsor (動詞)", "col": "under the sponsorship of", "ex": "The racing team depends on sponsorship."},
    "spontaneous": {"def": "自發的、自然的、本能的", "ipa": "/spɒnˈteɪniəs/", "trans": "spontaneity", "col": "spontaneous applause", "ex": "The audience gave a spontaneous standing ovation."},
    "spooky": {"def": "幽靈般的、毛骨悚然的", "ipa": "/ˈspuːki/", "trans": "spook", "col": "spooky story", "ex": "I don't like spooky movies."},
    "spoon": {"def": "湯匙、匙、舀", "ipa": "/spuːn/", "trans": "spoonful", "col": "silver spoon, wooden spoon", "ex": "He ate his soup with a spoon."},
}

with open("batch_l1_p76.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART76, f, ensure_ascii=False, indent=2)
