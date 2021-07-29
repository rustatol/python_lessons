my_list = [7, 5, 3, 3, 2]
print(my_list)
value = int(input("Введите рейтинг: "))
max_value = max(my_list)

if value > max_value:

    my_list.insert(0,value)

elif value in my_list:

    my_list.insert(-my_list[::-1].index(value),value)

else:

    my_list.append(value)

print(my_list)







