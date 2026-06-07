from src.linked_list import LinkedList

ll = LinkedList()

# append
ll.append(10)
ll.append(20)
ll.append(30)
print("Después de append:", ll)          # 10 -> 20 -> 30

# search
nodo = ll.search(20)
print("Buscar 20:", nodo)                # Node(20)
print("Buscar 99:", ll.search(99))       # None

# delete
ll.delete(20)
print("Después de delete(20):", ll)      # 10 -> 30
print("Largo final:", len(ll))           # 2