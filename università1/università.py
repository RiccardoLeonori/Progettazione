from __future__ import annotations

from datetime import date
from typing import List
from mytype import CodiceFiscale, IntG1900, IntGZ, Voto


class Regione:
    def __init__(self, nome: str):
        self.nome = nome
        self.citta: List[Citta] = []

    def aggiungi_citta(self, citta: Citta):
        if citta not in self.citta:
            self.citta.append(citta)
            citta.regione = self

    def __str__(self):
        return f"Regione: {self.nome}"


class Citta:
    def __init__(self, nome: str, regione: Regione | None = None):
        self.nome = nome
        self.regione = regione
        self.studenti: List[Studenti] = []

        if regione:
            regione.aggiungi_citta(self)

    def aggiungi_studente(self, studente: Studenti):
        if studente not in self.studenti:
            self.studenti.append(studente)

    def __str__(self):
        return f"Città: {self.nome}"


class Professori:
    def __init__(self, nome: str, data_nascita: date, cod_fisc: CodiceFiscale):
        self.nome = nome
        self.data_nascita = data_nascita
        self.cod_fisc = cod_fisc
        self.corsi: List[Corsi] = []

    def aggiungi_corso(self, corso: Corsi):
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.professore = self

    def __str__(self):
        return f"Prof. {self.nome} ({self.cod_fisc})"


class Facolta:
    def __init__(self, nome: str, tipo_facolta: str):
        self.nome = nome
        self.tipo_facolta = tipo_facolta
        self.corsi: List[Corsi] = []
        self.studenti: List[Studenti] = []

    def aggiungi_corso(self, corso: Corsi):
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.facolta = self

    def aggiungi_studente(self, studente: Studenti):
        if studente not in self.studenti:
            self.studenti.append(studente)
            studente.facolta = self

    def __str__(self):
        return f"Facoltà di {self.nome} ({self.tipo_facolta})"


class Corsi:
    def __init__(self, nome: str, codice: str, durata_in_ore: IntGZ):
        self.nome = nome
        self.codice = codice
        self.durata_in_ore = durata_in_ore
        self.facolta: Facolta | None = None
        self.professore: Professori | None = None
        self.studenti_superato: List[CorsoSuperatoStudente] = []

    def assegna_professore(self, professore: Professori):
        self.professore = professore
        professore.aggiungi_corso(self)

    def __str__(self):
        return f"Corso: {self.nome} ({self.codice}) - {self.durata_in_ore}h"


class CorsoSuperatoStudente:
    def __init__(self, studente: Studenti, corso: Corsi, voto: Voto):
        self.studente = studente
        self.corso = corso
        self.voto = voto

        studente.corsi_superati.append(self)
        corso.studenti_superato.append(self)

    def __str__(self):
        return f"{self.studente.nome} - {self.corso.nome}: {self.voto.v}"


class Studenti:
    def __init__(self, nome: str, cod_fisc: CodiceFiscale, data_nascita: date, anno_iscr: IntG1900, num_matricola: IntGZ, citta: Citta | None = None):
        self.nome = nome
        self.cod_fisc = cod_fisc
        self.data_nascita = data_nascita
        self.anno_iscr = anno_iscr
        self.num_matricola = num_matricola
        self.citta = citta
        self.facolta: Facolta | None = None
        self.corsi_superati: List[CorsoSuperatoStudente] = []

        if citta:
            citta.aggiungi_studente(self)

    def supera_corso(self, corso: Corsi, voto: int):
        return CorsoSuperatoStudente(self, corso, Voto(voto))

    def calcola_media(self) -> float:
        if not self.corsi_superati:
            return 0.0
        somma_voti = sum(corso.voto.v for corso in self.corsi_superati)
        return somma_voti / len(self.corsi_superati)

    def __str__(self):
        return f"Studente: {self.nome} (Matricola: {self.num_matricola})"


if __name__ == "__main__":
    lombardia = Regione("Lombardia")
    lazio = Regione("Lazio")

    milano = Citta("Milano", lombardia)
    roma = Citta("Roma", lazio)

    ingegneria = Facolta("Ingegneria", "Tecnica")
    lettere = Facolta("Lettere e Filosofia", "Umanistica")

    prof_rossi = Professori("Mario Rossi", date(1970, 5, 15), "RSSMRA70E15F205X")
    prof_bianchi = Professori("Anna Bianchi", date(1965, 3, 22), "BNCNNA65C62F205Y")

    matematica = Corsi("Matematica I", "MAT001", 60)
    fisica = Corsi("Fisica I", "FIS001", 80)
    letteratura = Corsi("Letteratura Italiana", "LET001", 50)

    ingegneria.aggiungi_corso(matematica)
    ingegneria.aggiungi_corso(fisica)
    lettere.aggiungi_corso(letteratura)

    matematica.assegna_professore(prof_rossi)
    fisica.assegna_professore(prof_rossi)
    letteratura.assegna_professore(prof_bianchi)

    studente1 = Studenti("Luca Verdi", "VRDLCU95A01F205Z", date(1995, 1, 1), 2020, 123456, milano)
    studente2 = Studenti("Sara Neri", "NRESRA96B02H501W", date(1996, 2, 2), 2021, 123457, roma)

    ingegneria.aggiungi_studente(studente1)
    lettere.aggiungi_studente(studente2)

    studente1.supera_corso(matematica, 28.0)
    studente1.supera_corso(fisica, 25.0)
    studente2.supera_corso(letteratura, 30.0)

    print("REGIONI E CITTÀ:")
    for regione in [lombardia, lazio]:
        print(f"{regione}")
        for citta in regione.citta:
            print(f"{citta}")

    print("\nFACOLTÀ:")
    for facolta in [ingegneria, lettere]:
        print(f"{facolta}")
        print(f"Corsi: {len(facolta.corsi)}")
        print(f"Studenti iscritti: {len(facolta.studenti)}")

    print("\nSTUDENTI:")
    for studente in [studente1, studente2]:
        print(f"{studente}")
        print(f"Città: {studente.citta}")
        print(f"Facoltà: {studente.facolta.nome}")
        print(f"Media voti: {studente.calcola_media():.2f}")
        print(f"Esami superati: {len(studente.corsi_superati)}")