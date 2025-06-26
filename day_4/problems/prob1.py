d = {"me" : 200 , "you" : 400}
print(d["you"])
d["someone"] = 20
print(d)
d["someone"] = 200
print(d)
print(len(d))
print("SOMEONE" in d)
print(d.keys())
for key in d:
    d[key] += 100
print(d)
print(dir(dict))
help(dict.update)
d.update({"me" : 250, "us" : 500})
print(d)
