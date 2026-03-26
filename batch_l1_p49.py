import json

# Level 1 Part 49: (Puncture - Purity)
L1_PART49 = {
    "puncture": {"def": "刺穿、戳破、穴、刺痕、刺破", "ipa": "/ˈpʌŋktʃə/", "trans": "punctured", "col": "tire puncture, puncture wound", "ex": "I had a puncture on my way here."},
    "pungent": {"def": "刺激性的、辛辣的、尖刻的", "ipa": "/ˈpʌndʒənt/", "trans": "pungency", "col": "pungent smell, pungent remark", "ex": "The air was filled with a pungent smell of onions."},
    "punish": {"def": "懲罰、處罰、折磨", "ipa": "/ˈpʌnɪʃ/", "trans": "punished, punishment, punishable", "col": "punish for a crime", "ex": "He was punished for his mistake."},
    "punishable": {"def": "可罰的、該罰的", "ipa": "/ˈpʌnɪʃəbl/", "trans": "punish (動詞)", "col": "punishable by law", "ex": "Littering is punishable by a fine."},
    "punishment": {"def": "懲罰、處罰、刑罰", "ipa": "/ˈpʌnɪʃmənt/", "trans": "punish (動詞)", "col": "capital punishment, corporal punishment", "ex": "He deserved the punishment."},
    "punitive": {"def": "懲罰性的、刑罰的", "ipa": "/ˈpjuːnətɪv/", "trans": "punish (動詞)", "col": "punitive measures, punitive damages", "ex": "The government took punitive action."},
    "punster": {"def": "愛說雙關語的人", "ipa": "/ˈpʌnstə/", "trans": "pun (名詞)", "col": "inveterate punster", "ex": "He is a notorious punster."},
    "punt": {"def": "平底小船、踢高球、撐船、賭博", "ipa": "/pʌnt/", "trans": "punted", "col": "punt on the river", "ex": "We went for a punt along the river."},
    "puny": {"def": "微小的、弱小的、微不足道的", "ipa": "/ˈpjuːni/", "trans": "puniness", "col": "puny attempt", "ex": "He is just a puny little man."},
    "pupil": {"def": "學生、小學生、瞳孔", "ipa": "/ˈpjuːpl/", "trans": "pupils", "col": "primary school pupil, dilated pupils", "ex": "The school has over 500 pupils."},
    "puppet": {"def": "木偶、傀儡、受人操縱的人", "ipa": "/ˈpʌpɪt/", "trans": "puppetry, puppeteer", "col": "puppet show, puppet government", "ex": "He is just a puppet in their hands."},
    "puppeteer": {"def": "操縱木偶的人", "ipa": "/ˌpʌpɪˈtɪə/", "trans": "puppet (名詞)", "col": "master puppeteer", "ex": "The puppeteer skillfully moved the marionette."},
    "puppy": {"def": "小狗、幼犬", "ipa": "/ˈpʌpi/", "trans": "puppies", "col": "puppy love", "ex": "She got a cute puppy for Christmas."},
    "purchase": {"def": "購買、採購、購買物、支點、購買", "ipa": "/ˈpɜːtʃəs/", "trans": "purchased, purchaser", "col": "make a purchase, purchase price", "ex": "I'd like to purchase this book."},
    "purchaser": {"def": "購買者、採購者", "ipa": "/ˈpɜːtʃəsə/", "trans": "purchase (名詞/動詞)", "col": "potential purchaser", "ex": "The purchaser must sign the contract."},
    "pure": {"def": "純淨的、純潔的、純粹的", "ipa": "/pjʊə/", "trans": "purely, purity, purify", "col": "pure water, pure gold", "ex": "This is pure silk."},
    "purely": {"def": "純粹地、完全地、潔淨地", "ipa": "/ˈpjʊəli/", "trans": "pure (形容詞)", "col": "purely accidental", "ex": "It was a purely business decision."},
    "purgatory": {"def": "煉獄、受苦的地方、淨化的", "ipa": "/ˈpɜːɡətri/", "trans": "purge (動詞)", "col": "soul in purgatory", "ex": "Waiting for the results was pure purgatory."},
    "purge": {"def": "淨化、清洗、通便、消除", "ipa": "/pɜːdʒ/", "trans": "purged", "col": "political purge", "ex": "The party purged its dissident members."},
    "purification": {"def": "淨化、提純、洗罪", "ipa": "/ˌpjʊərɪfɪˈkeɪʃn/", "trans": "purify (動詞)", "col": "water purification", "ex": "Purification of the soul is important."},
    "purify": {"def": "使純淨、淨化、滌罪", "ipa": "/ˈpjʊərɪfaɪ/", "trans": "purified, purification", "col": "purify air", "ex": "The machine purifies the water."},
    "purist": {"def": "純粹主義者、追求純正的人", "ipa": "/ˈpjʊərɪst/", "trans": "purism", "col": "language purist", "ex": "As a purist, he hates language blending."},
    "puritan": {"def": "清教徒、道德極其嚴謹的人、清教徒的", "ipa": "/ˈpjʊərɪtən/", "trans": "puritanical", "col": "puritan ethic", "ex": "He has a very puritan attitude toward life."},
    "purity": {"def": "純淨、純潔、純粹", "ipa": "/ˈpjʊərəti/", "trans": "pure (形容詞)", "col": "purity of heart", "ex": "The purity of the air is remarkable."},
}

with open("batch_l1_p49.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART49, f, ensure_ascii=False, indent=2)
