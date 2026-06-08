# lab4-lista-enlazada

Actividad de desarrollo colaborativo de una lista enlazada simple en Python. Cada equipo trabajó en una rama independiente (`feature/append`, `feature/delete`, `feature/search`) e integró su contribución mediante pull requests.

## Trabajo colaborativo

| Método | Responsable |
| --- | --- |
| `append()` | Juan José Paternina |
| `delete()` | Esteban Luna Seña |
| `search()` | Elena Vargas Grisales |

## Implementación

`src/linked_list.py` define dos clases:

- **`Node`**: nodo básico con atributos `data` y `next`.
- **`LinkedList`**: lista enlazada simple con un puntero `head` y contador `size`. Ofrece recorrido lineal para todas las operaciones; no usa índices ni estructuras auxiliares.

## Tests

Los tests en `tests/test_linked_list.py` están organizados por equipo. Los tests de `search` construyen la lista manualmente (sin depender de `append`) para aislar la funcionalidad bajo prueba. Los tests de `delete` y `append` usan ambos métodos de forma integrada.

## Estructura

```text
src/linked_list.py   # Implementación: Node y LinkedList
tests/               # Pruebas unitarias por equipo
```

## Métodos implementados

| Método | Descripción |
| --- | --- |
| `append(data)` | Agrega un elemento al final |
| `delete(data)` | Elimina la primera ocurrencia de un elemento |
| `search(data)` | Busca un elemento y retorna el nodo, o `None` |
| `__len__()` | Retorna el número de elementos |
| `__str__()` | Representación legible de la lista |

## Ejecutar tests

```bash
pip install -r requirements.txt
pytest
```
