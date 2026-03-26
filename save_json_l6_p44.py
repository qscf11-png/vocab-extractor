import json

# Level 6 Part 44: (Bourgeois - Boxer)
L6_PART44 = {
    "bourgeois": {"def": "中產階級的、世俗的、資產階級、中產階級的人、世俗地 (中產)", "ipa": "/ˈbʊəʒwɑː/", "trans": "middle-class", "col": "bourgeois values", "ex": "He has very bourgeois values and tastes.", "pos": "adj./n./adv."},
    "bourgeoisie": {"def": "中產階級、資產階級 (總稱)", "ipa": "/ˌbʊəʒwɑːˈziː/", "trans": "bourgeois", "col": "petty bourgeoisie (小資產階級)", "ex": "The French Revolution was a struggle against the bourgeoisie.", "pos": "n."},
    "bout": {"def": "一場(交鋒/疾病)、一陣、發作、在一場內人物、在一場內地 (場)", "ipa": "/baʊt/", "trans": "bouts", "col": "bout of flu, drinking bout, wrestling bout", "ex": "He suffered another bout of severe coughing.", "pos": "n./adv."},
    "boutique": {"def": "精品店、流行女裝店 (單數)", "ipa": "/buːˈtiːk/", "trans": "boutiques (複數)", "col": "exclusive boutique", "ex": "She bought the dress at an exclusive boutique in Milan.", "pos": "n."},
    "bovine": {"def": "牛的、牛科的、遲鈍的人、牛般地 (牛)", "ipa": "/ˈbəʊvaɪn/", "trans": "ox-like", "col": "bovine leukemia", "ex": "He gave a slow, bovine response to the question.", "pos": "adj./n./adv."},
    "bow": {"def": "弓、蝴蝶結、船頭、鞠躬、彎曲、鞠躬的人、彎曲地 (弓/鞠躬)", "ipa": "/baʊ/ (鞠躬/船頭) /bəʊ/ (弓/蝴蝶結)", "trans": "bows, bowing", "col": "bow and arrow, take a bow, bow ties, bow to pressure", "ex": "They made a polite bow to the queen.", "pos": "n./v./adv."},
    "bowed": {"def": "彎曲的、鞠躬的、持弓的的人 (或物) (彎)", "ipa": "/baʊd/", "trans": "bow (動詞/名詞/副詞)", "col": "bowed legs", "ex": "He stood there with a bowed head.", "pos": "adj./adv."},
    "bowel": {"def": "腸、內部、同情地 (腸)", "ipa": "/ˈbaʊəl/", "trans": "bowels", "col": "bowel movement, in the bowels of (在深處)", "ex": "He has a problem with his bowels.", "pos": "n./adv."},
    "bower": {"def": "涼亭、樹蔭、閨房、居住在涼亭的人 (或物)、涼亭地 (亭)", "ipa": "/ˈbaʊə/", "trans": "bowers", "col": "garden bower", "ex": "They sat in the garden bower to enjoy the shade.", "pos": "n./v./adv."},
    "bowl": {"def": "碗、碗狀物、木球、滾球、打保齡球、碗狀的人、碗狀地 (碗)", "ipa": "/bəʊl/", "trans": "bowls, bowling", "col": "mixing bowl, toilet bowl, sugar bowl, bowl over (大吃一驚)", "ex": "She filled the bowl with soup.", "pos": "n./v./adv."},
    "bowled": {"def": "(bowl的過去式及過去分詞)、(俚)大吃一驚的", "ipa": "/bəʊld/", "trans": "astonished", "col": "bowled over", "ex": "I was bowled over by her beauty.", "pos": "v./adj."},
    "bowler": {"def": "投球手、(英)圓頂硬禮帽 (單數)", "ipa": "/ˈbəʊlə/", "trans": "bowlers (複數)", "col": "cricket bowler, bowler hat", "ex": "He wore a traditional black bowler hat.", "pos": "n."},
    "bowling": {"def": "保齡球運動、投球、保齡球地 (保)", "ipa": "/ˈbəʊlɪŋ/", "trans": "bowl (名詞/動詞/副詞)", "col": "bowling alley, bowling green", "ex": "Let's go bowling this evening.", "pos": "n./adv."},
    "bowman": {"def": "弓箭手、(船)前槳手", "ipa": "/ˈbəʊmən/", "trans": "archers", "col": "skilled bowman", "ex": "The skilled bowman hit the target from a distance.", "pos": "n."},
    "bowstring": {"def": "弓弦 (單數)", "ipa": "/ˈbəʊstrɪŋ/", "trans": "bowstrings (複數)", "col": "taut bowstring", "ex": "He pulled the taut bowstring and let the arrow fly.", "pos": "n."},
    "bow-tie/bow tie": {"def": "蝴蝶結領結", "ipa": "/ˌbəʊ ˈtaɪ/", "trans": "ties", "col": "wear a bow tie", "ex": "He wore a black bow tie with his tuxedo.", "pos": "n."},
    "box": {"def": "箱、盒、亭、拳擊、裝箱、困住、盒子的人、裝盒地 (盒)", "ipa": "/bɒks/", "trans": "boxing, boxed", "col": "lunch box, telephone box, out of the box (與眾不同), box office (售票處)", "ex": "The cat is hiding in the cardboard box.", "pos": "n./v./adv."},
    "boxed": {"def": "裝箱的、(俚)受困的", "ipa": "/bɒkst/", "trans": "box (名詞/動詞/副詞)", "col": "boxed lunch", "ex": "I have a boxed set of these movies.", "pos": "adj."},
    "boxer": {"def": "拳擊手、拳師狗、裝箱機 (單數)", "ipa": "/ˈbɒksə/", "trans": "boxers (複數)", "col": "heavyweight boxer, boxer shorts", "ex": "The heavyweight boxer won the match by knockout.", "pos": "n."},
}