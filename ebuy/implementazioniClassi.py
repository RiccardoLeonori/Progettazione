from datetime import datetime
from custom_types import *

class Utente:

    _username: str # <<imm>>
    _registrazione: datetime # <<imm>>

    def __init__(self, username: str, registrazione: str):
        self.username = username
        self.registrazione = registrazione



class UtentePrivato(Utente):

    def __init__(self):
        super().__init__()


class Bid:

    _istante : datetime # <<imm>>

    def __init__(self, istante: datetime):
        self._istante = istante

class Asta:

    _prezzo_bid: RealGEZ
    _scadenza: datetime


class Asta_bid:
    pass

class Bid_ut:
    pass