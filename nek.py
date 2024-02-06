import json

res = {
    "include": [
        {"project": "foo", "config": "Debug"},
        {"project": "bar", "config": "Release"},
    ]
}
print(json.dumps(res))
