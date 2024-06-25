out = "["
with open("txt_to_list/in.txt", "r") as f:
  inp = f.readlines()
  for i in inp:
    out += i.strip("\n")
    out += ", "
out = out.removesuffix(", ") + "]"

with open("txt_to_list/out.txt", "w") as f:
    f.write(out)