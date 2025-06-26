from __future__ import annotations
from custom_types import *
from datetime import date
from impiegato import Impiegato
from dipartimento import Dipartimento
from coinvolto import Coinvolto
from progetto import Progetto

tel1: Telefono = Telefono("3334445566")
tel2: Telefono = Telefono("3337778899")
ind: Indirizzo = Indirizzo("Viale Cesare Pavese", "205b",
                           CAP("00144"))

alice: Impiegato = Impiegato("Alice", "Alessi",
                             date(year=1990, month=12, day=31),
                             RealGEZ(18000))
print(f"Ho creato l'impiegata {alice.nome()} {alice.cognome()}")

bob: Impiegato = Impiegato("Bob", "Burnham",
                             date(year=1997, month=10, day=11),
                             RealGEZ(19000))
print(f"Ho creato l'impiegato {bob.nome()} {bob.cognome()}")

valerio: Impiegato = Impiegato("Valerio", "Valeri", date.today(), RealGEZ(1000))

mario: Impiegato = Impiegato("Mario", "Rossi", date.today(), RealGEZ(2000))

p1: Progetto = Progetto("Ciao", RealGEZ(146))
p2: Progetto = Progetto("boh", RealGEZ(34856))


dip1: Dipartimento = Dipartimento("Vendite", tel1, ind, alice)

print(f"Ho creato il dipartimento {dip1}")


dip2: Dipartimento = Dipartimento("Acquisti", tel2, None, bob)
print(f"Ho creato il dipartimento {dip2}")

t: frozenset[Telefono] = dip1.telefoni()

print("dip1.telefoni() = " + str(dip1.telefoni()))

dip1.add_telefono(Telefono("3481265413"))

print("dip1.telefoni() = " + str(dip1.telefoni()))

print("progetti alice: ", alice._progetti)

p1.add_impiegato(alice)

print("progetti alice: ", alice._progetti)

p1.remove_impiegati(alice)

print("progetti alice: ", alice._progetti)

print(dip1._direttore[1].impiegato(),dip1._direttore[1].dipartimento())

dip1.add_impiegato(bob, date.today())
print(dip1.impiegati())
print(bob.dipartimento())
dip1.remove_impiegati(bob)
print(dip1.impiegati())
print(bob.dipartimento())

print("\n\n\n")
print(dip1.direttore())
print(alice.dirige())
print(bob.dirige())

dip1.set_direttore(bob)
print(dip1.direttore())
print(alice.dirige())
print(bob.dirige())