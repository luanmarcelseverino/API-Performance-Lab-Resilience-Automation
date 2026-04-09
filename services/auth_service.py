import requests

class AuthService:
    def __init__(self):
        self.url = "https://serverest.dev"

    def login(self, email, password):
        payload = {"email": email, "password": password}
        return requests.post(f"{self.url}/login", json=payload)