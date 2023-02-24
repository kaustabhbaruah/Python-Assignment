st = input("Enter an input string: ")
sz = len(st)
for i in range(0, sz):
 for j in range(0, i+1):
  print(st[j], end="")
  print("\n")
  print()
