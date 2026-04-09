def test_login_com_sucesso():
    auth = AuthService()
    response = auth.login("fulano@qa.com", "teste")

    # Verifica se o status é 200 (Sucesso)
    assert response.status_code == 200
    
    # Verifica se a mensagem de sucesso está no JSON
    assert response.json()["message"] == "Login realizado com sucesso"
    
    # OPCIONAL: Se a API mandar o token no corpo, você pode validar assim:
    # assert "token" in response.json()
    