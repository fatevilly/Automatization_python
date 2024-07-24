from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Iphone", "15Pro", "+79223334455")
phone2 = Smartphone("Samsung", "Galaxy", "+79334445566")
phone3 = Smartphone("Redme", "A2", "+79445556677")
phone4 = Smartphone("Nokia", "3310", "+79556667788")
phone5 = Smartphone("LG", "10", "+7966777889900")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(phone.brand, "-", phone.model, ".", phone.number)