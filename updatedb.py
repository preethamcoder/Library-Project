def update_db_val():
    print("Enter your Library ID")
    libid = int(input())
    query1 = "select * from Members where ID = {0};"
	cursor.execute(query1)
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
            str2 = 'update Members set {0} = {1} where ID = {3};'.format(cng1, upd2, libid)
            cursor.execute(str2)
            print("Your information is now: ")
            cursor.execute(query1)
    else:
        print("Try again with another Library ID number.")