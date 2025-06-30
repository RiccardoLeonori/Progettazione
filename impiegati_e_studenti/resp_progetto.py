from classi import Impiegato, Progetto


class Resp_Progetto:
    _impiegato: Impiegato
    _progetto: Progetto

    def __init__(self, impiegato: Impiegato, progetto: Progetto) -> None:
        self._impiegato = impiegato
        self._progetto = progetto

    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def progetto(self) -> Progetto:
        return self._progetto