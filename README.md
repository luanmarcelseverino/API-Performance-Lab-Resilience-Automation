# API-Performance-Lab: Resilience & Automation

Este projeto demonstra uma estratégia completa de testes para APIs de alta criticidade, unindo testes funcionais, validação de contrato e testes de performance (carga e estresse).

## 🛠 Tech Stack
* **Linguagem:** Python
* **Gestão de Dependências:** Poetry
* **Testes Funcionais:** Pytest & Requests
* **Performance:** K6 
* **CI/CD:** GitHub Actions

## 🌟 Diferenciais
* **Service Layer:** Abstração de chamadas para alta manutenibilidade.
* **Deterministic Environment:** Gestão rigorosa de dependências via Poetry.
* **Performance Híbrida:** Scripts de carga progressiva (ramping) com K6.
* **Pipeline Integrada:** Execução automática de testes (E2E & Load) via CI/CD.

## 🚀 Como executar
1. Instale as dependências: `poetry install`
2. Rode os testes funcionais: `poetry run pytest`
3. Rode o teste de carga: `k6 run tests/performance/load_test.js`

Dúvidas ou sugestões? Conecte-se comigo no LinkedIn https://www.linkedin.com/in/luanmarcelseverino/