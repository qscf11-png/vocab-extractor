import json

# Level 6 Part 45: (Boxing - Brag)
L6_PART45 = {
    "boxing": {"def": "拳擊運動、裝箱、拳擊的人 (或物) (拳)", "ipa": "/ˈbɒksɪŋ/", "trans": "box (動詞/名詞/副詞)", "col": "Boxing Day (節禮日), boxing match, boxing gloves", "ex": "He likes watching professional boxing.", "pos": "n./adv."},
    "boxwood": {"def": "黃楊木", "ipa": "/ˈbɒkswʊd/", "trans": "wood", "col": "carved boxwood", "ex": "The frame was made of finely carved boxwood.", "pos": "n."},
    "boy": {"def": "男孩、兒子、男僕、(口)傢伙、呼喚、(美口)好傢伙、男性地 (男)", "ipa": "/bɔɪ/", "trans": "boys, boyhood", "col": "blue-eyed boy (紅人), boy scout (童軍), oh boy!", "ex": "The boy is playing with his toys.", "pos": "n./int./adv."},
    "boycott": {"def": "抵制、拒絕參加、抵制的人 (或物)、抵制地 (抵制)", "ipa": "/ˈbɔɪkɒt/", "trans": "boycotts", "col": "trade boycott, calling a boycott", "ex": "They are calling for a boycott of the company's products.", "pos": "v./n./adv."},
    "boyhood": {"def": "少年時代、男孩們 (單數)", "ipa": "/ˈbɔɪhʊd/", "trans": "childhood", "col": "since boyhood", "ex": "They have been friends since early boyhood.", "pos": "n."},
    "boyish": {"def": "男孩般的、幼稚的、純真地", "ipa": "/ˈbɔɪɪʃ/", "trans": "youthful", "col": "boyish smile", "ex": "He still has a boyish smile even though he's in his fifties.", "pos": "adj./adv."},
    "boyishly": {"def": "男孩般地、幼稚地、純真地", "ipa": "/ˈbɔɪɪʃli/", "trans": "boyish (形容詞)", "col": "laughed boyishly", "ex": "He laughed boyishly at the joke.", "pos": "adv."},
    "boyishness": {"def": "天真、孩子氣、少年氣", "ipa": "/ˈbɔɪɪʃnəs/", "trans": "boyish (形容詞/副詞)", "col": "eternal boyishness", "ex": "He has retained an eternal boyishness.", "pos": "n."},
    "boysenberry": {"def": "博森莓 (單數)", "ipa": "/ˈbɔɪzəberi/", "trans": "boysenberries (複數)", "col": "ripe boysenberry", "ex": "He added some ripe boysenberries to the pie.", "pos": "n."},
    "bra": {"def": "胸罩 (單數)", "ipa": "/brɑː/", "trans": "bras (複數)", "col": "lace bra", "ex": "She bought a new lace bra.", "pos": "n."},
    "brace": {"def": "支柱、護具、支撐、大括號、一雙、使防備、支撐地 (撐)", "ipa": "/breɪs/", "trans": "bracing, braces", "col": "back brace, knee brace, brace oneself for, in braces (戴牙套)", "ex": "The workers used beams to brace the old wall.", "pos": "n./v./adv."},
    "bracelet": {"def": "手鐲、手鍊 (單數)", "ipa": "/ˈbreɪslət/", "trans": "bracelets (複數)", "col": "gold bracelet", "ex": "She wore a simple gold bracelet on her wrist.", "pos": "n."},
    "bracer": {"def": "支撐物、(舊)護腕、強心劑", "ipa": "/ˈbreɪsə/", "trans": "brace (動詞/名詞/副詞)", "col": "stiff bracer", "ex": "He took a stiff bracer before the interview.", "pos": "n."},
    "braces": {"def": "(衣)吊帶、(齒)牙套、(數)大括號 (複數)", "ipa": "/ˈbreɪsɪz/", "trans": "brace", "col": "wear braces", "ex": "The child has to wear braces on his teeth.", "pos": "n."},
    "bracing": {"def": "令人振奮的、涼爽的、支撐物的人 (或物) (撐)", "ipa": "/ˈbreɪsɪŋ/", "trans": "brace (動詞/名詞/副詞)", "col": "bracing sea air", "ex": "The bracing sea air was very refreshing.", "pos": "adj./n./adv."},
    "bracken": {"def": "蕨、蕨類植物叢 (單數)", "ipa": "/ˈbrækən/", "trans": "ferns", "col": "thick bracken", "ex": "The hillside was covered with thick green bracken.", "pos": "n."},
    "bracket": {"def": "括號、托架、等級、把...歸類、括號的人、括號地 (號)", "ipa": "/ˈbrækɪt/", "trans": "brackets", "col": "tax bracket, square brackets, income bracket, shelf bracket", "ex": "The values are shown in square brackets.", "pos": "n./v./adv."},
    "brackish": {"def": "微鹹的、難喝的、不悅的", "ipa": "/ˈbrækɪʃ/", "trans": "salty", "col": "brackish water", "ex": "The lagoon was filled with brackish water.", "pos": "adj."},
    "brad": {"def": "無頭釘、細長釘、(釘)釘地 (釘)", "ipa": "/bræd/", "trans": "nail", "col": "steel brad", "ex": "He used a steel brad to fix the molding.", "pos": "n./adv."},
    "brag": {"def": "吹牛、自誇、引以為榮、自誇的人 (或物)、誇大的人物、誇大地 (吹)", "ipa": "/bræɡ/", "trans": "bragging, braggart", "col": "nothing to brag about (沒什麼好自誇的)", "ex": "I don't mean to brag, but I'm a very good cook.", "pos": "v./n./adv."},
}