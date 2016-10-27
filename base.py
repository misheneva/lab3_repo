from methods import UserGet
from methods import FriendsGet

a = UserGet('35682979')
b = a.execute()
print(b)
print(b.json)

f = FriendsGet(b)
a = f.exectute()
print(a) #слова,Д, колво друзей
list_date = sorted(list(a.keys()), reverse=True) #отсортированный список годов
for i in list_date:
    print(2016 - int(i), end = ": ")
    for j in range(int(a[i])): #гистограмма возраст: кол-во друзей
        print("#", end="")
    print()