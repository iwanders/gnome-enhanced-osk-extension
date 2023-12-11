#!/usr/bin/env python3


import sys
import json

def load(p):
    with open(p) as f:
        return json.load(f)

def ascii_level(level):
    data = ""
    def format_key(k):
        # Fudge these values such that we can make the grid look good.
        w = {
            1: 4,
            1.5: 6,
            2: 8 + 1,
            2.5: 12,
            3: 14,
            4: 19,
        }[k.get("width", 1)]

        l = ""
        if "label" in k:
            l = k["label"][0:w]
        if "strings" in k:
            l = k["strings"][0][0:w]
        if "iconName" in k:
            l = k["iconName"].replace("go-", "").replace("-symbolic", "").replace("keyboard-", "").replace("edit-", "")[0:w]
        w = w - emoji_correction(l)
        return f"{l: ^{w}}"

    def row_length(r):
        v = sum(k.get("width", 1) for k in r)
        if abs(v - int(v)) < 0.001:
            return int(v)
        return v

    def emoji_correction(l):
        # Totally non robust lol
        w = 0
        if "🎉" in l:
            w += 1
        if "😀" in l:
            w += 1
        return w
        
    def str_len_accounting_for_emoji(s):
        w = len(s)
        w += emoji_correction(s)
        return w
        

    for r in level["rows"]:
        keys = [format_key(k) for k in r]
        row = "|".join(keys) + "|"
        width = row_length(r)
        align = 70 - str_len_accounting_for_emoji(row)
        data += f"{row}  {width: >{align}}"+ "\n"
    return data
    

if __name__ == "__main__":
    d = load(sys.argv[1])
    for l in d["levels"]:
        print()
        print("Level: ", l["level"], " mode: ", l["mode"])
        v = ascii_level(l)
        print(v)
        print()