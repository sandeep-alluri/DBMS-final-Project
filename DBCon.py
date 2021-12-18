import sqlite3  
  
cnt = sqlite3.connect("backup.dp")  
  
cnt.execute('''CREATE TABLE gfg(NAME TEXT,POINTS INTEGER,ACCURACY REAL);''')
cnt.execute('''INSERT INTO gfg VALUES(
'Count Inversion',20,80.5);''')
cnt.execute('''INSERT INTO gfg(ACCURACY, POINTS, NAME) VALUES(
90.5, 15, 'Kadanes Algo');''')
cnt.execute('''INSERT INTO gfg(NAME, ACCURACY, POINTS) VALUES(
'REVERSE STR', 100, 5);''')
cnt.commit()
print('Name, Points and Accuracy from '
      'records with accuracy greater than 85')
  
cursor = cnt.execute('''SELECT * FROM gfg WHERE ACCURACY>85;''')
for i in cursor:
    print(i[0]+"    "+str(i[1])+"   "+str(i[2]))
  
print('')  # Print new line
  
print('Name, Accuracy from '
      'records with accuracy greater than 85')
  
cursor = cnt.execute('''SELECT NAME, ACCURACY FROM
gfg WHERE ACCURACY>85;''')

for i in cursor:
    print(i[0]+"    "+str(i[1]))

