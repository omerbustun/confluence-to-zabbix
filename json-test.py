import json

with open("output.json", "r", encoding='utf-8-sig') as file_a:
    a = json.load(file_a)

with open("output2.json", "r", encoding='utf-8-sig') as file_b:
    b = json.load(file_b)

def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

print(ordered(a) == ordered(b))
print(a == b)