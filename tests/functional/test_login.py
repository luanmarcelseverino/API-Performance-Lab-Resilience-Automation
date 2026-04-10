import pytest
from services.auth_service import AuthService  # <--- ESSA LINHA É A CHAVE!

def test_login_com_sucesso():
    auth = AuthService()
    response = auth.login("fulano@qa.com", "teste")

    # Verifica se o status é 200 (Sucesso)
    assert response.status_code == 200
    
    # Verifica se a mensagem de sucesso está no JSON da resposta
    assert response.json()["message"] == "Login realizado com sucesso"