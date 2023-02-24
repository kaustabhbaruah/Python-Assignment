def get_dict(list1, list2):
    return {
        'milk': list1,
        'bread': list2
    }

def expenses_milk_bread(filename):
   
    letter_list = []
    with open(filename, 'r') as file:
        for line in file:
            letter_list.append(line.split())
    
    
    m_list = []
    b_list = []
    for i in letter_list:
        if i[0] == 'b':
            i.pop(0)
            b_list.append(i)
        elif i[0] == 'm':
            i.pop(0)
            m_list.append(i)

   
    new_m_list = []
    for i in m_list:
        new_m_list.append([float(ele) for ele in i])

    new_b_list = []
    for i in b_list:
        new_b_list.append([float(ele) for ele in i])

    return get_dict(new_m_list, new_b_list)


print(expenses_milk_bread('myfile.txt'))