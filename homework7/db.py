import sqlite3

def add():
    base = sqlite3.connect('new.db')
    cur = base.cursor()

    base.execute('CREATE TABLE IF NOT EXISTS data(name, surname, phonenumber PRIMARY KEY, comment)')
    base.commit

    cur.execute('INSERT INTO data VALUES(?, ?, ?, ?)',(input("name : "), input("surname : "), input("phone number : "), input("comment : ")))
    base.commit()

def delete():
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    variant = int(input("Удаляем по : \n 1 если по name \n 2 если по surname \n 3 если по phone number \n 4 если по comment : "))
    if variant == 1:
        cur.execute('DELETE FROM data WHERE name == ?', (input("Введите имя кого удаляем ? "),)) 
        base.commit()
    if variant == 2:
        cur.execute('DELETE FROM data WHERE surname == ?', (input("Введите фамилию кого удаляем ? "),)) 
        base.commit()
    if variant == 3:
        cur.execute('DELETE FROM data WHERE phonenumber == ?', (input("Введите телефон кого удаляем ? "),)) 
        base.commit()
    if variant == 4:
        cur.execute('DELETE FROM data WHERE comment == ?', (input("Введите коментарий кого удаляем ? "),)) 
        base.commit()

def update():
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    variant = int(input("Что обновляем ? \n 1 если name \n 2 если surname 3 \n если phonenumber \n 4 если comment"))
    variant_1 = int(input("На что обновляем ? \n 1 если name \n 2 если surname \n 3 если phonenumber \n 4 если comment"))
    if variant == 1 and variant_1 == 1:
        cur.execute('UPDATE data SET name == ? WHERE name == ?', (input("Введите на которое нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()
    if variant == 1 and variant_1 == 2:
        cur.execute('UPDATE data SET name == ? WHERE surname == ?', (input("Введите на которое нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()
    if variant == 1 and variant_1 == 3:
        cur.execute('UPDATE data SET name == ? WHERE phonenumber == ?', (input("Введите на которое нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()
    if variant == 1 and variant_1 == 4:
        cur.execute('UPDATE data SET name == ? WHERE comment == ?', (input("Введите на которое нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()
    if variant == 2 and variant_1 == 1:
        cur.execute('UPDATE data SET surname == ? WHERE name == ?', (input("Введите на которое нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()
    if variant == 2 and variant_1 == 2:
        cur.execute('UPDATE data SET surname == ? WHERE surname == ?', (input("Введите на которое нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()
    if variant == 2 and variant_1 == 3:
        cur.execute('UPDATE data SET surname == ? WHERE phonenumber == ?', (input("Введите на которое нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()
    if variant == 2 and variant_1 == 4:
        cur.execute('UPDATE data SET surname == ? WHERE comment == ?', (input("Введите на которое нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()
    if variant == 3 and variant_1 == 3:
        cur.execute('UPDATE data SET phonenumber == ? WHERE phonenumber == ?', (input("Введите на который нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()
    if variant == 4 and variant_1 == 4:
        cur.execute('UPDATE data SET comment == ? WHERE comment == ?', (input("Введите на который нужно поменять  : "), (input("у кого ? ")))) 
        base.commit()


def find():
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    variant = int(input("Выберите поиск чего : \n 1 если  name :  \n 2 если  surname :   \n 3 если  phone numbers : \n 4 если  comment : "))
    variant_2 = int(input("Выберите поиск по : \n 1 если по name :  \n 2 если по surname :   \n 3 если по phone numbers : \n 4 если по comment : "))
    if variant == 1 and variant_2 == 2 :
        read = cur.execute('SELECT name FROM data WHERE surname == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 1 and variant_2 == 3 :
        read = cur.execute('SELECT name FROM data WHERE phonenumber == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 1 and variant_2 == 4 :
        read = cur.execute('SELECT name FROM data WHERE comment == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 2 and variant_2 == 1 :
        read = cur.execute('SELECT surname FROM data WHERE name == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 2 and variant_2 == 3 :
        read = cur.execute('SELECT surname FROM data WHERE phonenumber == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 2 and variant_2 == 4 :
        read = cur.execute('SELECT surname FROM data WHERE comment == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 3 and variant_2 == 1 :
        read = cur.execute('SELECT phonenumber FROM data WHERE name == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 3 and variant_2 == 2 :
        read = cur.execute('SELECT phonenumber FROM data WHERE surname == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 3 and variant_2 == 4 :
        read = cur.execute('SELECT phonenumber FROM data WHERE comment == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 4 and variant_2 == 1 :
        read = cur.execute('SELECT comment FROM data WHERE name == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 4 and variant_2 == 2 :
        read = cur.execute('SELECT comment FROM data WHERE surname == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 4 and variant_2 == 3 :
        read = cur.execute('SELECT comment FROM data WHERE phonenumber == ?', (input(': '),)).fetchone()  
        print(read)


def find_oll():
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    read = cur.execute('SELECT * FROM data').fetchall() 
    print(read)


