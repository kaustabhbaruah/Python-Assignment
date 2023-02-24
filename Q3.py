st = input("Enter the input string: ")
st = st.upper()
print("Input string is: "+ st)
c= 0
for i in range(0,len(st)//2):
 if st[i] == st[-(i+1)]:
  c += 1
if c == len(st)//2:
 print(st + " is palindrome")
else:
 print(st + " is not palindrome")
