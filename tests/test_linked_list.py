# tests/test_linked_list.py
# Pruebas base escritas por el docente.
# CADA EQUIPO agregará sus propias pruebas en este archivo
# desde su rama — esto generará merge conflicts intencionales.

import pytest
from src.linked_list import LinkedList, Node


# ------------------------------------------------------------------ #
# Pruebas del docente — __str__ y __len__                             #
# ------------------------------------------------------------------ #

def test_lista_vacia_str():
    ll = LinkedList()
    assert str(ll) == "Lista vacía"


def test_lista_vacia_len():
    ll = LinkedList()
    assert len(ll) == 0


def test_node_repr():
    n = Node(42)
    assert repr(n) == "Node(42)"
    
# ------------------------------------------------------------------ #
# Pruebas de Búsqueda — Equipo C: rama feature/search                 #
# ------------------------------------------------------------------ #

def hacer_lista(*valores):
    """
    Función auxiliar: crea una lista enlazada a mano,
    sin depender de append (que aún no está implementado).
    """
    ll = LinkedList()
    if not valores:
        return ll
    nodos = [Node(v) for v in valores]
    for i in range(len(nodos) - 1):
        nodos[i].next = nodos[i + 1]
    ll.head = nodos[0]
    return ll


def test_search_elemento_en_el_medio():
    """Buscar un valor que está en el medio de la lista."""
    ll = hacer_lista(10, 20, 30)
    resultado = ll.search(20)
    assert resultado is not None
    assert resultado.data == 20


def test_search_primer_elemento():
    """Buscar el primer elemento (la cabeza de la lista)."""
    ll = hacer_lista(10, 20, 30)
    resultado = ll.search(10)
    assert resultado is not None
    assert resultado.data == 10


def test_search_ultimo_elemento():
    """Buscar el último elemento de la lista."""
    ll = hacer_lista(10, 20, 30)
    resultado = ll.search(30)
    assert resultado is not None
    assert resultado.data == 30


def test_search_elemento_no_existe():
    """Buscar un valor que NO está en la lista — debe retornar None."""
    ll = hacer_lista(10, 20, 30)
    resultado = ll.search(99)
    assert resultado is None


def test_search_lista_vacia():
    """Buscar en una lista vacía — debe retornar None."""
    ll = LinkedList()
    resultado = ll.search(5)
    assert resultado is None


def test_search_retorna_el_nodo_correcto():
    """Verificar que retorna el nodo exacto, no solo cualquier nodo."""
    ll = hacer_lista(10, 20, 30)
    resultado = ll.search(30)
    assert resultado is not None
    assert resultado.data == 30
    assert resultado.next is None   # el último nodo no apunta a nada