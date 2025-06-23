import doctest
from typing import Self, Type
from typing import Any
import re


class RealGEZ(float):
    # Tipo di dato Reale >= 0

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'float'
        n: float = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")


class Telefono(str):
    def __new__(cls, t: str | Self) -> Self:
        if re.fullmatch(r"^\d{10}$", t):
            return super().__new__(cls, t)
        raise ValueError(f"'{t}' non è un numero di telefono italiano valido")


class CAP(str):
    def __new__(cls, v: str | Self) -> Self:
        if re.fullmatch(r"^\d{5}$", v):
            return super().__new__(cls, v)
        raise ValueError(f"'{v}' non è un CAP italiano valido!")

class Indirizzo:
    # campi dati:
    _via:str
    _civico: str
    _cap: CAP
    def __init__(self, via: str, civico: str, cap: CAP) -> None:
        self._via: str = via

        if not re.search("^[0-9]+[a-zA-Z]*$", civico):
            raise ValueError(f"value for civico '{civico}' not allowed")
        self._civico: str = civico
        self._cap: CAP = cap

    def via(self) -> str:
        return self._via

    def civico(self) -> str:
        return self._civico

    def cap(self) -> str:
        return self._cap

    def __repr__(self) -> str:
        return f"Indirizzo(via={self.via()}, civico={self.civico()}, cap={self.cap()})"

    def __str__(self) -> str:
        return f"{self.via()} {self.civico()} - {self.cap()}"

    # class Indirizzo implementa un tipo di dato: Python deve riconoscere se oggetti diversi rappresentano lo stesso valore
    def __hash__(self) -> int:
        return hash((self.via(), self.civico(), self.cap()))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return (self.via(), self.civico(), self.cap()) == (other.via(), other.civico(), other.cap())


if __name__ == "__main__":

    tel1: Telefono = Telefono("ciao")