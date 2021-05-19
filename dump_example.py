db = {
    "base1": {
            "numbers": {
                "type": "int",
                "data":
                        [5, 3, 2]

            },
            "words": {
                "type": "str",
                "data": [
                        "dsadsa",
                        "dsadsasda",
                        "dfdasfdas"
                        ]
            }
    },
    "base2": {
            "numbers": {
                "type": "float",
                "data": [
                        5.0,
                        3.2,
                        2.1
                        ]
                },
            "slowa": {
                "type": "str",
                "data":
                        ["dsadsa",
                        "dsadsasda",
                        "dfdasfdas"]

                }
    }
}

import json

with open("./source/base.json", "w") as json_file:
    json.dump(db, json_file)
