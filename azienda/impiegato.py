from datetime import date
from custom_types import RealGEZ

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, noto alla nascita
    _stipendio: RealGEZ # noto alla nascita
    _coinvolti: dict['Progetto', 'Coinvolto'] # certamente non noto alla nascita


    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ) -> None:
        from coinvolto import Coinvolto
        from progetto import Progetto
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self._progetti = {}

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGEZ:
        return self._stipendio

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cognome(self, c: str) -> None:
        self._cognome: str = c

    def set_stipendio(self, s: RealGEZ) -> None:
        self._stipendio = s

    def progetti(self) -> dict['Progetto', 'Coinvolto']:
        return self._progetti

    def add_progetto(self, progetto: 'Progetto'):
        if progetto not in self._progetti:
            self.progetti[progetto] = 'Coinvolto'(progetto, self)
        else:
            raise ValueError("L'impiegato già è coinvolto in un progetto")
        
    def get_progetti(self):
        return f"I progetti sono {self._coinvolti}"