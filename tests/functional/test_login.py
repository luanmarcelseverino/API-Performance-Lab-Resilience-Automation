from services.auth_service import AuthService

def test_login_com_sucesso():
    auth = AuthService()
    response = auth.login("fulano@qa.com", "teste")
    
    assert response.status_code == 200
    assert response.json()["message"] == "Login realizado com sucesso"
    assert "authorization" in response.headers