from enum import *
from typing import Any, Self
import re

class Genere(StrEnum):
    uomo = auto()
    donna = auto()


class IntGZ(int):

    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n: int = super().__new__(cls, valore)
        if n >= 0:
            return n
        raise ValueError(f"Numero inserito non positivo")
    

class IntG1900(int):
    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n: int = super().__new__(cls, valore)
        if n > 1900:
            return n
        raise ValueError(f"Numero inserito non valido")
    
    

class Voto:
    v: int
    def __init__(self, v: int):
        if v < 18 or v > 31:
            raise ValueError("Il voto deve essere tra 18 e 31")
        self.v = v

    def __eq__(self, other: Any) -> bool:
        return self.v == other.v



class RealeMaggioreDiZero(float):
    r: float
    def __new__(cls, r: float):
        if r <= 0.0:
            raise ValueError("Il valore deve essere un valore reale maggiore di 0")
        return float.__new__(r)



class RealeTraZeroUno(float):
    r: float
    def __new__(cls, r: float):
        if r < 0.0 or r > 1.0:
            raise ValueError("Il valore deve essere un valore reale tra 0 e 1")
        return float.__new__(r)



class NumeroTelefono(str):
    n: str
    def __new__(cls, n: str):
        if n != re.compile(r"^(?:\+39)?\s?(?:0\d{1,3}|\(?0\d{1,3}\)?)\s?\d{5,8}$"):
            raise ValueError("Devi inserire il numerodi telefono rispettando bene i parametri")
        return str.__new__(n)



class CodiceFiscale(str):
    c: str
    def __new__(cls, c: str):
        pattern = r"^[A-Z]{6}[0-9]{2}[A-EHLMPR-T][0-9]{2}[A-Z][0-9]{3}[A-Z]$"
        if not re.fullmatch(pattern, c):
            raise ValueError("Devi inserire il codice fiscale rispettando bene i parametri")
        return super().__new__(cls, c)

    def __str__(self):
        return f"Il codice fiscale è {self}"

            


class Email(str):
    e: str
    def __new__(cls, e: str):
        if e != re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"):
            raise ValueError("Devi inserire l'email rispettando bene i parametri")
        return str.__new__(e)



if __name__ == '__main__':
    print(Genere.uomo)
    print(Genere.donna)