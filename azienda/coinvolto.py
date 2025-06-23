from impiegato import Impiegato
from progetto import Progetto


class Coinvolto():
    
    _progetti: Progetto
    _impiegato: Impiegato

    def __init__(self, progetto: Progetto, impiegato: Impiegato):
        self._progetto = progetto
        self._impiegato = impiegato

    def progetto(self) -> Progetto:
        return self._progetto
    
    def impiegato(self) -> Impiegato:
        return self._impiegato