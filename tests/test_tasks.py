import unittest
from tasks import agregar_tarea, completar_tarea, pendientes, filtrar_tareas, listar_categorias


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertFalse(tarea["completada"])
        self.assertEqual(tarea["categoria"], "General")

    def test_agregar_tarea_con_categoria(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Estudiar Python", "Trabajo")
        self.assertEqual(tarea["categoria"], "Trabajo")

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_filtrar_por_categoria(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Trabajo")
        agregar_tarea(tareas, "Comprar pan", "Personal")

        filtradas = filtrar_tareas(tareas, categoria="Trabajo")

        self.assertEqual(len(filtradas), 1)
        self.assertEqual(filtradas[0]["titulo"], "Leer documentación")

    def test_listar_categorias(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Trabajo")
        agregar_tarea(tareas, "Comprar pan", "Personal")
        agregar_tarea(tareas, "Organizar escritorio")

        self.assertEqual(listar_categorias(tareas), ["Trabajo", "Personal", "General"])


if __name__ == "__main__":
    unittest.main()
