def fooo(n):
 dictt = {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five"
, '6': "six", '7': "seven", '8': "eight", '9': "nine"}
 return " ".join(map(lambda x: dictt[x], str(n)))
print(fooo(4721))
