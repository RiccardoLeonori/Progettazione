from __future__ import annotations
from custom_types import *


class Persona:
    _nome: str
    _cognome: str
    _cf: list[CodiceFiscale] # [1..*]
    _genere: Genere
    _maternita: IntGEZ # [0..1] - deve avere un valore se e solo se _genere = Genere.donna
    _posizione_mil: PosizioneMilitare | None # [0..1] da aggregazione, deve avere un valore se e solo se _genere = Genere.uomo

    def __init__(self, *, nome: str, cognome: str,
                 cf: list[CodiceFiscale],
                 genere: Genere,
                 maternita: IntGEZ|None=None,
                 pos: PosizioneMilitare|None=None) -> None:
        self._nome = nome
        self._cognome = cognome
        self._genere = None
        if not cf:
            raise ValueError("La persona deve avere almeno un codice fiscale!")

        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("È obbligatorio fornire il numero di maternità per le donne")
            self.diventa_donna(maternita)
        
        if genere == Genere.uomo:
            if pos is None:
                raise ValueError("È obbligatorio fornire la posizione militare per gli uomini")
            self.diventa_uomo(pos)

    def diventa_donna(self, maternita: IntGEZ) -> None:
        if self._genere == Genere.donna:
            raise RuntimeError("La persona era già una donna!")
        self._genere = Genere.donna
        self.set_maternita(maternita)
        self.__dimentica_uomo()

    def __dimentica_uomo(self) -> None:
        # metodo privato
        self._posizione_mil = None

    def set_maternita(self, maternita: IntGEZ) -> None:
        if not self._genere == Genere.donna:
            raise RuntimeError("Gli uomini non hanno il numero di maternità!")
        self._maternita = maternita

    def diventa_uomo(self, pos: PosizioneMilitare) -> None:
        if self._genere == Genere.uomo:
            raise RuntimeError("La persona era già un uomo!")
        self._genere = Genere.uomo
        self.set_posizione_mil(pos)
        self.__dimentica_donna()

    def __dimentica_donna(self) -> None:
        self._maternita = None


    def set_posizione_mil(self, pos: PosizioneMilitare) -> None:
        if not self._genere == Genere.uomo:
            raise RuntimeError("Le donne non hanno la posizione militare!")
        self._posizione_mil = pos

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def cf(self) -> CodiceFiscale:
        return self._cf
    
    def genere(self) -> Genere:
        return self._genere
    
    def maternita(self) -> IntGEZ:
        return self._maternita
    
    def pos_mil(self) -> PosizioneMilitare:
        return self._posizione_mil
    

class Impiegato(Persona):

    _stipendio: RealGEZ
    _ruolo: Ruolo
    _is_responsabile: bool
    _resp_prog: dict['Progetto': 'Resp_prog']
    
    def __init__(self, *, nome: str, cognome: str, cf: list[CodiceFiscale], genere: Genere, maternita: IntGEZ|None=None, 
               pos: PosizioneMilitare|None=None, stipendio: RealGEZ, ruolo: Ruolo) -> None:
        super().__init__(nome = nome, cognome = cognome, cf = cf, genere = genere, maternita = maternita, pos = pos)
        from resp_prog import Resp_Prog
        self.set_stipendio(stipendio)
        self.set_ruolo(ruolo)
        if ruolo == Ruolo.progettista:
            self._is_responsabile = False
        else:
            self._is_responsabile = None
        self._resp_prog = {}

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio

    def set_ruolo(self, ruolo: Ruolo) -> None:
        self._ruolo = ruolo

    def set_responsabile(self, resp: bool) -> None:
        self._is_responsabile = resp

    def stipendio(self) -> RealGEZ:
        return self._stipendio
    
    def ruolo(self) -> Ruolo:
        return self._ruolo
    
    def is_responsabile(self) -> bool:
        return self._is_responsabile
    
    def progetti(self) -> dict['Progetto', 'Resp_Prog']:
        return self._resp_prog
    
    def __repr__(self) -> str:
        return self.nome()

class Studente(Persona):
    _matricola: IntGEZ
    _matricole: set[IntGEZ] = set()
    def __init__(self, *, nome: str, cognome: str, cf: list[CodiceFiscale], genere: Genere, maternita: IntGEZ|None=None, pos: PosizioneMilitare|None=None, matricola: IntGZ) -> None:
        if matricola in self._matricole:
            raise ValueError("Esiste già uno studente con questo numero di matricola!")
        super().__init__(nome, cognome, cf, genere, maternita, pos)
        self._matricola = matricola
        self._matricole.add(matricola)

    def matricola(self) -> IntGEZ:
        return self._matricola

class Progetto:
    _nome: str
    _resp_prog: dict[Impiegato, 'Resp_Prog']
    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self._resp_prog = {}

    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def nome(self) -> str:
        return self._nome
    
    def add_responsabile(self, impiegato: 'Impiegato') -> None:
        from resp_prog import Resp_Prog
        if impiegato.ruolo() != Ruolo.progettista:
            raise ValueError("L'impiegato non è un progettista!")
        if impiegato not in self._resp_prog:
            resp: 'Resp_Prog' = Resp_Prog(self, impiegato)
            self._resp_prog[impiegato] = resp
            impiegato._resp_prog[self] = resp
            impiegato.set_responsabile(True)
        else:
            raise ValueError("L'impiegato è già responsabile del progetto!")
        
    def remove_responsabile(self, impiegato:'Impiegato') -> None:
        if impiegato in self._resp_prog:
            self._resp_prog.pop(impiegato)
            impiegato._resp_prog = None
        else:
            raise ValueError("L'impiegato non è responsabile del progetto!")
        
    def responsabili(self) -> dict['Impiegato', 'Resp_Prog']:
        return self._resp_prog
    
    def __repr__(self) -> str:
        return self.nome()

class PosizioneMilitare:
    _posizioni_militari: set[str] = set()
    _nome: str # <<imm>> 
    
    def __init__(self, nome: str) -> None:
        if nome in PosizioneMilitare._posizioni_militari:
            raise ValueError("Posizione militare già esistente!")
        self._nome = nome
        PosizioneMilitare._posizioni_militari.add(nome)

    def nome(self) -> str:
        return self._nome
    

if __name__ == "__main__":
    print("=== TEST Persona donna ===")
    cf_donna = [CodiceFiscale("RSSMRA85M01H501X")]
    p_donna = Persona(nome="Maria", cognome="Rossi", cf=cf_donna, genere=Genere.donna, maternita=IntGEZ(1))
    print(p_donna.nome(), p_donna.cognome(), p_donna.cf(), p_donna.genere(), p_donna.maternita(), p_donna.pos_mil())

    print("=== TEST Persona uomo ===")
    pos_mil = PosizioneMilitare("Caporale")
    cf_uomo = [CodiceFiscale("BNCLCU85M01H501Y")]
    p_uomo = Persona(nome="Luca", cognome="Bianchi", cf=cf_uomo, genere=Genere.uomo, pos=pos_mil)
    print(p_uomo.nome(), p_uomo.cognome(), p_uomo.cf(), p_uomo.genere(), p_uomo.maternita(), p_uomo.pos_mil())

    print("=== TEST Impiegato ===")
    imp = Impiegato(nome="Giulia", cognome="Verdi", cf=[CodiceFiscale("VRDGLL90A01H501Z")],
                    genere=Genere.donna, maternita=IntGEZ(2), stipendio=RealGEZ(1200.50), ruolo=Ruolo.progettista)
    print(imp.nome(), imp.cognome(), imp.cf(), imp.genere(), imp.maternita(), imp.pos_mil(), imp.stipendio(), imp.ruolo(), imp.is_responsabile())

    print("=== TEST Progetto e Responsabile ===")
    progetto = Progetto("Progetto Alfa")
    print("Nome progetto:", progetto.nome())
    progetto.add_responsabile(imp)
    print("Responsabili:", progetto.responsabili())
    print("Progetti impiegato:", imp.progetti())
    progetto.remove_responsabile(imp)
    print("Responsabili dopo rimozione:", progetto.responsabili())
    print("Progetti impiegato dopo rimozione:", imp.progetti())

    print("=== TEST Studente ===")
    stud = Studente(nome="Marco", cognome="Neri", cf=[CodiceFiscale("NRIMRC92A01H501W")],
                    genere=Genere.uomo, pos=pos_mil, matricola=1001)
    print(stud.nome(), stud.cognome(), stud.cf(), stud.genere(), stud.pos_mil(), stud.matricola())