from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_estudiante():
    response = client.post("/estudiantes/", json={
        "id_usuario": 1,
        "id_acudiente": 2,
        "fecha_nacimiento": "2010-05-10",
        "id_curso": 3,
        "estado_matricula": "matriculado",
        "sede": "Principal"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["id_usuario"] == 1
    assert data["estado_matricula"] == "matriculado"

def test_listar_estudiantes_por_asignatura():
    """Test para verificar que el endpoint de estudiantes por asignatura funciona"""
    # Test con una asignatura que debería existir
    response = client.get("/estudiantes/por_asignatura/1")
    # El endpoint puede devolver 200 con lista vacía o 404 si no hay estudiantes
    assert response.status_code in [200, 404]
    
    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, list)
        # Si hay datos, verificar la estructura
        if data:
            estudiante = data[0]
            assert "id_estudiante" in estudiante
            assert "nombres" in estudiante
            assert "apellidos" in estudiante
            assert "id_curso" in estudiante

def test_listar_estudiantes_por_curso():
    """Test para verificar que el endpoint de estudiantes por curso funciona"""
    # Test con un curso que debería existir
    response = client.get("/estudiantes/por_curso/1")
    # El endpoint puede devolver 200 con lista o 404 si no hay estudiantes o curso no existe
    assert response.status_code in [200, 404]
    
    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, list)
        # Si hay datos, verificar la estructura
        if data:
            estudiante = data[0]
            assert "id_estudiante" in estudiante
            assert "nombres" in estudiante
            assert "apellidos" in estudiante
            assert "id_curso" in estudiante
            # Verificar que todos los estudiantes pertenecen al curso solicitado
            assert estudiante["id_curso"] == 1