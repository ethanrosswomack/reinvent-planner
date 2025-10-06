#!/bin/bash

# Script d'installation pour le serveur MCP re:Invent Planner v3.0

echo "🚀 Installation du serveur MCP re:Invent Planner v3.0..."

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    exit 1
fi

# Créer l'environnement virtuel
echo "📦 Création de l'environnement virtuel..."
python3 -m venv venv

# Activer l'environnement virtuel et installer les dépendances
echo "📥 Installation des dépendances..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Exécuter les tests
echo "🧪 Exécution des tests..."
python -m pytest tests/ -v

echo "✅ Installation terminée !"
echo ""
echo "🛠️ Commandes disponibles :"
echo "  make test          - Exécuter les tests"
echo "  make test-integration - Tests avec APIs externes"
echo "  make clean         - Nettoyer les fichiers temporaires"
echo "  make help          - Voir toutes les commandes"
echo ""
echo "📋 Pour utiliser dans Kiro :"
echo "1. Le fichier .kiro/settings/mcp.json est configuré"
echo "2. Redémarrez Kiro ou reconnectez le serveur MCP"
echo "3. 20 outils MCP disponibles pour re:Invent 2025 !"