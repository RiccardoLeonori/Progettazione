from typing import Any, Self
from mytype import *


class Volo:
    _codice: str #<<immutable>>, noto alla nascita
    _durata_min: IntGZ #noto alla nascita
    _aereoporto_arrivo: Aereoporto #noto alla nascita
    _aereoporto_partenza: Aereoporto #noto alla nascita
    _v_compagnia: Compagnia #noto alla nascita

    def __init__(self, codice: str, durata_min: IntGZ, aereoporto_arrivo: Aereoporto, aereoporto_partenza: Aereoporto, voli_compagnia: Compagnia) -> None:
        self.set_codice(codice)
        self.set_durata_min(durata_min)
        self.set_aereoporto_arrivo(aereoporto_arrivo)
        self.set_aereoporto_partenza(aereoporto_partenza)
        self.set_voli_compagnia(voli_compagnia)

    def codice(self) -> str:
        return self._codice
    
    def durata_min(self) -> IntGZ:
        return self._durata_min
    
    def aereoporto_arrivo(self) -> Aereoporto:
        return self._aereoporto_arrivo
    
    def aereoporto_partenza(self) -> Aereoporto:
        return self._aereoporto_partenza
    
    def voli_compagnia(self) -> Compagnia:
        return self._voli_compagnia

    def set_codice(self, codice: str) -> None:
        self._codice: str = codice

    def set_durata_min(self, durata: IntGZ) -> None:
        self._durata_min: IntGZ = durata

    def set_aereoporto_arrivo(self, aereoporto_arrivo: Aereoporto) -> None:
        self._aereoporto_arrivo: Aereoporto = aereoporto_arrivo

    def set_aereoporto_partenza(self, aereoporto_partenza: Aereoporto) -> None:
        self._aereoporto_partenza: Aereoporto = aereoporto_partenza

    def set_voli_compagnia(self, voli_compagnia: Compagnia) -> None:
        self._voli_compagnia: Compagnia = voli_compagnia


class Compagnia:
    _nome: str #noto alla nascita
    _anno: int #<<immutable>>, noto alla nascita

    def __init__(self, nome: str, anno: int) -> None:
        self._nome = nome
        self._anno = anno

    
    def nome(self) -> str:
        return self._nome
    
    def anno(self) -> int:
        return self._anno
    
    def set_nome(self, nome: str) -> None:
        self._nome: str = nome

    def set_anno(self, anno: int) -> None:
        self._anno: int = anno


class Città:
    _nome: str #noto alla nascita
    _abitanti: IntGZ #noto alla nascita
    _aer_cit:list[Aereoporto] #noto alla nascita

    def __init__(self,*, nome: str, abitanti: IntGZ, aereoport_città: set[Aereoporto]) -> None:
        self.set_nome (nome)
        self.set_abitanti = abitanti
        self._aereoporto_città:list[Aereoporto] = aereoport_città

    def nome(self) -> str:
        return self._nome
    
    def abitanti(self) -> IntGZ:
        return self._abitanti
    
    def set_nome(self, nome: str) -> None:
        self._nome: str = nome

    def set_abitanti(self, a: IntGZ) -> None:
        self._abitanti: IntGZ = a
        
    def aer_cit(self) -> frozenset[Aereoporto]:
        return frozenset(self._aereoporto_città)
    
    def add_aer_cit(self, a: Aereoporto) -> None:
        self._aer_cit.add(a)

    def remove_aer_cit(self, a: Aereoporto) -> None:
        if a:
            self._aer_cit.remove(a)
    
class Aereoporto:
    _codice: str #noto alla nascita
    _nome: str #noto alla nascita
    _città: Città #noto alla nascita

    def __init__(self, nome: str, codice: str, città: Città) -> None:
        self.set_nome(nome)
        self.set_codice(codice)
        self.set_città(città)

    def nome(self) -> str:
        return self._nome

    def codice(self) -> str:
        return self._codice
    
    def città(self) -> Città:
        return self._città

    def set_nome(self, nome: str) -> None:
        self._nome: str = nome

    def set_codice(self, codice: str) -> None:
        self._codice: str = codice

    def set_città(self, città: Città) -> None:
        self._città: Città = città
        


class Nazione:
    _nome: str #noto alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome = nome

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome: str = nome