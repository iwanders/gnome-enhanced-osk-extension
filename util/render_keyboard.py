#!/usr/bin/env python3


import sys
import json

def load(p):
    with open(p) as f:
        return json.load(f)

def ascii_level(level):
    data = ""
    def format_key(k):
        w = k.get("width", 1) * 7
        l = ""
        if "label" in k:
            l = k["label"][0:3]
        if "strings" in k:
            l = k["strings"][0][0:3]
        if "iconName" in k:
            l = k["iconName"].replace("go-", "").replace("-symbolic", "")[0:3]
        return f"{l: ^{w}}"
    for r in level["rows"]:
        keys = [format_key(k) for k in r]
        row = "|".join(keys)
        data += row + "\n"
    return data
    

if __name__ == "__main__":
    d = load(sys.argv[1])
    for l in d["levels"]:
        print("Level: ", l["level"], " mode: ", l["mode"])
        v = ascii_level(l)
        print(v)
        print()