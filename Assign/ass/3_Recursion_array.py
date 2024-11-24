def print_list_r(lst,index=0):

    if index == len(lst):
        return 1    

    print_list_r(lst, index + 1)
    print(lst[index])      
my_list = input()

print_list_r(my_list)
