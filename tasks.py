def _normalizar_categoria(categoria):
    if categoria is None:
        return "General"
    categoria = str(categoria).strip()
    return categoria if categoria else "General"


def agregar_tarea(tareas, titulo, categoria=None):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")

    categoria = _normalizar_categoria(categoria)
    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "completada": False,
        "categoria": categoria,
    }
    tareas.append(tarea)
    return tarea


def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")


def filtrar_tareas(tareas, categoria=None, completadas=None):
    filtradas = []
    for tarea in tareas:
        if categoria is not None:
            categoria_actual = _normalizar_categoria(tarea.get("categoria"))
            categoria_objetivo = _normalizar_categoria(categoria)
            if categoria_actual.lower() != categoria_objetivo.lower():
                continue

        if completadas is not None:
            if bool(tarea.get("completada", False)) != bool(completadas):
                continue

        filtradas.append(tarea)

    return filtradas


def filtrar_por_categoria(tareas, categoria):
    return filtrar_tareas(tareas, categoria=categoria)


def tareas_por_categoria(tareas, categoria):
    return filtrar_por_categoria(tareas, categoria)


def pendientes(tareas, categoria=None):
    return filtrar_tareas(tareas, categoria=categoria, completadas=False)


def listar_categorias(tareas):
    categorias = []
    for tarea in tareas:
        categoria = _normalizar_categoria(tarea.get("categoria"))
        if categoria not in categorias:
            categorias.append(categoria)
    return categorias
