import json

# Level 1 Part 71: (Soldier - Soon)
L1_PART71 = {
    "soldier": {"def": "士兵、軍人", "ipa": "/ˈəʊldʒə/", "trans": "soldiers, soldierly", "col": "unknown soldier, foot soldier", "ex": "He is a brave soldier."},
    "sole": {"def": "唯一的、單獨的、腳掌", "ipa": "/səʊl/", "trans": "solely", "col": "sole survivor, sole purpose", "ex": "He is the sole survivor of the crash."},
    "solely": {"def": "獨自地、僅僅", "ipa": "/ˈəʊlli/", "trans": "sole (形容詞)", "col": "solely responsible", "ex": "She is solely responsible for the project."},
    "solemn": {"def": "莊嚴的、嚴肅的、鄭重的", "ipa": "/ˈɒləm/", "trans": "solemnly, solemnity", "col": "solemn promise", "ex": "He gave a solemn promise."},
    "solid": {"def": "固體的、結實的、可靠的", "ipa": "/ˈɒlɪd/", "trans": "solidify, solidity, solidarity", "col": "solid evidence, solid foundation", "ex": "Ice is water in its solid state."},
    "solidarity": {"def": "團結、一致", "ipa": "/ˌɒlɪˈdærəti/", "trans": "solid (形容詞)", "col": "show solidarity", "ex": "They expressed solidarity with the strikers."},
    "solitary": {"def": "孤獨的、獨自的、隱士", "ipa": "/ˈɒlətri/", "trans": "solitude", "col": "solitary confinement, solitary life", "ex": "He leads a solitary life in the woods."},
    "solitude": {"def": "孤獨、隱居、寂寞", "ipa": "/ˈɒlətjuːd/", "trans": "solitary (形容詞)", "col": "peace and solitude", "ex": "She enjoyed the solitude of the mountains."},
    "solo": {"def": "獨奏、單獨的、單獨地", "ipa": "/ˈəʊləʊ/", "trans": "soloist", "col": "piano solo, fly solo", "ex": "He performed his first piano solo."},
    "solution": {"def": "解決方案、溶解、溶液", "ipa": "/səˈluːʃn/", "trans": "solve, soluble", "col": "perfect solution, chemical solution", "ex": "There is no easy solution to this problem."},
    "solve": {"def": "解決、解答、溶解", "ipa": "/sɒlv/", "trans": "solvable, solver, solution", "col": "solve a mystery, solve a riddle", "ex": "We must solve this problem immediately."},
    "some": {"def": "一些、某些、大約性", "ipa": "/sʌm/", "trans": "somebody, something", "col": "some day, for some time", "ex": "Would you like some coffee?"},
    "somebody": {"def": "某人、大人物", "ipa": "/ˈʌmbədi/", "trans": "someone", "col": "somebody else", "ex": "Somebody left their umbrella here."},
    "someday": {"def": "有朝一日", "ipa": "/ˈʌmdeɪ/", "trans": "sometime", "col": "someday soon", "ex": "I hope to visit Japan someday."},
    "somehow": {"def": "不知何故、以某種方式", "ipa": "/ˈʌmhaʊ/", "trans": "no", "col": "somehow or other", "ex": "We will get there somehow."},
    "someone": {"def": "某人", "ipa": "/ˈʌmwʌn/", "trans": "somebody", "col": "someone special", "ex": "Someone is knocking at the door."},
    "something": {"def": "某事、某物", "ipa": "/ˈʌmθɪŋ/", "trans": "sometime", "col": "something new, or something", "ex": "I have something to tell you."},
    "sometime": {"def": "在某個時候、以往的", "ipa": "/ˈʌmtaɪm/", "trans": "sometimes", "col": "sometime next week", "ex": "Let's have lunch sometime."},
    "sometimes": {"def": "有時、偶爾", "ipa": "/ˈʌmtaɪmz/", "trans": "sometime", "col": "sometimes... sometimes...", "ex": "Sometimes I go to the gym before work."},
    "somewhat": {"def": "稍微、有點", "ipa": "/ˈʌmwɒt/", "trans": "some (名詞)", "col": "somewhat surprised", "ex": "The results were somewhat disappointing."},
    "somewhere": {"def": "在某處、大約", "ipa": "/ˈʌmweə/", "trans": "anywhere", "col": "somewhere else", "ex": "I've seen him somewhere before."},
    "son": {"def": "兒子、孩子", "ipa": "/sʌn/", "trans": "sons", "col": "oldest son, like father like son", "ex": "He has two sons."},
    "song": {"def": "歌曲、歌聲", "ipa": "/sɒŋ/", "trans": "singer, songwriting", "col": "love song, theme song", "ex": "I love this song."},
    "soon": {"def": "不久、很快、早", "ipa": "/suːn/", "trans": "sooner, soonest", "col": "as soon as, see you soon", "ex": "The sun will set soon."},
}

with open("batch_l1_p71.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART71, f, ensure_ascii=False, indent=2)
