import json

# Level 1 Part 69: (Smother - Soaked)
L1_PART69 = {
    "smother": {"def": "窒息、悶死、壓制", "ipa": "/ˈsmʌðə/", "trans": "smothered", "col": "smother with kisses", "ex": "Don't smother the fire; it needs air."},
    "smuggle": {"def": "走私、私運、偷運", "ipa": "/ˈsmʌɡl/", "trans": "smuggled, smuggler, smuggling", "col": "smuggle drugs", "ex": "They tried to smuggle gold into the country."},
    "smuggler": {"def": "走私者、私運船", "ipa": "/ˈsmʌɡlə/", "trans": "smuggle (動詞)", "col": "arms smuggler", "ex": "The smuggler was caught at the border."},
    "smuggling": {"def": "走私、私運", "ipa": "/ˈsmʌɡlɪŋ/", "trans": "smuggle (動詞)", "col": "antiques smuggling", "ex": "He was arrested for smuggling."},
    "snack": {"def": "零食、點心", "ipa": "/snæk/", "trans": "snacks", "col": "quick snack", "ex": "I like to have a snack between meals."},
    "snail": {"def": "蝸牛、慢性子的人", "ipa": "/sneɪl/", "trans": "snails", "col": "snail mail", "ex": "The snail moved slowly across the leaf."},
    "snake": {"def": "蛇、陰險之人", "ipa": "/sneɪk/", "trans": "snakes, snaky", "col": "poisonous snake", "ex": "She is terrified of snakes."},
    "snap": {"def": "砰然折斷、快照", "ipa": "/snæp/", "trans": "snapped, snappy, snapshot", "col": "snap one's fingers, snap a picture", "ex": "The dry branch snapped under his weight."},
    "snapshot": {"def": "快照、簡略情況", "ipa": "/ˈsnæpʃɒt/", "trans": "snapshots", "col": "family snapshot", "ex": "I took a snapshot of the kids playing."},
    "snare": {"def": "陷阱、圈套、誘捕", "ipa": "/sneə/", "trans": "snared", "col": "rabbit snare", "ex": "The fox was caught in a snare."},
    "snatch": {"def": "奪取、搶奪、碎片", "ipa": "/snætʃ/", "trans": "snatched", "col": "snatch a victory", "ex": "The thief snatched her purse and ran off."},
    "sneak": {"def": "潛行、溜、偷竊", "ipa": "/sniːk/", "trans": "sneaked, snuck, sneaker", "col": "sneak in, sneak peek", "ex": "He tried to sneak out of the room."},
    "sneaker": {"def": "運動鞋、鬼鬼祟祟的人", "ipa": "/ˈsniːkə/", "trans": "sneak (動詞)", "col": "pair of sneakers", "ex": "He wore a pair of white sneakers."},
    "sneer": {"def": "冷笑、嘲笑、嘲弄", "ipa": "/snɪə/", "trans": "sneering", "col": "sneer at someone", "ex": "He sneered at my humble background."},
    "sneeze": {"def": "打噴嚏、噴嚏", "ipa": "/sniːz/", "trans": "sneezing", "col": "sneeze at", "ex": "The dust made her sneeze."},
    "sniff": {"def": "吸氣、嗅、聞", "ipa": "/snɪf/", "trans": "sniffed", "col": "sniff the air", "ex": "The dog sniffed the stranger's hand."},
    "snob": {"def": "勢利眼、假內行", "ipa": "/snɒb/", "trans": "snobbish, snobbery", "col": "intellectual snob", "ex": "He is such a snob about wine."},
    "snore": {"def": "打呼、鼾聲", "ipa": "/snɔː/", "trans": "snored, snoring", "col": "loud snore", "ex": "I couldn't sleep because he was snoring."},
    "snow": {"def": "雪、下雪", "ipa": "/snəʊ/", "trans": "snowy, snowstorm, snowflake", "col": "heavy snow, white as snow", "ex": "The ground was covered with snow."},
    "snowflake": {"def": "雪花", "ipa": "/ˈsnəʊfleɪk/", "trans": "snowflakes", "col": "ice snowflake", "ex": "No two snowflakes are exactly alike."},
    "snowy": {"def": "下雪的、被雪覆蓋的", "ipa": "/ˈsnəʊi/", "trans": "snow (名詞)", "col": "snowy mountains", "ex": "It was a cold, snowy day."},
    "snug": {"def": "舒適的、溫暖的", "ipa": "/snʌɡ/", "trans": "snugly", "col": "snug as a bug in a rug", "ex": "The children were snug in their beds."},
    "so": {"def": "如此地、那麼", "ipa": "/səʊ/", "trans": "無", "col": "so far, or so", "ex": "I am so happy to see you."},
    "soak": {"def": "浸泡、滲透、濕透", "ipa": "/səʊk/", "trans": "soaked", "col": "soak in water", "ex": "Soak the beans overnight."},
    "soaked": {"def": "濕透的、浸透的", "ipa": "/səʊkt/", "trans": "soak (動詞)", "col": "soaked to the skin", "ex": "His clothes were soaked with rain."},
}

with open("batch_l1_p69.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART69, f, ensure_ascii=False, indent=2)
