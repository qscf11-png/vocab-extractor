import json

# Level 1 Part 77: (Sport - Spy)
L1_PART77 = {
    "sport": {"def": "運動、體育、遊戲", "ipa": "/spɔːt/", "trans": "sporting, sporty, sportsman", "col": "sports center, team sport", "ex": "Do you play any sport?"},
    "sporting": {"def": "運動的、體育的", "ipa": "/ˈspɔːtɪŋ/", "trans": "sport (名詞)", "col": "sporting event", "ex": "It was a great sporting occasion."},
    "sportsman": {"def": "運動員、有精神的人", "ipa": "/ˈspɔːtsmən/", "trans": "sportswoman", "col": "good sportsman", "ex": "He is a keen sportsman."},
    "sportswear": {"def": "運動服裝", "ipa": "/ˈspɔːtsweə/", "trans": "sport (名詞)", "col": "casual sportswear", "ex": "The shop sells quality sportswear."},
    "sporty": {"def": "像運動員的、時髦的", "ipa": "/ˈspɔːti/", "trans": "sport (名詞)", "col": "sporty car", "ex": "She looks very sporty in that outfit."},
    "spot": {"def": "點、斑點、地點", "ipa": "/spɒt/", "trans": "spotted, spotless", "col": "on the spot, blind spot", "ex": "He showed me the exact spot where he fell."},
    "spotlight": {"def": "聚光燈、焦點", "ipa": "/ˈspɒtlaɪt/", "trans": "spotlights", "col": "in the spotlight", "ex": "The scandal put him in the spotlight."},
    "spotless": {"def": "極乾淨的、無瑕疵的", "ipa": "/ˈspɒtləs/", "trans": "spotlessly", "col": "spotless record", "ex": "The kitchen was spotless."},
    "spotted": {"def": "有斑點的、認出的", "ipa": "/ˈspɒtɪd/", "trans": "spot (名詞)", "col": "spotted tie", "ex": "She wore a spotted dress."},
    "spouse": {"def": "配偶、夫或妻", "ipa": "/spaʊz/", "trans": "spousal", "col": "dependent spouse", "ex": "Fill in your spouse's name here."},
    "sprain": {"def": "扭傷、扭", "ipa": "/spreɪn/", "trans": "sprained", "col": "sprained ankle", "ex": "I've sprained my wrist."},
    "spray": {"def": "噴霧、浪花、噴灑", "ipa": "/spreɪ/", "trans": "sprayer", "col": "hair spray, insect spray", "ex": "Water was spraying everywhere."},
    "spread": {"def": "傳播、蔓延、攤開", "ipa": "/spred/", "trans": "spreading", "col": "spread the news, spread butter", "ex": "The fire spread quickly."},
    "spring": {"def": "春天、泉水、彈簧", "ipa": "/sprɪŋ/", "trans": "sprang, sprung, springtime", "col": "hot spring, spring break", "ex": "Flowers bloom in spring."},
    "sprinkle": {"def": "噴灑、灑、淋", "ipa": "/ˈsprɪŋkl/", "trans": "sprinkled, sprinkler", "col": "sprinkle with salt", "ex": "Sprinkle the cake with sugar."},
    "sprint": {"def": "全速奔跑、衝刺", "ipa": "/sprɪnt/", "trans": "sprinter", "col": "final sprint", "ex": "He won the race with a brilliant sprint."},
    "sprout": {"def": "抽芽、長出、萌芽", "ipa": "/spraʊt/", "trans": "sprouted", "col": "bean sprout", "ex": "The seeds have started to sprout."},
    "spruce": {"def": "雲杉、整潔的", "ipa": "/spruːs/", "trans": "spruced", "col": "spruce up", "ex": "They spruced themselves up for the party."},
    "spurious": {"def": "偽造的、假造的", "ipa": "/ˈspjʊəriəs/", "trans": "spuriously", "col": "spurious claims", "ex": "They made spurious arguments."},
    "spy": {"def": "間諜、暗中監視", "ipa": "/spaɪ/", "trans": "spies, spying", "col": "industrial spy, spy on someone", "ex": "He was accused of being a Soviet spy."},
}

with open("batch_l1_p77.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART77, f, ensure_ascii=False, indent=2)
