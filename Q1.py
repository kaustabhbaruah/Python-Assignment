ss = input("Enter the input string: ")
print("Input string is: ")
print(ss)
a = []
a.append(ss.split())
aa = {}
for i in range(0,len(a[0])):
 aa[a[0][i]] = len(a[0][i])
print("Required dictionary is: ")
print(aa)