#Task 1: Տրված է list of lists։ Պետք է հեռացնել կրկնվող sublist-երը։
#English description:
#Given a list of lists, remove all duplicate sublists, preserving the original order.
#sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
from dis import disassemble


# def duples_cuter():
#     sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
#     new_list = []
#     for key in sample_list:
#         if key not in new_list:
#             new_list.append(key)
#     print(new_list)
# duples_cuter()

#Task 2: Flatten a given nested list structure
#Given a nested list structure, flatten it into a single list.

# def flatten_to_single():
#     original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
#     second_list =[]
#     for key in original_list:
#         if type(key) is list:
#             for emout in key:
#                 second_list.append(emout)
#         else:
#             second_list.append(key)
#     print(second_list)
# flatten_to_single()

#Task 3: Write a Python function to split a list
# into two parts, where the length of the first part is given.

def one_two():
    original_list = [1, 1, 2, 3, 4, 4, 5, 1]
    first_list = []
    second_list = []
    cout = 0
    for key in original_list:
        cout += 1
        if cout < 5:
            first_list.append(key)
        else:
            second_list.append(key)
    print(f'First list ==>{first_list}\n'
          f'Second list ==>{second_list}')

one_two()
