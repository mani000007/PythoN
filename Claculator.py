class Calculations:
    def Cal(n1, n2):

        def add(n1, n2):
            return n1 + n2

        def sub(n1, n2):
            return n1 - n2

        def mul(n1, n2):
            return n1 * n2

        def div(n1, n2):
            return n1 / n2

        count = 0
        print("Select Operation:")
        print("1.add")
        print("2.sub")
        print("3.mult")
        print("4.Division")
        while True:
            choice = input("enter ur choice:  ")

            if choice == '1':
                print(f"{n1}+{n2}={add(n1, n2)}")
                count += 1

            elif choice == '2':
                print(f"{n1}-{n2}={sub(n1, n2)}")
                count += 1

            elif choice == '3':
                print(f"{n1}*{n2}={mul(n1, n2)}")
                count += 1

            elif choice == '4':
                if n2 != 0:
                    print(f"{n1}/{n2} = {div(n1, n2)}")
                    count += 1
                else:
                    print("division of zero not possible")
            elif choice.lower() == "exit":
                break
            else:
                print("Invalid choice, please Enter Valid Choice")

        print("The number of calculations: ", count)

    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter a Second number:"))
        Cal(num1, num2)
    except:
        print("Enter only numbers")


###OUTPUT###
Enter first number:1
Enter a Second number:2
Select Operation:
1.add
2.sub
3.mult
4.Division
enter ur choice:  1
1+2=3
enter ur choice:  2
1-2=-1
enter ur choice:  3
1*2=2
enter ur choice:  4
1/2 = 0.5
enter ur choice:  exit
The number of calculations:  4