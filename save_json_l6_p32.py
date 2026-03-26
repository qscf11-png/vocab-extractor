import json

# Level 6 Part 32: (Bewail - Bibliophile)
L6_PART32 = {
    "bewail": {"def": "哀悼、為...慟哭、深表遺憾", "ipa": "/bɪˈweɪl/", "trans": "lament", "col": "bewail one's fate", "ex": "She bewailed the loss of her childhood friend.", "pos": "v."},
    "beware": {"def": "當心、提防", "ipa": "/bɪˈweə/", "trans": "watch out", "col": "beware of dog, beware of pickpockets", "ex": "Beware of the dog!", "pos": "v."},
    "bewilder": {"def": "使迷惑、使糊塗、使不知所措", "ipa": "/bɪˈwɪldə/", "trans": "bewildered, bewilderment", "col": "total bewilder", "ex": "The new rules only served to bewilder the students.", "pos": "v."},
    "bewildered": {"def": "困惑的、不知所措的", "ipa": "/bɪˈwɪldəd/", "trans": "bewilder (動詞), bewilderment", "col": "look bewildered", "ex": "The bewildered child cried for his mother.", "pos": "adj."},
    "bewildering": {"def": "令人困惑的、令人不知所措的", "ipa": "/bɪˈwɪldərɪŋ/", "trans": "bewilder (動詞), bewilderment", "col": "bewildering variety", "ex": "The shop has a bewildering variety of cheese.", "pos": "adj."},
    "bewilderment": {"def": "困惑、不知所措、迷亂", "ipa": "/bɪˈwɪldəmənt/", "trans": "bewilder (動詞), bewildered", "col": "look of bewilderment", "ex": "There was a look of bewilderment on her face.", "pos": "n."},
    "bewitch": {"def": "使著迷、施魔法於", "ipa": "/bɪˈwɪtʃ/", "trans": "bewitching", "col": "bewitch by", "ex": "She was bewitched by his charm.", "pos": "v."},
    "bewitched": {"def": "著迷的、受魔法控制的", "ipa": "/bɪˈwɪtʃt/", "trans": "bewitch (動詞), bewitching", "col": "bewitched by beauty", "ex": "The prince was bewitched by her beauty.", "pos": "adj."},
    "bewitching": {"def": "迷人的、著迷的", "ipa": "/bɪˈwɪtʃɪŋ/", "trans": "bewitch (動詞), bewitched", "col": "bewitching smile", "ex": "She has a bewitching smile.", "pos": "adj."},
    "beyond": {"def": "在...那一邊、遠於、越出、超出、在遠處地 (外)", "ipa": "/bɪˈjɒnd/", "trans": "further", "col": "beyond belief, beyond repair, beyond comparison", "ex": "The house is beyond the lake.", "pos": "prep./adv./adj./n."},
    "bezant": {"def": "(古)拜占庭金幣 (單數)", "ipa": "/ˈbezənt/", "trans": "bezants (複數)", "col": "golden bezant", "ex": "The golden bezant was used in the Middle Ages.", "pos": "n."},
    "bezel": {"def": "斜邊、溝槽、(鐘/錶)玻璃圈的人 (或物) (圈)", "ipa": "/ˈbezl/", "trans": "bezels", "col": "rotating bezel", "ex": "The watch has a rotating bezel.", "pos": "n./adv."},
    "bi-": {"def": "(字根)二、雙、兩次", "ipa": "/baɪ/", "trans": "two", "col": "bicycle, bilingual, biannual", "ex": "'Bilingual' means speaking two languages.", "pos": "pref."},
    "biannual": {"def": "一年兩次的、半年一次的、半年地 (半年)", "ipa": "/baɪˈænjuəl/", "trans": "twice a year", "col": "biannual report", "ex": "The company publishes a biannual report.", "pos": "adj./adv."},
    "biannually": {"def": "一年兩次地、半年一次地", "ipa": "/baɪˈænjuəli/", "trans": "biannual (形容詞/副詞)", "col": "published biannually", "ex": "The magazine is published biannually.", "pos": "adv."},
    "bias": {"def": "偏見、偏袒、斜紋、使有偏見、偏斜的、偏心地 (偏)", "ipa": "/ˈbaɪəs/", "trans": "biases", "col": "political bias, cultural bias, without bias", "ex": "The report was criticized for its political bias.", "pos": "n./v./adj./adv."},
    "biased": {"def": "有偏見的、結果偏向一方的", "ipa": "/ˈbaɪəst/", "trans": "bias (名詞/動詞/形容詞/副詞)", "col": "heavily biased", "ex": "His report was heavily biased towards his own view.", "pos": "adj."},
    "bib": {"def": "圍兜、圍裙、飲、啜、圍兜的人 (或物) (兜)", "ipa": "/bɪb/", "trans": "bibs", "col": "baby bib", "ex": "The baby was wearing a colorful bib.", "pos": "n./v./adv."},
    "Bible": {"def": "聖經、權威書籍 (單數)", "ipa": "/ˈbaɪbl/", "trans": "Bibles (複數)", "col": "Holy Bible, the fisherman's Bible", "ex": "The Holy Bible is a sacred text.", "pos": "n."},
    "biblical": {"def": "聖經的、根據聖經的、聖經般地 (聖經)", "ipa": "/ˈbɪblɪkl/", "trans": "Bible (名詞)", "col": "biblical proportions", "ex": "The flood was of biblical proportions.", "pos": "adj./adv."},
    "bibliography": {"def": "參考書目、文獻學", "ipa": "/ˌbɪbliˈɒɡrəfi/", "trans": "bibliographies", "col": "annotated bibliography", "ex": "The book includes an extensive bibliography.", "pos": "n."},
    "bibliophile": {"def": "藏書家、愛書人", "ipa": "/ˈbɪbliəʊfaɪl/", "trans": "book lover", "col": "passionate bibliophile", "ex": "He is a passionate bibliophile with a vast collection.", "pos": "n."},
}