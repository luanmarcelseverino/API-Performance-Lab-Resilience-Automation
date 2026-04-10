# 🚀 API-Performance-Lab: Resilience & Automation

![Pipeline Status](https://github.com/luanmarcelseverino/API-Performance-Lab-Resilience-Automation/actions/workflows/main.yml/badge.svg)
![K6 Performance](https://github.com/luanmarcelseverino/API-Performance-Lab-Resilience-Automation/actions/workflows/main.yml/badge.svg?job=performance-tests)

Este projeto demonstra uma estratégia completa de testes para APIs de alta criticidade, unindo testes funcionais, validação de contrato e testes de performance (carga e estresse).

### 📊 Relatório de Testes (Allure Report)
Você pode visualizar os resultados detalhados da última execução da pipeline aqui:
👉 **[Visualizar Relatório Online](https://luanmarcelseverino.github.io/API-Performance-Lab-Resilience-Automation/)**

---

## 🛠 Tech Stack
* **Linguagem:** Python
* **Gestão de Dependências:** Poetry
* **Testes Funcionais:** Pytest & Requests
* **Performance:** K6
* **CI/CD:** GitHub Actions

## ⭐ Diferenciais
* **Service Layer:** Abstração de chamadas para alta manutenibilidade.
* **Deterministic Environment:** Gestão rigorosa de dependências via Poetry.
* **Performance Híbrida:** Scripts de carga progressiva (ramping) com K6.
* **Pipeline Integrada:** Execução automática de testes (E2E & Load) via CI/CD.

## 🚀 Como executar
1. Instale as dependências: `poetry install`
2. Rode os testes funcionais: `poetry run pytest`
3. Rode o teste de carga: `k6 run tests/performance/load_test.js`

---
Dúvidas ou sugestões? Conecte-se comigo no LinkedIn: [in/luanmarcelseverino](https://www.linkedin.com/in/luanmarcelseverino/)