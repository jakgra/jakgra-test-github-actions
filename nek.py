import json

res = {
    "include":
    [
        {
            "project": "foo",
            "config": "Debug"
        },
        {
            "project":"bar",
            "config": "Release"
        }
    ]
}
print("matrix=" + json.dumps(res))
