class System:
   def Prime(self):
       list = [10, 19, 3, 2, 23, 17, 20]
       count = 0
       for i in list:
           for j in range(2, i):
               if i % j == 0:
                   count += 1
           if count == 0:
               print(i)
           else:
               list.remove(i)

       print(list)

   def UpperAndLower(self):
       User_Input = input("Enter The UserInput: ")
       n = len(User_Input)
       m = []
       k = []
       for i in User_Input:
           if i.isupper():
               m.append(i)
           else:
               k.append(i)
       print(f"The Number of Upper case Letters are {len(m)} They are {m}, And Lower case Letters are {len(k)} They Are {k}")



s = System()
s.Prime()
s.UpperAndLower()


###---OutPut---###

The Listed Prime Numbers are [19, 2, 17]
Enter The UserInput: MANIkumar NeeRugaTTi
The Number of Upper case Letters are 8 They are ['M', 'A', 'N', 'I', 'N', 'R', 'T', 'T'], And Lower case Letters are 12 They Are ['k', 'u', 'm', 'a', 'r', ' ', 'e', 'e', 'u', 'g', 'a', 'i']
