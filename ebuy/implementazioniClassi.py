from datetime import datetime, timedelta
from custom_types import *
from typing import List, Optional, Set

class Utente:

    _username: str # <<imm>>
    _registrazione: datetime # <<imm>>

    def __init__(self, username: str, registrazione: datetime):
        self.username = username
        self.registrazione = registrazione
        self.bid_effettuate: List['Bid'] = []
        self.post_aste: List['Asta'] = []
        self.post_bid: List['Bid'] = []
        self.post_pubblicati: List['PostOggetto'] = []
        self.post_feedback: List['PostConFeedback'] = []

    def popolarita(self, i: datetime) -> float:

        P = self.post_pubblicati

        start_time = i - timedelta(days=12)

        Ucs_set: Set[UtentePrivato] = set()
        for p in P:
            for (u, cs_istante) in getattr(p, 'cs_utenti', []):
                if start_time <= cs_istante <= i:
                    Ucs_set.add(u)

        Ua_set: Set[UtentePrivato] = set()
        for p in P:
            for asta_bid in getattr(p, 'asta_bid', []):  # lista di Bid collegati a p
                b = asta_bid
                if start_time <= b.istante <= i:
                    Ua_set.add(b.utente)

        result = len(Ucs_set) + len(Ua_set)
        return result
        

    def affidabilita(self, i: datetime) -> float:

        PF = [pf for pf in self.post_feedback if pf.istante <= i]

        if not PF:
            raise ValueError("Precondizione non soddisfatta: PF deve avere almeno un elemento")

        S = sum(pf.voto for pf in PF)
        FT = len(PF)
        m = S / FT
        PFN = [pf for pf in PF if pf.voto <= 2]
        FN = len(PFN)
        z = FN / FT

        result = (m * (1 - z)) / 5.0
        # Clip tra 0 e 1 per sicurezza
        return max(0.0, min(1.0, result))

        
    
class UtentePrivato(Utente):
    def __init__(self, username: str, registrazione: datetime):
        super().__init__(username, registrazione)

class Bid:

    _istante : datetime # <<imm>>

    def __init__(self, id_bid: int, istante: datetime, utente: 'Utente'):
        self.id = id_bid
        self.istante = istante
        self.utente = utente  # relazione bid_ut
        utente.bid_effettuate.append(self)

class Asta:

    _prezzo_bid: RealGEZ
    _scadenza: datetime

    def __init__(self, id_asta: int, prezzo_bid: float, scadenza: datetime, creatore: 'Utente'):
        self.id = id_asta
        self.prezzo_bid = prezzo_bid
        self.scadenza = scadenza
        self.creatore = creatore  # relazione 1..1 creatore
        self.vincitore: Optional[Utente] = None
        self.ultimo_bid: Optional[Bid] = None
        self.finita: bool = False
        self.bid_list: List[Bid] = []  # relazione asta_bid
        creatore.post_aste.append(self)

    def aggiungi_bid(self, bid: Bid):
        self.bid_list.append(bid)
        self.ultimo_bid = bid