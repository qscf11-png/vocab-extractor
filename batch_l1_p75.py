import json

# Level 1 Part 75: (Spell - Spinal)
L1_PART75 = {
    "spell": {"def": "拼字、拼寫、咒語", "ipa": "/spel/", "trans": "spelling, speller, spellbound", "col": "cast a spell, dry spell", "ex": "How do you spell your name?"},
    "spelling": {"def": "拼字、拼寫、拼法", "ipa": "/ˈspelɪŋ/", "trans": "spell (動詞)", "col": "spelling bee, spelling mistake", "ex": "Is there a correct spelling for this word?"},
    "spend": {"def": "花費、浪費、度過", "ipa": "/spend/", "trans": "spent, spending, spender", "col": "spend money, spend time", "ex": "How much did you spend on that car?"},
    "spending": {"def": "開支、花費", "ipa": "/ˈspendɪŋ/", "trans": "spend (動詞)", "col": "public spending, consumer spending", "ex": "Government spending has increased."},
    "spent": {"def": "精疲力竭的、花掉的", "ipa": "/spent/", "trans": "spend (動詞)", "col": "spent force", "ex": "I am completely spent after the marathon."},
    "sphere": {"def": "球體、範圍、領域", "ipa": "/sfɪə/", "trans": "spherical", "col": "social sphere, public sphere", "ex": "That is outside my sphere of influence."},
    "spice": {"def": "香料、調味品、趣味", "ipa": "/spaɪs/", "trans": "spicy", "col": "variety is the spice of life", "ex": "Add some spice to the soup."},
    "spicy": {"def": "辛辣的、有香料味的", "ipa": "/ˈspaɪsi/", "trans": "spice (名詞)", "col": "spicy food", "ex": "I love spicy food."},
    "spider": {"def": "蜘蛛", "ipa": "/ˈspaɪdə/", "trans": "spiders", "col": "spider web", "ex": "A spider was crawling up the wall."},
    "spike": {"def": "長釘、釘鞋、尖峰", "ipa": "/spaɪk/", "trans": "spiked", "col": "spike in prices", "ex": "The price of oil showed a sudden spike."},
    "spill": {"def": "溢出、洩漏、摔下", "ipa": "/spɪl/", "trans": "spilled, spilt, spillage", "col": "spill the beans, oil spill", "ex": "I accidentally spilled my coffee."},
    "spin": {"def": "旋轉、紡紗、吐絲", "ipa": "/spɪn/", "trans": "spun, spinning, spinner", "col": "spin a web, head spin", "ex": "The earth spins on its axis."},
    "spinach": {"def": "菠菜", "ipa": "/ˈspɪnɪdʒ/", "trans": "spinaches", "col": "fresh spinach", "ex": "Spinach is rich in iron."},
    "spinal": {"def": "脊髓的、脊柱的", "ipa": "/ˈspaɪnl/", "trans": "spine", "col": "spinal cord, spinal injury", "ex": "He suffered a spinal injury in the accident."},
}

with open("batch_l1_p75.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART75, f, ensure_ascii=False, indent=2)
