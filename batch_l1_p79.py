import json

# Level 1 Part 79: (Stagnant - Station)
L1_PART79 = {
    "stagnant": {"def": "停滯的、不發展的", "ipa": "/ˈstæɡnənt/", "trans": "stagnate, stagnation", "col": "stagnant water, stagnant economy", "ex": "The economy has remained stagnant for several years."},
    "stain": {"def": "染色、污漬", "ipa": "/steɪn/", "trans": "stainless, stained", "col": "coffee stain, blood stain", "ex": "The ink left a permanent stain on the carpet."},
    "stainless": {"def": "不鏽的、無暇的", "ipa": "/ˈsteɪnləs/", "trans": "stain (名詞)", "col": "stainless steel", "ex": "We bought a set of stainless steel cutlery."},
    "stair": {"def": "樓梯、階梯", "ipa": "/steə/", "trans": "staircase", "col": "upstairs, bottom stair", "ex": "He ran up the stairs."},
    "stamp": {"def": "郵票、印章、標誌", "ipa": "/stæmp/", "trans": "stamped, stampede", "col": "postage stamp, rubber stamp", "ex": "Don't forget to put a stamp on the envelope."},
    "stand": {"def": "站立、忍受、攤位", "ipa": "/stænd/", "trans": "stood, standing, standard", "col": "stand up, stand by", "ex": "I can't stand the heat."},
    "standard": {"def": "標準、規格、旗幟", "ipa": "/ˈstændəd/", "trans": "standardize", "col": "standard of living, double standard", "ex": "The hotel is of a very high standard."},
    "star": {"def": "星星、明星、星形物", "ipa": "/stɑː/", "trans": "starry, stardom", "col": "shooting star, guest star", "ex": "The sky was full of stars."},
    "stare": {"def": "凝視、注視", "ipa": "/steə/", "trans": "staring", "col": "stare at", "ex": "Don't stare at people, it's rude."},
    "start": {"def": "開始、出發、驚跳", "ipa": "/stɑːt/", "trans": "started, starter, startle", "col": "start a fire, for a start", "ex": "What time does the movie start?"},
    "startle": {"def": "驚嚇、大吃一驚", "ipa": "/ˈstɑːtl/", "trans": "startling", "col": "startle someone", "ex": "The noise startled the horse."},
    "starve": {"def": "挨餓、飢餓、使餓死", "ipa": "/stɑːv/", "trans": "starvation", "col": "starve to death", "ex": "The animals were left to starve."},
    "state": {"def": "國家、州、狀態", "ipa": "/steɪt/", "trans": "stated, statement, statesman", "col": "united states, emotional state", "ex": "The president will make a statement later."},
    "statement": {"def": "陳述、聲明、報表", "ipa": "/ˈsteɪtmənt/", "trans": "state (動詞)", "col": "bank statement, financial statement", "ex": "The government issued a statement about the new policy."},
    "station": {"def": "車站、站、局", "ipa": "/ˈsteɪʃn/", "trans": "stationary", "col": "police station, railway station", "ex": "I'll meet you at the station."},
}

with open("batch_l1_p79.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART79, f, ensure_ascii=False, indent=2)
