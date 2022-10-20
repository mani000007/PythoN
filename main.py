class System:
   def Prime(self):   
        List = [4, 3, 6, 7, 9, 19, 5, 29]
        prime = []
        for i in List:
            count = 0
            for j in range(2, i):
                if i % j == 0:
                count += 1
            if count == 0:
                prime.append(i)
        print("The Listed Prime Numbers Are: \n", prime)


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

The Listed Prime Numbers Are: 
 [3, 7, 19, 5, 29]

Enter The UserInput: MANIkumar NeeRugaTTi
The Number of Upper case Letters are 8 They are ['M', 'A', 'N', 'I', 'N', 'R', 'T', 'T'], And Lower case Letters are 12 They Are ['k', 'u', 'm', 'a', 'r', ' ', 'e', 'e', 'u', 'g', 'a', 'i']
