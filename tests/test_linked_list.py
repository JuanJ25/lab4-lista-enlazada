import pytest
from src.linked_list import LinkedList, Node

# ------------------------------------------------------------------ #
# Pruebas del docente — __str__ y __len__                              #
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

# ------------------------------------------------------------------ #
# Pruebas Equipo B — delete                                           #
# ------------------------------------------------------------------ #

def test_delete_elemento_existente():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    resultado = ll.delete(2)
    assert resultado is True
    assert str(ll) == "1 -> 3"
    assert len(ll) == 2
    
def test_delete_head():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.delete(10)
    assert ll.head.data == 20

def test_delete_elemento_inexistente():
    ll = LinkedList()
    ll.append(5)
    resultado = ll.delete(99)
    assert resultado is False
    assert len(ll) == 1

def test_delete_lista_vacia():
    ll = LinkedList()
    assert ll.delete(1) is False
    assert str(ll) == "Lista vacía"
    assert len(ll) == 0


# ------------------------------------------------------------------ #
# Pruebas del Equipo A - Rama: feature/append                        #
# ------------------------------------------------------------------ #

def test_append_un_elemento():
    ll = LinkedList()
    ll.append(10)
    assert ll.head is not None
    assert ll.head.data == 10
    assert len(ll) == 1


def test_append_varios_elementos():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    resultado = ll.delete(2)
    assert resultado is True
    assert str(ll) == "1 -> 3"


def test_append_orden_preservado():
    ll = LinkedList()
    for v in [5, 10, 15]:
        ll.append(v)
    current = ll.head
    for expected in [5, 10, 15]:
        assert current.data == expected
        current = current.next
