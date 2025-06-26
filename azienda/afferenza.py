
from __future__ import annotations
from datetime import date

class Afferenza():
    _impiegato: 'Impiegato' 
    _dipartimento: 'Dipartimento'
    _data_afferenza: date # <<imm>>


    def __init__(self, impiegato: 'Impiegato', dipartimento: 'Dipartimento', data: date) -> None:
        from impiegato import Impiegato
        from dipartimento import Dipartimento
        self._impiegato = impiegato
        self._dipartimento = dipartimento
        self._data_afferenza = data

    def impiegato(self) -> 'Impiegato':
        return self._impiegato
    
    def dipartimento(self) -> 'Dipartimento':
        return self._dipartimento