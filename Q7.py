input_list = [12, 3, 4, 5, 6]
output_list = []
for i in range(0, len(input_list)):
 if input_list[i]%2 == 0:
  output_list.append(input_list[i])
else:
 output_list.append(input_list[i]+1)
print(output_list)
