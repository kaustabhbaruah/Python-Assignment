input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
output_list = []
for i in range(0, len(input_list)):
 if i != 0 and i != 2 and i != 4 and i != 5:
  output_list.append(input_list[i])
 else:
  continue
print(output_list)
