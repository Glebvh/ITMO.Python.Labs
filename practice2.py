# -*- coding: utf-8 -*-
# # 1
# string1 = "This is a string."
# string2 = " This is another string. "
#
# # 2
# string3 = string1 + string2
# print("This is a string." + "This is another string." + string3)
#
# # 3
# print(len(string2))
# print(string2.title())
# print(string2.lower())
# print(string2.upper())
# print(string2.rstrip())
# print(string2.lstrip())
# print(string2.strip('. gT'))
#
# # 4 - 7
# d = "qwerty"
# ch = d[2]
# print(ch)
#
# chm = d[1:5:2]
# print(chm)
#
# # nums
# a = 15
# b = 6
# print(a % b)
# param = "string" + str(15)
# print(param)

# # datas
# n1 = input("Enter the first number: ")
# n2 = input("Enter the second number: ")
# n3 = float(n1) + float(n2)
# print(n1 + " plus " + n2 + " = ", "{:!=+10.0f}".format(n3))
#
# # format
# a = 1/3
# print("{:7.3f}".format(a))
# a = 2/3
# b = 2/9
# print("{:7.3f} {:7.3f}".format(a, b))
# print("{:10.3e} {:10.3e}".format(a, b))

# list
# list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
# print(dir(list1))
# list1[0] = 777
# print(list1)
# list1.append(999)
# print(list1)
# list1.insert(6, 666)
# print(list1)
# list1.pop(6)
# print(list1)
# list1.pop()
# print(list1)
# list2 = sorted(list1, reverse=True)
# list1.sort(reverse=True)
# print(list1)
#
# # tuple
# seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
# print(seq.count(8))
# print(seq.index(44))
# list_seq = list(seq)
# print(list_seq)
# print(type(list_seq))
#
# # dictionary
# D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
# print(D['food'])
# D['quantity'] += 10
# print(D)
# dp = {}
# # dp['name'] = input('first: ')
# # dp['age'] = input('second: ')
# print(dp)
#
# # nesting
# rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 25}
# print(rec['name'])
# print(rec['name']['lastname'])
# print(rec['job'])
# rec['job'].append('janitor')
# print(f'employer {rec["name"]["firstname"]} {rec["name"]["lastname"]} has age {rec["age"]} and {rec["job"][2]} job')

x = 142.673701
y = -73.608792
k = str('{:010.9}'.format(abs(x)))
print(f'{k[0:3]}\xb0{k[4:6]}\'{k[6:8]}.{k[8:10]}\"')

