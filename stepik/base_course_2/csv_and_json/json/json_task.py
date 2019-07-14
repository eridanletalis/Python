import json

a = input()
dict_json = json.loads(a)
dict_result = {}


def add_parents(key_glob, key, d):
    d_copy = d.copy()
    for child in d_copy[key]:
        d[key_glob].add(child)
        add_parents(key_glob, child, d)


for obj in dict_json:
    for parent in obj["parents"]:
        if not dict_result.get(parent):
            dict_result[parent] = {obj["name"]}
        else:
            dict_result[parent].add(obj["name"])
        if not dict_result.get(obj["name"]):
            dict_result[obj["name"]] = set()
for i in dict_result:
    add_parents(i, i, dict_result)
for key in sorted(dict_result.keys()):
    print(key, ":", len(dict_result[key]) + 1)
print(dict_result)
