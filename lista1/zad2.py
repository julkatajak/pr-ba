from zad1 import Vector
v1 = Vector()
v2=Vector()
v3=Vector(2)
print("Wektor bez zadanej wartości:", v1)  
print("Wektor mający jedynie 2 elementy:", v3)
v1.losuj()
print("Wylosowane współrzędne dla wektora pierwszego:", v1) 
v2 = Vector()
v2.z_listy([1, 2, 3])
print("Wektor, którego wartości zostały wczytane z listy:", v2) 
v3 = v1 + v2
print("Suma wektorów 1 i 2:", v1+v2)  
v4 = v1 - v2
print("Rónica wektorów 1 i 2:", v1-v2)
v5 = v1 * 2
print("Wektor pierwszy, przemnozony przez skalar a=2:", v5) 
d1 = v1.dlugosc()
print("Długość wektora nr 1:", d1) 
s1 = v1.suma()
print("Suma elementów wektora 1:", s1)
p1 = v1.iloczyn_skalarny(v2)
print("Wynik mnozenia skalarnego wektorów v1 i v2:", p1)
e1 = v1[1]
print("Drugi element wektora nr 1 to:", e1)
c1 = 2 in v2
print("Sprawdzenie czy w wektorze nr 2 występuje '2':", c1)
c2 = 10 in v2
print("Sprawdzenie czy w wektorze nr 2 występuje '10':", c2)