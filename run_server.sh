#!/bin/bash

# Script wrapper pour le serveur MCP re:Invent Planner
# Ce script s'assure que l'environnement est correctement configuré

# Aller dans le répertoire du serveur
cd "$(dirname "$0")"

# Activer l'environnement virtuel et lancer le serveur
exec ./venv/bin/python server.py