#########PROGRAME-1:######################
my_list=[1, 2, 2, 4, 4, 6, 6, 8, 10, 13, 22, 35, 52, 83]
list1 = []
list2 = []
list1.append([i for i in my_list if i>=10])
print(list1)
value = int(input("Enter User value: "))
for i in my_list:
    if i > value:
        list2.append(i)
print(list2)
#####OUTPUT#######
[[10, 13, 22, 35, 52, 83]]
Enter User value: 4
[6, 6, 8, 10, 13, 22, 35, 52, 83]
#########PROGRAMME-2:#####################
employees={'name':'Tim', 'age':30, 'birthday':'1990-03-10', 'job':"Devops Engineer"}
print(f"The Details of Employees is: {employees}")
employees['job']='Software Engineer'
employees.pop('age')
print("\nAfter updated:\n")
for i,j in employees.items():
    print(i ,':',j)
###OUTPUT###
The Details of Employees is: {'name': 'Tim', 'age': 30, 'birthday': '1990-03-10', 'job': 'Devops Engineer'}
After updated:
name : Tim
birthday : 1990-03-10
job : Software Engineer
#########################PROGRAMME-3:#######################

employees = [
    {'name': 'Tanya', 'age': 20, 'birthday': '1990-03-10',
    {'name': 'Tina', 'age': 20, 'birthday': '1990-03-10',
        'job': 'DevOps Engineer', 'address': {'city': 'New York', 'country': 'USA'}},
    {'name': 'Tim', 'age': 35, 'birthday': '1985-02-21', 'job': 'Developer', 'address': {'city': 'Sydney', 'country': 'Australia'}}]

@@ -58,6 +58,6 @@ print(employees[1]["address"]["country"])


###OUTPUT###
name:Tanya, DevOps Engineer, city:New York
name:Tina, DevOps Engineer, city:New York
name:Tim, job:Developer, city:Sydney
Australia