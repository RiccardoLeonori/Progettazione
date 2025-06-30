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
                 maternita: IntGEZ|None=None) -> None:
        self._nome = nome
        self._cognome = cognome
        if not cf:
            raise ValueError("La persona deve avere almeno un codice fiscale!")

        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("È obbligatorio fornire il numero di maternità per le donne")
            self.diventa_donna(maternita)

    def diventa_donna(self, maternita: IntGEZ) -> None:
        if self._genere == Genere.donna:
            raise RuntimeError("La persona era già una donna!")
        self._genere = Genere.donna
        self.set_maternita(maternita)
        self.__dimentica_uomo()

    def __dimentica_uomo(self) -> None:
        # Questo metodo è privato perché non deve essere mai invocato dall'esterno, ma solo all'interno di questa classe
        self._posizione_mil = None

    def set_maternita(self, maternita: IntGEZ) -> None:
        if not self._genere == Genere.donna:
            raise RuntimeError("Gli uomini non hanno il numero di maternità!")

    def __dimentica_donna(self) -> None:
        self._maternita = None

    def set_posizione_mil(self, pos: PosizioneMilitare) -> None:
        if not self._genere == Genere.uomo:
            raise RuntimeError("Le donne non hanno la posizione militare!")
        self._posizione_mil = pos

    def diventa_uomo(self, pos: PosizioneMilitare) -> None:
        if self._genere == Genere.uomo:
            raise RuntimeError("La persona era già un uomo!")
        self._genere = Genere.uomo
        self.set_posizione_mil(pos)
        self.__dimentica_donna()

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
    _resp_progetto: dict['Progetto': 'Resp_progetto']
    
    def __init__(self, *, nome: str, cognome: str, cf: list[CodiceFiscale], genere: Genere, maternita: IntGEZ|None=None, 
               posizione: PosizioneMilitare|None=None, stipendio: RealGEZ, ruolo: Ruolo) -> None:
        super().__init__(nome = nome, cognome = cognome, cf = cf, genere = genere, maternita = maternita, posizione = posizione)
        from impiegati_e_studenti.resp_progetto import Resp_Progetto
        self.set_stipendio(stipendio)
        self.set_ruolo(ruolo)
        if ruolo == Ruolo.progettista:
            self._is_responsabile = False
        else:
            self._is_responsabile = None
        self._resp_progetto = {}

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio

    def set_ruolo(self, ruolo: Ruolo) -> None:
        self._ruolo = ruolo

    def set_responsabile(self, responsabile: bool) -> None:
        self._is_responsabile = responsabile

    def stipendio(self) -> RealGEZ:
        return self._stipendio
    
    def ruolo(self) -> Ruolo:
        return self._ruolo
    
    def is_responsabile(self) -> bool:
        return self._is_responsabile
    
    def progetti(self) -> dict['Progetto', 'Resp_Progetto']:
        return self._resp_progetto
    
    def __repr__(self) -> str:
        return self.nome()

class Studente(Persona):
    _matricola: IntGEZ
    _matricole: set[IntGEZ] = set()
    def __init__(self, *, nome: str, cognome: str, 
                 cf: list[CodiceFiscale], genere: Genere, 
                 maternita: IntGEZ|None=None, 
                 posizione: PosizioneMilitare|None=None, 
                 matricola: IntGEZ) -> None:
        if matricola in self._matricole:
            raise ValueError("Esiste già questa matricola!")
        super().__init__(nome, cognome, cf, genere, maternita, posizione)
        self._matricola = matricola
        self._matricole.add(matricola)

    def matricola(self) -> IntGEZ:
        return self._matricola

class Progetto:
    _resp_progetto: str
    
    def __init__(self, nome: str) -> None:
        self._resp_progetto_ = nome

    def set_resp_progetto(self, nome: str) -> None:
        if self._resp_progetto != None:
            raise ValueError("Esiste già un capo progetto")
        self._resp_progetto = nome
        
    def remove_resp_progetto(self, nome: str) -> None:
        if self._resp_progetto == None:
            raise ValueError("Non esiste un capo progetto")
        self._resp_progetto = None

    def responsabile(self) -> str:
        return self._resp_progetto

class PosizioneMilitare:
    _posizioni_militari: set[str] = set()
    _nome: str
    
    def __init__(self, nome: str) -> None:
        if nome in PosizioneMilitare._posizioni_militari:
            raise ValueError("La posizione militare esiste già!")
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

    print("=== TEST Studente ===")
    stud = Studente(nome="Marco", cognome="Neri", cf=[CodiceFiscale("NRIMRC92A01H501W")],
                    genere=Genere.uomo, pos=pos_mil, matricola=1001)
    print(stud.nome(), stud.cognome(), stud.cf(), stud.genere(), stud.pos_mil(), stud.matricola())