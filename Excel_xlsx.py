import pandas as pd
location = 'E:\mani\employees.xlsx'
df = pd.read_excel(location)
d = df.sort_values('Years_of_experience', ascending=True)
d1 = df.sort_values('Years_of_experience', ascending=False)
print("Before Sorting: \n\n", df, "\n\n")
print("Ascending Order: \n\n", d, "\n\n")
print("Descending Order: \n\n",d1)


###---Output---###

Before Sorting:


 Name          Years_of_experience      Job_Title     Date_of_Birth
 Mani                  2                 DevOps        1999-08-19
 kumar                 4                 Devloper      1999-09-19
 mkr                   1                 DevOps        2000-08-12
 siva                  3                 MuleSoft      1998-12-09
 ram                   5                 Testing       1997-08-27 


Ascending Order:


Name         Years_of_experience    Job_Title     Date_of_Birth
mkr                 1                 DevOps        2000-08-12
Mani                2                 DevOps        1999-08-19
siva                3                 MuleSoft      1998-12-09
kumar               4                 Devloper      1999-09-19
ram                 5                 Testing       1997-08-27


Descending Order:
 
  Name         Years_of_experience     Job_Title    Date_of_Birth
  ram                    5             Testing       1997-08-27
  kumar                  4             Devloper      1999-09-19
  siva                   3             MuleSoft      1998-12-09
  Mani                   2             DevOps        1999-08-19
  mkr                    1             DevOps        2000-08-12



