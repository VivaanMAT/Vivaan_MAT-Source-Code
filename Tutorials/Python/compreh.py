# Comprehensions In List 
        # import random 

        # a = [random.randint(10,100) for n in range(20) ]
        # b = [(x,x**2,x**3) for x in range(11)]
        # print(b)
        # if 90 in a :
        #     print("90 is in a")
        # print(a)

        # c = [[1,2,3],[4,5,6],['Vivaan','MAT']]
        # d = [*c[2]]
        # print(d)
#Comprehensions in Dictionaries

# a = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
# a1 = {'f':6**3 for (f) in a.items()}
# # print(a1)

# a2 = {d:('Even' if x%2 == 0 else 'Odd') for (d, x) in a.items()}
# print(a2)