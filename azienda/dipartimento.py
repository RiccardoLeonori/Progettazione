from __future__ import annotations
from custom_types import Telefono, Indirizzo
from datetime import date
class Dipartimento:

    _nome: str # noto alla nascita
    _telefoni: set[Telefono] # [1..*] noto alla nascita
    _indirizzo: Indirizzo | None  # [0..1] possibilmente non noto alla nascita
    _direttore : 'Impiegato' # noto alla nascita
    _impiegati : dict['Impiegato': 'Afferenza'] # certamente non noto alla nascita
    _direttore : tuple('Impiegato', 'Direzione') # certamente noto alla nascita

    def __init__(self, nome: str, tel: Telefono, ind: Indirizzo|None, direttore: 'Impiegato') -> None:
        from impiegato import Impiegato

        self.set_nome(nome)

        # opzione 1
        self._telefoni = set()
        self.add_telefono(tel)
        # opzione 2
        # self.set_telefoni({tel})

        self.set_indirizzo(ind)
        self._impiegati = {}
        self._direttore = None
        self.set_direttore(direttore)

    def nome(self) -> str:
        return self._nome

    def indirizzo(self) -> Indirizzo | None:
        return self._indirizzo

    def telefoni(self) -> frozenset[Telefono]:
        return frozenset(self._telefoni)

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_indirizzo(self, i: Indirizzo | None) -> None:
        self._indirizzo = i

    def add_telefono(self, telefono: Telefono) -> None:
        self._telefoni.add(telefono)

    def set_telefoni(self, telefoni: set[Telefono]) -> None:
        if not telefoni: # equivalente a len(telefoni) == 0
            raise ValueError("Il dipartimento deve avere almeno un numero di telefono")
        self._telefoni = telefoni

    def remove_telefono(self, telefono: Telefono) -> None:
        if len(self._telefoni) >= 2: # telefono è [1..*]!
            self._telefoni.remove(telefono)
        else:
            raise RuntimeError("Il dipartimento deve avere almeno un numero di telefono")

    def __str__(self):
        if self._indirizzo is None:
            ind_str: str = "senza sede"
        else:
            ind_str: str = f"con sede in {self.indirizzo()}"

        return f"Dipartimento '{self.nome()}' {ind_str} e numeri telefono: {self.telefoni()}"
    
    def add_impiegato(self, impiegato: 'Impiegato', data: date) -> None:
        from afferenza import Afferenza
        if impiegato not in self._impiegati:
            afferenza: 'Afferenza' = Afferenza(self, impiegato, data)
            self._impiegati[impiegato] = afferenza
            impiegato._dipartimento = (self, afferenza)
        else:
            raise ValueError("L'impiegato lavora già nel dipartimento")
        
    def remove_impiegati(self, impiegato:'Impiegato') -> None:
        if impiegato in self._impiegati:
            self._impiegati.pop(impiegato)
            impiegato._dipartimento = None
        else:
            raise ValueError("L'impiegato non lavora nel diparitmento")
        
    def impiegati(self) -> dict['Impiegato', 'Afferenza']:
        return self._impiegati
    
    def set_direttore(self, direttore: 'Impiegato') -> None:
        from direzione import Direzione
        if self._direttore:
            self._direttore[0]._dirige.pop(self)
        link = Direzione(direttore, self)
        self._direttore = (direttore, link)
        direttore._dirige[self] = link

    def direttore(self) -> tuple('Impiegato', 'Direzione'):
        return self._direttore


if __name__ == "__main__":
    pass