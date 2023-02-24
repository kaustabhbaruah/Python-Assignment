input_list = [1, 2, 3, 2, 1, 5, 8, 9, 2, 4, 6, 4, 2, 3, 7]
count = 0
for i in range(0, len(input_list)):
 if input_list[i] == 2:
  count += 1
print("The occurance of number 2 in the list: "+ str(count))