input_n = int(input("Enter n: "))
listt = list(range(1, input_n+1))
diction = {}
for i in range(0, input_n):
 diction[listt[i]] = listt[i]*listt[i]
print(diction)
