"""
Print out each element of the following array on a separate line:

['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""

# arr = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]
# #iterate through the list
# for item in arr:
#     #print each item in seperate lines
#     print(item)


"""
Stretch:
Print out each element of the following array on a separate line, but 
this time the input array can contain arrays nested to an arbitrarily deep level:
['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

For the above input, the expected output is:
Bob
Slack
reddit
89
101
alacritty
(brackets)
5
375
0
{slice, owned}
22
"""

x = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375,["hello"]]], 0, ['{slice, owned}'], 22]

def nested_print(nested_list):
    # interation (for loop)
    for item in nested_list:
        if isinstance(item, list):
            nested_print(item)
        else:
            print(item)

nested_print(x)
#condtional
#base case: if item 

    # for item in nested_list:
    #     if type(item) == str:
    #         print(item)
    #     elif type(item) == list:
    #         for i in item:
    #             if type(i) == str:
    #                 print(i)
    #             elif type(i) == list:
    #                 for x in i:
    #                     print(x)
    #     elif type(item) == int:
    #         print(item)  



