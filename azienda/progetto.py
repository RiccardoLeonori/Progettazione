from __future__ import annotations
from custom_types import RealGEZ

class Progetto:
    _nome: str # noto alla nacita
    _budget: RealGEZ # noto alla nascita
    _impiegati: dict['Impiegato': 'Coinvolto']

    def __init__(self, nome: str, budget: RealGEZ) -> None:


        self.set_nome(nome)
        self.set_budget(budget)
        self._impiegati = {}
    
    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
    def set_budget(self, budget: RealGEZ) -> None:
        self._budget = budget

    def budget(self) -> RealGEZ:
        return self._budget
    
    def add_impiegato(self, impiegato: 'Impiegato') -> None:
        from impiegato import Impiegato
        from coinvolto import Coinvolto
        if impiegato not in self._impiegati:
            coinvolto: 'Coinvolto' = Coinvolto(self, Impiegato)
            self._impiegati[impiegato] = coinvolto
            impiegato._progetti[self] = coinvolto
        else:
            raise ValueError("L'impiegato già è coinvolto nel progetto")
        
    def remove_impiegati(self, impiegato:'Impiegato') -> None:
        if impiegato in self._impiegati:
            self._impiegati.pop(impiegato)
            impiegato._progetti.pop(self)
        else:
            raise ValueError("L'impiegato non è coinvolto nel progetto")
        
    def impiegati(self) -> dict['Impiegato', 'Coinvolto']:
        return self._impiegati