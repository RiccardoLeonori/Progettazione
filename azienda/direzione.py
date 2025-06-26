from __future__ import annotations

class Direzione():
    _impiegato: 'Impiegato' 
    _dipartimento: 'Dipartimento'

    def __init__(self, impiegato: 'Impiegato', dipartimento: 'Dipartimento') -> None:
        from impiegato import Impiegato
        from dipartimento import Dipartimento
        self._impiegato = impiegato
        self._dipartimento = dipartimento

    def impiegato(self) -> 'Impiegato':
        return self._impiegato
    
    def dipartimento(self) -> 'dipartimento':
        return self._dipartimento