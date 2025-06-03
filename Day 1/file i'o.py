with open("hey.txt","r") as f:
     f.read()
     f.close()
     print(f)




import json
emplist={
  "name": "Zamin",
  "age": 17,
  "skills": ["Python", "AI"]
}

try:
     with open("hy.json","w") as fh:
      json.dump(emplist,fh)
      print(fh)
except FileExistsError:
#     print("That file already exists")


import json
emplist={
  "name": "Zamin",
  "age": 17,
  "skills": ["Python", "AI"]
}
with open("hhj.json","w") as fl:
    json.dump(emplist,fl,indent=6)
    print(fl)













