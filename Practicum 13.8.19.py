<<<<<<< HEAD
ticket = int(input())
persons = 0
cost = 0
while ticket>=1:
    age = int(input())
    if age < 18:
        print("Бесплатный билет!")
        ticket = ticket - 1
        persons +=1
    elif age >= 18 and age <= 25:
        cost = cost + 990
        print("Билет стоит 990 рублей!")
        ticket = ticket - 1
        persons +=1
    else:
        cost = cost + 1390
        print("Полная стоимость билета 1390 рублей")
        ticket = ticket - 1
        persons +=1
if persons >= 3:
    cost = cost * 0.9
    print("Скидка 10%, поздравляем")
else:
    print("У вас нет скидки")
=======
ticket = int(input())
persons = 0
cost = 0
while ticket>=1:
    age = int(input())
    if age < 18:
        print("Бесплатный билет!")
        ticket = ticket - 1
        persons +=1
    elif age >= 18 and age <= 25:
        cost = cost + 990
        print("Билет стоит 990 рублей!")
        ticket = ticket - 1
        persons +=1
    else:
        cost = cost + 1390
        print("Полная стоимость билета 1390 рублей")
        ticket = ticket - 1
        persons +=1
if persons >= 3:
    cost = cost * 0.9
    print("Скидка 10%, поздравляем")
else:
    print("У вас нет скидки")
>>>>>>> e51309027df14a9fc75195162dcace5e2ae1eee2
print("Сумма к оплате", cost)