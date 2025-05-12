print("Hello")
my_list = [1 , 'apple', 3004 ]
my_list.append('mango')
my_list[0] = 2
print(my_list[0])
try:
    print(my_list[len(my_list)-2])
except IndexError:
    print("Array index error")
    print(my_list[len(my_list)-1])
finally:
    print("Pgm over")

my_tuple = (1 , 'apple', 3004 )
print(my_tuple[1])
try:
    my_tuple[0] = 2
except TypeError:
    print(my_tuple[0])

my_dict = {'name':"Mary",'age':22,'addr':"Little Flower Convent"}
if my_dict.get('name').find("mary"):
    print(my_dict.get('addr'))
