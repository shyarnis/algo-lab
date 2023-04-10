def input_llist(n):
    '''Return user input list of size n '''
    rand_list = []
    for i in range(n):
        new_num = int(input(f"Enter {i+1} number : "))
        rand_list.append(new_num)
    return rand_list

def input_list(n):
    '''Return user input list of size n '''
    return [int(input(f"Enter {i+1} number: ")) for i in range(n)]

