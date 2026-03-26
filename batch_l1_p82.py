import json

# Level 1 Part 82: (Stipulate - Storey)
L1_PART82 = {
    "stipulate": {"def": "規定、約定", "ipa": "/ˈstɪpjuleɪt/", "trans": "stipulation", "col": "stipulate that...", "ex": "The contract stipulates that the work must be finished by June."},
    "stir": {"def": "攪動、激動", "ipa": "/stɜː/", "trans": "stirring", "col": "stir the soup, stir up trouble", "ex": "Stir the sauce until it is smooth."},
    "stitch": {"def": "縫、縫合", "ipa": "/stɪtʃ/", "trans": "stitching", "col": "a stitch in time saves nine", "ex": "I need to put a few stitches in this shirt."},
    "stock": {"def": "庫存、股票", "ipa": "/stɒk/", "trans": "stocking, stockist, stockbroker", "col": "in stock, stock market", "ex": "The shop has a large stock of books."},
    "stockbroker": {"def": "股票經紀人", "ipa": "/ˈstɒkbrəʊkə/", "trans": "stock (名詞)", "col": "work as a stockbroker", "ex": "He made a fortune as a stockbroker."},
    "stomach": {"def": "胃、肚子", "ipa": "/ˈstʌmək/", "trans": "stomach-ache", "col": "empty stomach, stomach upset", "ex": "I have a pain in my stomach."},
    "stone": {"def": "石頭、果核", "ipa": "/stəʊn/", "trans": "stony", "col": "precious stone, stone cold", "ex": "He threw a stone into the river."},
    "stoop": {"def": "彎腰、屈服", "ipa": "/stuːp/", "trans": "stooped", "col": "stoop down", "ex": "He had to stoop to get through the door."},
    "stop": {"def": "停止、阻礙", "ipa": "/stɒp/", "trans": "stopped, stoppage, stopper", "col": "bus stop, stop by", "ex": "Stop talking and listen."},
    "storage": {"def": "儲存、倉庫", "ipa": "/ˈstɔːrɪdʒ/", "trans": "store (動詞)", "col": "cold storage, data storage", "ex": "We put our furniture into storage."},
    "store": {"def": "商店、儲備", "ipa": "/stɔː/", "trans": "storage, storehouse, storeroom", "col": "department store, in store", "ex": "Where do you store your winter clothes?"},
    "storey": {"def": "樓層", "ipa": "/ˈstɔːri/", "trans": "story", "col": "single-storey building", "ex": "The building has ten storeys."},
}

with open("batch_l1_p82.json", "w", encoding="utf-8") as f:
    json.dump(L1_PART82, f, ensure_ascii=False, indent=2)
