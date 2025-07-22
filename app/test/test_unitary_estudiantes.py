from unittest.mock import MagicMock, patch
import pytest # type: ignore
import app.services.estudiantes as estudiantes_service

# Dummy clases para simular datos
class DummyEstudianteCreate:
    def dict(self):
        return {
            "id_usuario": 1,
            "id_acudiente": 2,
            "fecha_nacimiento": "2010-05-10",
            "id_curso": 3,
            "estado_matricula": "matriculado",
            "sede": "Principal"
        }

class DummyEstudiante:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

@pytest.fixture
def mock_db():
    return MagicMock()

def test_create_estudiante(mock_db):
    estudiante_create = DummyEstudianteCreate()
    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    with patch('app.services.estudiantes.Estudiante', return_value=DummyEstudiante(id_estudiante=1)):
        result = estudiantes_service.create_estudiante(mock_db, estudiante_create) # type: ignore

    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()
    assert hasattr(result, 'id_estudiante')

def test_get_estudiante_found(mock_db):
    dummy_estudiante = DummyEstudiante(id_estudiante=1)
    mock_db.query.return_value.filter.return_value.first.return_value = dummy_estudiante

    result = estudiantes_service.get_estudiante(mock_db, 1)
    assert result == dummy_estudiante

def test_get_estudiante_not_found(mock_db):
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = estudiantes_service.get_estudiante(mock_db, 999)
    assert result is None

def test_list_estudiantes(mock_db):
    dummy_list = [DummyEstudiante(id_estudiante=1), DummyEstudiante(id_estudiante=2)]
    mock_db.query.return_value.all.return_value = dummy_list

    result = estudiantes_service.list_estudiantes(mock_db)
    assert result == dummy_list

def test_list_estudiantes_by_acudiente(mock_db):
    dummy_list = [DummyEstudiante(id_estudiante=1, id_acudiente=2), DummyEstudiante(id_estudiante=2, id_acudiente=2)]
    mock_db.query.return_value.filter.return_value.all.return_value = dummy_list

    result = estudiantes_service.list_estudiantes_by_acudiente(mock_db, 2)
    assert result == dummy_list

def test_list_estudiantes_by_curso(mock_db):
    dummy_list = [DummyEstudiante(id_estudiante=1, id_curso=3), DummyEstudiante(id_estudiante=2, id_curso=3)]
    mock_db.query.return_value.filter.return_value.all.return_value = dummy_list

    result = estudiantes_service.list_estudiantes_by_curso(mock_db, 3)
    assert result == dummy_list

@patch('app.services.estudiantes.requests.get')
def test_list_estudiantes_by_asignatura_success(mock_requests_get, mock_db):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"id_curso": 1, "id_asignatura": 10},
        {"id_curso": 2, "id_asignatura": 10},
        {"id_curso": 3, "id_asignatura": 20}
    ]
    mock_requests_get.return_value = mock_response

    dummy_list = [DummyEstudiante(id_estudiante=1, id_curso=1), DummyEstudiante(id_estudiante=2, id_curso=2)]
    mock_db.query.return_value.filter.return_value.all.return_value = dummy_list

    result = estudiantes_service.list_estudiantes_by_asignatura(mock_db, 10)
    assert result == dummy_list

@patch('app.services.estudiantes.requests.get')
def test_list_estudiantes_by_asignatura_no_courses(mock_requests_get, mock_db):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id_curso": 1, "id_asignatura": 20}]
    mock_requests_get.return_value = mock_response

    result = estudiantes_service.list_estudiantes_by_asignatura(mock_db, 10)
    assert result == []

@patch('app.services.estudiantes.requests.get')
def test_list_estudiantes_by_asignatura_api_error(mock_requests_get, mock_db):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_requests_get.return_value = mock_response

    result = estudiantes_service.list_estudiantes_by_asignatura(mock_db, 10)
    assert result == []

@patch('app.services.estudiantes.requests.get')
def test_list_estudiantes_by_asignatura_exception(mock_requests_get, mock_db):
    mock_requests_get.side_effect = Exception("API failure")

    result = estudiantes_service.list_estudiantes_by_asignatura(mock_db, 10)
    assert result == []
