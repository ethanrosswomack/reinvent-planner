# Structure du projet re:Invent Planner MCP Server v3.0

```text
reinvent-planner/
├── server.py                    # Serveur MCP principal avec 20 outils
├── requirements.txt             # Dépendances Python
├── README.md                   # Documentation principale
├── PROJECT_SUMMARY.md          # Résumé du projet
├── config.json                 # Configuration et métadonnées
├── install.sh                  # Script d'installation automatique
├── run_server.sh               # Script de démarrage du serveur
├── Makefile                    # Tâches de développement
├── pytest.ini                 # Configuration pytest
├── .gitignore                  # Fichiers ignorés par Git
├── reinvent_data.db           # Base SQLite (créée automatiquement)
├── venv/                      # Environnement virtuel Python
├── docs/                      # Documentation
│   ├── STRUCTURE.md           # Ce fichier
│   ├── examples.md            # Exemples d'utilisation détaillés
│   └── CHANGELOG.md           # Historique des versions
├── tests/                     # Tests automatisés
│   ├── __init__.py
│   ├── conftest.py            # Configuration pytest
│   ├── test_server.py         # Tests unitaires (8 tests)
│   └── test_integration.py    # Tests d'intégration (4 tests)
├── generated-docs/            # Documentation générée
│   └── repomix_output.xml
└── .git/                      # Dépôt Git

Configuration MCP:
../.kiro/settings/mcp.json      # Configuration pour Kiro
```

## Fichiers principaux

### `server.py` (2000+ lignes)

- Serveur MCP complet avec 20 outils
- Gestion SQLite avec 8 tables
- Parsing RSS, HTML et API JSON
- Cache intelligent et gestion d'erreurs
- Gestion des événements personnels et favoris
- Export iCal pour Outlook/Google Calendar

### `reinvent_data.db` (SQLite)

- **sessions** : 1868 sessions avec détails complets
- **rss_items** : Mises à jour RSS des nouvelles sessions
- **aws_events** : Événements officiels AWS (keynotes, expo, etc.)

- **personal_events** : Événements personnels de l'utilisateur
- **favorite_lists** : Listes de favoris personnalisées
- **favorite_sessions** : Sessions favorites avec notes et priorités
- **sync_log** : Historique complet des synchronisations

## 20 Outils MCP disponibles

### Sessions et données (4 outils)

1. **search_sessions** - Recherche flexible de sessions avec filtres multiples
2. **get_session_details** - Détails complets d'une session spécifique
3. **list_available_filters** - Liste tous les filtres disponibles
4. **get_schedule_by_day** - Planning complet d'une journée

### Mises à jour RSS (2 outils)

5. **get_rss_updates** - Dernières mises à jour du flux RSS
6. **sync_rss_feed** - Synchronisation RSS manuelle

### Agenda officiel AWS (2 outils)

7. **get_aws_events** - Événements officiels AWS
8. **sync_aws_events** - Synchronisation agenda AWS

### Synchronisation et historique (2 outils)

11. **sync_all_data** - Synchronisation complète de toutes les sources
12. **get_sync_history** - Historique des synchronisations

### Événements personnels (3 outils)

13. **add_personal_event** - Ajouter un événement personnel
14. **get_personal_events** - Obtenir les événements personnels
15. **delete_personal_event** - Supprimer un événement personnel

### Sessions favorites (4 outils)

16. **add_session_to_favorites** - Ajouter une session aux favoris
17. **get_favorite_sessions** - Obtenir les sessions favorites
18. **remove_session_from_favorites** - Supprimer une session des favoris
19. **create_favorite_list** - Créer une liste de favoris personnalisée

### Export et intégration (1 outil)

20. **export_schedule_to_ical** - Export iCal pour Outlook/Google Calendar

## Sources de données

- **API Sessions** : 1868 sessions re:Invent 2025
- **RSS Feed** : Nouvelles sessions ajoutées en temps réel
- **Agenda AWS** : Événements officiels (keynotes, expo, réceptions)

- **Données personnelles** : Événements et favoris de l'utilisateur

## Tests et qualité

### Suite de tests complète

- **Tests unitaires** : 8 tests couvrant la base de données et les fonctionnalités
- **Tests d'intégration** : 4 tests vérifiant la connectivité API
- **Configuration pytest** : Exécution automatisée avec `pytest`
- **Couverture** : Tests des fonctionnalités critiques

### Commandes de développement

```bash
# Installation et configuration
./install.sh                    # Installation automatique complète
make install                    # Installation via Makefile

# Tests
make test                       # Exécuter tous les tests
pytest tests/                   # Tests avec pytest
pytest tests/test_server.py     # Tests unitaires seulement

# Développement
make run                        # Démarrer le serveur
make clean                      # Nettoyer les fichiers temporaires
```

## Intégration Kiro

### Configuration MCP automatique

Le serveur est configuré automatiquement dans Kiro avec :

- **Auto-approbation** : Tous les 20 outils sont pré-approuvés
- **Gestion d'erreurs** : Logs détaillés et récupération automatique
- **Performance** : Cache intelligent et optimisations
- **Sécurité** : Validation des entrées et gestion des permissions

### Utilisation en production

Le serveur est prêt pour une utilisation en production avec :

- ✅ Base de données SQLite robuste
- ✅ Gestion complète des erreurs
- ✅ Cache intelligent (30 minutes)
- ✅ Tests automatisés complets
- ✅ Documentation exhaustive
- ✅ Export iCal pour intégration calendrier
- ✅ Gestion des événements personnels
- ✅ Système de favoris avancé