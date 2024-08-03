from address import Address
from mailing import Mailing

to_address = Address("454077", "Челябинск", "Шишкина", "51", "10")
from_address = Address("4550004", "Миасс", "Пушкина", "1", "12")
mailing = Mailing(to_address, from_address, 380, "333333")

print("Отправление", mailing.track,
       "из", mailing.from_address.indeks, mailing.from_address.city, mailing.from_address.street, mailing.from_address.house, mailing.from_address.flat, 
       "в",  mailing.to_address.indeks, mailing.to_address.city, mailing.to_address.street, mailing.to_address.house, mailing.to_address.flat,"."
       " Стоимость", mailing.cost, "pyблей.")