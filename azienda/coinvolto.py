from __future__ import annotations



class Coinvolto():
    _progetto: 'Progetto' # immutabile noto alla nascita
    _impiegato: 'Impiegato' # immutabile noto alla nascita

    def __init__(self, progetto: 'Progetto', impiegato: 'Impiegato'):
        from impiegato import Impiegato
        from progetto import Progetto
        self._progetto = progetto
        self.self_impiegato = impiegato

    def progetto(self) -> 'Progetto':
        return self._progetto

    def impiegato(self) -> 'Impiegato':
        return self._impiegato