# laboratorio-agente-cloud

Gestor de tareas sencillo escrito en Python, sin dependencias externas.

## Funcionalidades

- **Agregar tareas** con un título obligatorio. Los espacios al inicio y al final se eliminan, y un título vacío produce un error.
- **Completar tareas** por su ID.
- **Listar tareas pendientes**, es decir, las que no han sido completadas.

## Estructura

```
laboratorio-agente-cloud/
├── README.md
├── tasks.py            # Lógica principal de las tareas
├── app.py              # Ejemplo de uso por consola
└── tests/
    └── test_tasks.py   # Pruebas unitarias
```

## Requisitos

- Python 3.8 o superior
- No requiere instalar paquetes adicionales

## Uso

Desde la raíz del repositorio:

```bash
python app.py
```

Salida esperada:

```
- 2: Preparar laboratorio
```

### Uso desde código

```python
from tasks import agregar_tarea, completar_tarea, pendientes

tareas = []
agregar_tarea(tareas, "Comprar materiales")
agregar_tarea(tareas, "Enviar informe")
completar_tarea(tareas, 1)

print(pendientes(tareas))
# [{'id': 2, 'titulo': 'Enviar informe', 'completada': False}]
```

## API

| Función | Descripción | Errores |
|---|---|---|
| `agregar_tarea(tareas, titulo)` | Crea una tarea, la agrega a la lista y la retorna. | `ValueError` si el título está vacío. |
| `completar_tarea(tareas, tarea_id)` | Marca como completada la tarea con ese ID y la retorna. | `ValueError` si no existe la tarea. |
| `pendientes(tareas)` | Retorna una lista con las tareas no completadas. | — |

Cada tarea es un diccionario con este formato:

```python
{"id": 1, "titulo": "Ejemplo", "completada": False}
```

## Validaciones

- El título de una tarea no puede estar vacío ni contener solo espacios.
- Solo se pueden completar tareas que existan en la lista.

## Pruebas

Ejecute las pruebas desde la raíz del repositorio:

```bash
python -m unittest discover -s tests
```

Las pruebas actuales verifican que:

- Una tarea nueva se crea con el título correcto y sin completar.
- Una tarea completada ya no aparece en la lista de pendientes.
