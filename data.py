names = ["Иван", "Игорь", "Анна"]
surnames = ["Иванов", "Николаев", "Петрова"]
metros = ["Чертановская", "Сокольники", "Коломенская"]
addresses = [
    "Москва, ул. Тверская, д. 1",
    "Москва, ул. Вишневая, д. 7",
    "Москва, пр-т Мира, д. 25",
]

order_data = [
    {
        "name": names[i],
        "surname": surnames[i],
        "metro": metros[i],
        "address": addresses[i],
        "phone": f"+7999000000{i + 1}",
    }
    for i in range(3)
]

day = [5, 7, 10]
period = [3, 5, 6]
color = ["black", "grey", "black"]
comment = ["hello", "", "world"]
