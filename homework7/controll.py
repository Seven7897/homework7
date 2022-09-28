import db

number = 0
def options():
    number = int(input(f"что собираемся делать ? : \n Выберите 1 если добавить \n Выберите 2 если удалить \n Выберите 3 если обновить \n Выберите 4 если найти \n Выберите 5 если показать всю базу : "))
    if number == 1:
        db.add()
    if number == 2:
        db.delete()
    if number == 3:
        db.update()
    if number == 4:
        db.find()
    if number == 5:
        db.find_oll()
    


