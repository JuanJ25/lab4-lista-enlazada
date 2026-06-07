class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.head is None:
            return "Lista vacía"
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

    def append(self, data):
        """Agrega un elemento al final de la lista."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete(self, data):
        if self.head is None:
            return False
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

    # ------------------------------------------------------------------ #
    # TODO — Equipo C: rama feature/search                                #
    # ------------------------------------------------------------------ #
        """Elimina la primera ocurrencia de un elemento."""
        pass

    def search(self, data):
            """Busca un valor en la lista.

            Args:
                data: El valor a buscar.

            Returns:
                El nodo que contiene data, o None si no existe.
            """
            current = self.head

            while current is not None:
                if current.data == data:
                    return current
                current = current.next

            return None
