def test_crea_tablas_y_persiste_relacion(conexion):
    tablas = {fila["name"] for fila in conexion.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    assert {"materias", "tareas"}.issubset(tablas)

    conexion.execute("INSERT INTO materias (nombre, nombre_normalizado, color) VALUES (?, ?, ?)", ("Cálculo", "cálculo", "#123456"))
    materia_id = conexion.execute("SELECT id FROM materias").fetchone()["id"]
    conexion.execute("INSERT INTO tareas (materia_id, titulo, fecha_entrega) VALUES (?, ?, ?)", (materia_id, "Parcial", "2026-11-01T10:00:00"))
    conexion.commit()
    assert conexion.execute("SELECT COUNT(*) AS total FROM tareas").fetchone()["total"] == 1


def test_borrado_de_materia_aplica_cascada(conexion):
    conexion.execute("INSERT INTO materias (nombre, nombre_normalizado, color) VALUES (?, ?, ?)", ("Cálculo", "cálculo", "#123456"))
    materia_id = conexion.execute("SELECT id FROM materias").fetchone()["id"]
    conexion.execute("INSERT INTO tareas (materia_id, titulo, fecha_entrega) VALUES (?, ?, ?)", (materia_id, "Parcial", "2026-11-01T10:00:00"))
    conexion.commit()
    conexion.execute("DELETE FROM materias WHERE id = ?", (materia_id,))
    conexion.commit()
    assert conexion.execute("SELECT COUNT(*) AS total FROM tareas").fetchone()["total"] == 0
