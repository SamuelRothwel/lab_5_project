rep = {
  "AutoIncidentMain": "IM",
  "AutoIncidentSimilarityExclusion": "ISE",
  "AutoIncidentSimilarityTfIdf": "ISV",
  "WHERE": '" +\n$"WHERE', 
  "IS ": '" +\n$"IS ', 
  "AND": '" +\n$"AND',
  "FROM": '" +\n$"FROM',
  "LEFT": '" +\n$"LEFT',
  "RIGHT": '" +\n$"RIGHT',
  "INNER": '" +\n$"INNER',
  "ON": '" +\n$"ON',
  "BETWEEN": '" +\n$"BETWEEN',
}

out = ""
with open("in.txt", "r") as f:
  inp = f.readlines()
  x = ""
  for i in range(len(inp)):
    x += inp[i]
  spl1 = x.split('",')
  vars = spl1[len(spl1) - 1]
  vars = vars.replace(");", "").split(",")
  out = spl1[0]
  for i in range(len(vars)):
    repNum = "{" + str(i) + "}"
    print(repNum)
    repVar =  "{" + vars[i].replace("\n", "").replace(" ", "") + "}"
    out = out.replace(repNum, repVar)
  out += '"'
  print(out)
out = out.split('"')
out2 = '$"'
for i in range(len(out)):
  if (i == 0):
    continue
  if "+" in out[i]:
    continue
  out2 += out[i].replace("\n", '" +\n$"')
out2 += '";'

for i in rep:
  out2 = out2.replace(i + ".Schema", rep[i]);
  out2 = out2.replace(i, rep[i]);

with open("out.txt", "w") as f:
  f.write(out2)