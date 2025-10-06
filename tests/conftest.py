"""
Configuration pytest pour les tests du serveur MCP re:Invent Planner
"""

import pytest

def pytest_configure(config):
    """Configuration des markers pytest"""
    config.addinivalue_line(
        "markers", "integration: marque les tests d'intégration nécessitant une connexion internet"
    )

def pytest_collection_modifyitems(config, items):
    """Modifier la collection de tests"""
    if config.getoption("--integration"):
        # Si --integration est spécifié, exécuter tous les tests
        return
    
    # Sinon, ignorer les tests d'intégration par défaut
    skip_integration = pytest.mark.skip(reason="Tests d'intégration ignorés (utilisez --integration pour les exécuter)")
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_integration)

def pytest_addoption(parser):
    """Ajouter des options de ligne de commande"""
    parser.addoption(
        "--integration",
        action="store_true",
        default=False,
        help="Exécuter les tests d'intégration"
    )