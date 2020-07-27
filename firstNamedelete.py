x = str(input())
name = '"' + x + '"'
def delete_rows_FN(name):
	str1 = 'delete from Members where FirstName = name'
	cursor.execute()