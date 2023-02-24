file = open("myfile.txt","r") 
Counter=0
Content = file.read() 
CoList = Content.split("\n") 
for i in CoList: 
    if i[0]!="A": 
        Counter += 1 
print(Counter)