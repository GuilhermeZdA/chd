from pathlib import Path

CAMINHO_RAIZ = Path(__file__).resolve().parent

CAMINHO_DATABASE = CAMINHO_RAIZ / "database"
JSON_CONSULTAS = CAMINHO_DATABASE / "consultas.json"
JSON_MEDICOS = CAMINHO_DATABASE / "medicos.json"
JSON_PACIENTES = CAMINHO_DATABASE / "pacientes.json"
JSON_BLOQUEIOS = CAMINHO_DATABASE / "bloqueios_agenda.json"