import json

res = [
    {
        "test": "something",
        "out": "neki"
    },
    {
        "test": "something 2",
        "out": "neki 2"
    },
]
print(json.dumps(res))
