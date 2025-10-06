.PHONY: help install test test-integration clean lint format

help: ## Afficher l'aide
	@echo "Commandes disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Installer les dépendances
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

test: ## Exécuter les tests unitaires
	. venv/bin/activate && python -m pytest tests/ -v

test-integration: ## Exécuter tous les tests (unitaires + intégration)
	. venv/bin/activate && python -m pytest tests/ -v --integration

clean: ## Nettoyer les fichiers temporaires
	rm -rf __pycache__/
	rm -rf tests/__pycache__/
	rm -rf .pytest_cache/
	rm -f *.ics
	rm -f *.db
	rm -f *.log

lint: ## Vérifier le code avec flake8
	. venv/bin/activate && python -m flake8 server.py tests/ --max-line-length=120

format: ## Formater le code avec black
	. venv/bin/activate && python -m black server.py tests/ --line-length=120

run-server: ## Démarrer le serveur MCP
	. venv/bin/activate && python server.py

demo: ## Exécuter une démonstration rapide
	. venv/bin/activate && python -c "import asyncio; from server import ReinventPlannerServer; asyncio.run(ReinventPlannerServer().sync_all_data())"