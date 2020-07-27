import string
from random import randint
print("Enter the number of enteries you want to fill in the database:")
n = int(input())
def update_database(n):
    FirstNames = ["John", "Dwayne", "David", "Shane", "Darren"]
    LastNames = ["Lewis", "Smith", "Sammy", "Watson", "Warner"]
    for i in range(n):
        if(i < 500):
            FirstName = FirstNames[randint(0, 4)]
            LastName = LastNames[randint(0, 4)]
        else:
            LastName = FirstNames[randint(0, 4)]
            FirstName = LastNames[randint(0, 4)]
        Phoneno = str(randint(1000000001, 9999999999))  # Generate 10 digit random number
        #Email = "sk1@gmail.com"  # EMAILNAMEPARTR .. PROVIDER :
        Email = FirstName + str(randint(1, 99879)) + "@gmail.com"
        SSN = str(randint(1000000001, 9999999999))
        AddressList = ["Isle", "Street", "Way", "Colony"]
        Address = str(randint(1, 1000)) + " " + AddressList[randint(0, len(AddressList)-1)]
        Genderlist = ["Male", "Female"]
        Gender = ""
        if(randint(1, 100000000000000000000000000000) % 2 == 0):
            Gender = Genderlist[1]
        else:
            Gender = Genderlist[0]
        #str1 = "insert into Members (FirstName, LastName) values ({0}, {1})".format(a, b)
        str1 = 'insert into Members (ID, FirstName, LastName, Phoneno, Email, SSN, Address, Gender) VALUES (LPAD(FLOOR(RAND() * 999999.99), 6, "x"), {0}, {1}, {2}, {3}, {4}, {5}, {6});'.format(FirstName, LastName, Phoneno, Email, SSN, Address, Gender)
        #print(str1)
        print(str1)

update_database(n)