import random
import math

class Vector:
    """
    Klasa reprezentująca wektor w przestrzeni.
    """
    def __init__(self, rozmiar=3):
        """
        Konstruktor klasy Wektor.

        Input:
            rozmiar (int): Liczba elementów wektora.
        """
        self.rozmiar = rozmiar
        self.dane = [0] * rozmiar
    
    def losuj(self):
        """
        Losowo generuje wartości dla każdego elementu wektora.
        """
        self.dane = [random.uniform(-10, 10) for _ in range(self.rozmiar)]
    
    def z_listy(self, lista):
        """
        Ustawia wartości wektora na podstawie listy podanej jako argument.

        Input:
            lista (list): Lista wartości dla kolejnych elementów wektora.

        Output:
            ValueError: Jeśli lista ma nieprawidłowy rozmiar.
        """
        if len(lista) != self.rozmiar:
            raise ValueError("Nieprawidłowy rozmiar listy wejściowej")
        self.dane = lista
    
    def __add__(self, other):
        """
        Zwraca sumę dwóch wektorów.
        Input:
            other: Drugi wektor.

        Output:
            wynik: Wektor będący sumą dwóch wektorów.
            ValueError: Jeśli wektory mają różne rozmiary.
        """
        if self.rozmiar != other.rozmiar:
            raise ValueError("Wektory muszą mieć taki sam rozmiar")
        wynik = Vector(self.rozmiar)
        for i in range(self.rozmiar):
            wynik.dane[i] = self.dane[i] + other.dane[i]
        self.dane=wynik.dane
        return self.dane
    
    def __sub__(self, other):
        """
        Zwraca różnicę dwóch wektorów.
        Input:
            other: Drugi wektor.

        Output:
            wynik: Wektor będący różnicą dwóch wektorów.
            ValueError: Jeśli wektory mają różne rozmiary.
        """
        if self.rozmiar != other.rozmiar:
            raise ValueError("Wektory muszą mieć taki sam rozmiar")
        wynik = Vector(self.rozmiar)
        for i in range(self.rozmiar):
            wynik.dane[i] = self.dane[i] - other.dane[i]
        self.dane=wynik.dane
        return self
    
    def __mul__(self, skalar):
        """
        Zwraca wektor pomnożony przez podany skalar.
        Input:
            skalar (float): Wartość, przez którą mnożymy każdy element wektora.
        Output:
            wynik: Wektor pomnożony przez skalar.
        """
        wynik = Vector(self.rozmiar)
        for i in range(self.rozmiar):
            wynik.dane[i] = self.dane[i] * skalar
        self.dane=wynik.dane
        return self
    
    def dlugosc(self):
        """
        Zwraca długość wektora.

        Output:
            float: Długość wektora.
        """
        return math.sqrt(sum([x*x for x in self.dane]))
    
    def suma(self):
        """
        Zwraca sumę elementów wektora.
        output:
            float: Suma elementów wektora.
        """
        return sum(self.dane)
    
    def iloczyn_skalarny(self, other):
        """
        Zwraca iloczyn skalarny dwóch wektorów.
        Input:
            other: Drugi wektor.
        Output:
            float: Iloczyn skalarny dwóch wektorów.
            ValueError: Jeśli wektory mają różne rozmiary.
        """
        if self.rozmiar != other.rozmiar:
            raise ValueError("Wektory muszą mieć taki sam rozmiar")
        return sum([self.dane[i] * other.dane[i] for i in range(self.rozmiar)])
    
    def __repr__(self):
        """
        Zwraca reprezentację tekstową wektora.
        Output:
            str: Reprezentacja tekstowa wektora.
        """
        return f"Wektor({', '.join([str(x) for x in self.dane])})"
    
    def __getitem__(self, indeks):
        """
        Pozwala na dostęp do konkretnych elementów wektora.
        Input:
            indeks (int): Indeks elementu.
        Output:
            float: Wartość elementu o podanym indeksie.
        """
        return self.dane[indeks]
    
    def __contains__(self, wartosc):
        """
        Sprawdza przynależność wartości do wektora.
        Input:
            wartosc (float): Wartość, której przynależność do wektora chcemy sprawdzić.
        Output:
            bool: True, jeśli wartość należy do wektora, False w przeciwnym przypadku.
       """
        return wartosc in self.dane
