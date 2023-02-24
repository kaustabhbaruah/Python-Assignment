sample_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in range(0, len(sample_list)):
 if len(sample_list[i]) >= 2 and sample_list[i][0] == sample_list[i][-1]:
  count += 1
print("Expected result : " + str(count))
