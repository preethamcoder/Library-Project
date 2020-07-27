# This line imports the python packge needed to connect to the MySQl db
import mysql.connector
# Capture the errors
#from mysql.connector import Error
#import math
from random import randint
connection = mysql.connector.connect(host='localhost', database='lib102', user='root', password='Passw0rd$')
    # If the connection is established or not?
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    
    #insert into Members (ID, FirstName, LastName, Phoneno, Email, SSN, Address, Gender) VALUES (LPAD(FLOOR(RAND() * 999999.99), 6, 'x'), "Kaushik", "Konda", "4049998888", "sk1@gmail.com", "4433251234", "101 Isle", "Male"), (LPAD(FLOOR(RAND() * 999999.99), 6, 'x'), "Errol", "Williams", "2129098765", "ewilliams3@gmail.com", "3344556612", "309 Plaza", "Male");
    #cursor.execute('insert into Members (ID, FirstName, LastName, Phoneno, Email, SSN, Address, Gender) VALUES (LPAD(FLOOR(RAND() * 999999.99), 6, "x"), "King", "Marshall", "4012345645", "mka1@gmail.com", "8966534345", "198 Way", "Male");')
    #cursor.execute("commit;")
    #update_database(n)
cursor = connection.cursor()
#This function will delete all rows in a database where the phone number ends with a specific order of numbers.
def phone_end(mycursor):
    print("This function will delete all rows in a database where the phone number ends with a specific order of numbers.")
    x = int(input())
    y = "'%" + x + "'"
    dtr1 = "delete from Members where Phoneno like {0}".format(y)
    mycursor.execute(dtr1)
    mycursor.execute('commit;')
#The below function will delete all rows in a database where the phone number starts with a specific order of letters.
def phone_beg(mycursor):
    print("This function will delete all rows in the databse when the phone number starts with a specific order of numbers")
    x = int(input())
    y = "'" + x + "%'"
    dtr1 = "delete from Members where Phoneno like {0}".format(y)
    mycursor.execute(dtr1)
    mycursor.execute('commit;')
#The below function will delete all rows in a database where the last name starts with a specific order of letters.
def beg_del_ln(mycursor):
    print("This function will delete all the records in a database where the last name starts with a specific order of letters.")
    x = str(input())
    y = "'" + x + "%'"
    dtr1 = "delete from Members where LastName like {0}".format(y) 
    mycursor.execute(dtr1)
    mycursor.execute('commit;')
#The below function will delete all rows in a database where the last name ends with a specific order of letters.
def end_del_ln(mycursor):
    print("This function will delete all the records in a database where the last name ends with a specific order of letters.")
    x = str(input())
    y = "'%" + x + "'"
    dtr1 = "delete from Members where LastName like {0}".format(y) 
    mycursor.execute(dtr1)
    mycursor.execute('commit;')
#This function will delete all the records in a database where the first name ends with a specific order of letters.
def end_del(mycursor):
    print("This function will delete all the records in a database where the first name ends with a specific order of letters.")
    x = str(input())
    y = "'%" + x + "'"
    dtr1 = "delete from Members where FirstName like {0}".format(y) 
    mycursor.execute(dtr1)
    mycursor.execute('commit;')
#This function will delete all the records in a database where the first name starts with a specific order of letters.
def beg_del(mycursor):
    print("This function will delete all the records in a database where the first name starts with a specific order of letters.")
    x = str(input())
    y = "'" + x + "%'"
    dtr1 = "delete from Members where FirstName like {0}".format(y) 
    mycursor.execute(dtr1)
    mycursor.execute('commit;')
def update_db_val(mycursor):
    print("Enter your Library ID")
    libid = int(input())
    query1 = "select * from Members where ID = {0};".format(libid)
    #print(query1)
    mycursor.execute(query1)
    #mycursor.execute('select * from Members;')
    record = mycursor.fetchall()
    for row in record:
        print(row)
    print("Is this you? (Y / N)")
    x = str(input())
    if(x == "Y"):
        print("How many things do you want to change?")
        a = int(input())
        for i in range(a):
            print("What do you want to change? Your options are: Phoneno, Email, or Address")
            cng1 = str(input())
            print("What do you want to change it to?")
            upd1 = input()
            upd2 = '"' + upd1 + '"'
            str2 = 'update Members set {0} = {1} where ID = {2};'.format(cng1, upd2, libid)
            #print(str2)
            mycursor.execute(str2)
            mycursor.execute('commit;')
            print("Your information is now: ")
            #print(query1)
            mycursor.execute(query1)
            rec = mycursor.fetchall()
            for raw in rec:
                print(raw)
    else:
        print("Try again with another Library ID number.")

# n is the prameter passed to the belwo function
# This isnot checked for definition.
# 
def insert_values_into_database(mycursor):
    print("How many entries do you want to insert into this module?")
    n = int(input())
    FirstNames = ["John", "Dwayne", "David", "Shane", "Darren"]
    LastNames = ["Lewis", "Smith", "Sammy", "Watson", "Warner"]
    Phoneno = (randint(1123456781, 9999999999))  # Generate 10 digit random number
    #Email = "sk1@gmail.com"  # EMAILNAMEPARTR .. PROVIDER :
    SSN = (randint(1000000001, 9999999999))
    AddressList = ["Isle", "Street", "Way", "Colony"]
    Address = str(randint(1, 1000)) + " " + AddressList[randint(0, len(AddressList)-1)]
    Genderlist = ["Male", "Female"]
    Gender = ""
    for i in range(n):
        if(i < 500):
            FirstName = FirstNames[randint(0, 4)]
            LastName = LastNames[randint(0, 4)]
        else:
            LastName = FirstNames[randint(0, 4)]
            FirstName = LastNames[randint(0, 4)]
        #print(Address)
        if(randint(1, 100000000000000000000000000001) % 2 == 0):
            Gender = Genderlist[1]
        else:
            Gender = Genderlist[0]
        Email = str(FirstName) + str(randint(1, 99879)) + "@gmail.com"
        FN = '"' + FirstName + '"'
        LN = '"' + LastName + '"'
        PN = '"' + str(Phoneno) + '"'
        SN = '"' + str(SSN) + '"'
        Ad = '"' + Address + '"'
        Gen = '"' + Gender + '"'
        Em = '"' + Email + '"'
        #str1 = "insert into Members (FirstName, LastName) values ({0}, {1})".format(a, b)
        str1 = 'insert into Members (ID, FirstName, LastName, Phoneno, Email, SSN, Address, Gender) values ((LPAD(FLOOR(RAND() * 999999.99), 6, \' x \')), {0}, {1}, {2}, {3}, {4}, {5}, {6});'.format(FN, LN, PN, Em, SN, Ad, Gen)
        mycursor.execute(str1)
        mycursor.execute('commit;')
        #print(str1)
#x = str(input())
#name = "'" + x + "'"
#print(name)
#Use .format() to get over the loopholes in SQL
def delete_rows_FN(name):
	str2 = "DELETE from Members WHERE FirstName={0};".format(name)
	cursor.execute(str2)
    cursor.execute('commit;')
#delete_rows_FN(name)
#Using try except is a good practivce of programming to catche all possible errors
#try:
    #Connect to the database using you MySQL db details like, host name, USerid, Password.
    # This return a connection object+                                                                                                                                                                                          
insert_values_into_database(cursor)
#beg_del()
update_db_val(cursor)
#record = cursor.fetchall()
cursor.execute("select * from Members;")
#cursor.execute('commit;')
record = cursor.fetchall()
print('-----------------------------------------------------------------------------------------------------------------------')    
for row in record:
    print(row)

#print("You're connected to database: ", record)


#except Error as e:
 #   print("Error while connecting to MySQL", e)
if (connection.is_connected()):
    cursor.close()
    #connection.close()
    print("MySQL connection is closed")