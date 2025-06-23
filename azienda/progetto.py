from custom_types import *


class Progetto:
    _nome: str
    _budget: RealGEZ

    def __init__(self, nome: str, budget: RealGEZ):
        self.set_nome(nome)
        self.set_budget(budget)
        self._impiegati = {}

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_budget(self, b: RealGEZ) -> None:
        self._budget: RealGEZ = b

    def get_nome(self):
        return f"Il nome è {self._nome}"
    
    def get_budget(self):
        return f"Il nome è {self._budget}"
    
    def add_impiegato(self, impiegato: 'Impiegato') -> None:
        from impiegato import Impiegato
        from coinvolto import Coinvolto
        if impiegato not in self._impiegati:
            coinvolto: 'Coinvolto' = 'Coinvolto'(self, 'Impiegato')
            self._impiegati[impiegato] = coinvolto
            impiegato._progetti[self] = coinvolto
        else:
            raise ValueError("L'impiegato è già coinvolto in un progetto")

    def remove_impiegato(self, impiegato:'Impiegato') -> None:
        from impiegato import Impiegato
        from coinvolto import Coinvolto
        if impiegato in self._impiegati:
            self._impiegati.pop(impiegato)
        else:
            raise ValueError("L'impiegato è già coinvolto in un progetto")