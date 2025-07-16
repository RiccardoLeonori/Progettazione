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