# AWS re:Invent Planner MCP Server v3.0

Un serveur MCP (Model Context Protocol) pour AWS re:Invent 2025. Interroge l'API re:Invent Planner, surveille les mises à jour RSS et récupère l'agenda officiel AWS. Inclut la gestion personnelle avec événements et listes de favoris, plus l'export iCal pour Outlook.

## 🚀 Fonctionnalités

### 📊 Sessions et données
- **Recherche de sessions** : Recherche flexible avec filtres multiples
- **Détails de session** : Informations complètes sur une session spécifique
- **Filtres disponibles** : Liste tous les filtres possibles (jours, lieux, niveaux, etc.)
- **Planning par jour** : Affichage du planning complet d'une journée
- **Mises à jour RSS** : Surveillance des nouvelles sessions ajoutées
- **Agenda officiel AWS** : Événements, keynotes, expo, réceptions

> ℹ️ **Info** : Pour les soirées et événements networking, consultez https://conferenceparties.com/reinvent2025/ qui liste toutes les parties et événements sociaux de re:Invent 2025 !

### 👤 Gestion personnelle
- **Événements personnels** : Ajout de réunions, repas, déplacements
- **Listes de favoris** : 4 listes (preselection, plan_a, plan_b, plan_c) + listes personnalisées
- **Notes et priorités** : Organisation de vos sessions avec notes personnelles
- **Export iCal** : Export complet vers Outlook, Google Calendar, Apple Calendar

### 🗄️ Stockage et historique
- **Base de données SQLite** : Historique complet des synchronisations
- **Cache intelligent** : Optimisation des performances
- **Suivi des modifications** : Historique des mises à jour

## 🛠️ 18 Outils MCP disponibles

### Sessions (API principale)

### `search_sessions`
Recherche de sessions avec options de filtrage flexibles :
- `query` : Recherche textuelle dans le titre, résumé ou noms des speakers
- `day` : Filtrer par jour (Monday, Tuesday, Wednesday, Thursday, Friday)
- `venue` : Filtrer par lieu (ex: 'Venetian', 'MGM')
- `level` : Filtrer par niveau (100, 200, 300, 400)
- `service` : Filtrer par service AWS
- `topic` : Filtrer par sujet
- `type` : Filtrer par type de session
- `area_of_interest` : Filtrer par domaine d'intérêt
- `limit` : Nombre maximum de résultats (défaut: 50)

### `get_session_details`
Obtenir les informations détaillées d'une session spécifique :
- `session_id` : ID de session ou ID court (ex: 'DVT222-S')

### `list_available_filters`
Lister toutes les valeurs de filtres disponibles :
- `filter_type` : Type de filtre ('days', 'venues', 'levels', 'services', 'topics', 'types', 'areas_of_interest', 'all')

### `get_schedule_by_day`
Obtenir le planning complet d'une journée :
- `day` : Jour à afficher
- `venue` : Optionnel, filtrer par lieu spécifique

### Mises à jour RSS

### `get_rss_updates`
Obtenir les dernières mises à jour du flux RSS :
- `limit` : Nombre maximum de résultats (défaut: 10)
- `category` : Filtrer par catégorie (ex: 'Keynote', 'Breakout session')

### `sync_rss_feed`
Synchroniser manuellement le flux RSS pour récupérer les nouvelles sessions

### Agenda officiel AWS

### `get_aws_events`
Obtenir les événements officiels AWS :
- `day` : Filtrer par jour
- `event_type` : Filtrer par type (Keynote, Session, Expo, Social, Meal, General)
- `limit` : Nombre maximum d'événements (défaut: 50)

### `sync_aws_events`
Synchroniser manuellement l'agenda officiel AWS

### Synchronisation et historique

### `sync_all_data`
Synchroniser toutes les sources de données (RSS, événements AWS, sessions)

### `get_sync_history`
Obtenir l'historique des synchronisations :
- `source` : Filtrer par source (catalog, rss, aws_events)
- `limit` : Nombre maximum d'enregistrements (défaut: 20)

### Événements personnels

### `add_personal_event`
Ajouter un événement personnel à votre planning :
- `title` : Titre de l'événement (requis)
- `description` : Description de l'événement
- `start_datetime` : Date/heure de début (format: YYYY-MM-DD HH:MM) (requis)
- `end_datetime` : Date/heure de fin (format: YYYY-MM-DD HH:MM) (requis)
- `location` : Lieu de l'événement
- `event_type` : Type d'événement (meeting, meal, travel, personal, etc.)
- `notes` : Notes supplémentaires

### `get_personal_events`
Obtenir vos événements personnels :
- `day` : Filtrer par jour (Monday, Tuesday, etc.)
- `event_type` : Filtrer par type d'événement

### `delete_personal_event`
Supprimer un événement personnel :
- `event_id` : ID de l'événement à supprimer (requis)

### Sessions favorites

### `add_session_to_favorites`
Ajouter une session à une liste de favoris :
- `session_id` : ID de session ou ID court (requis)
- `list_name` : Nom de la liste (preselection, plan_a, plan_b, plan_c) (requis)
- `notes` : Notes personnelles sur cette session
- `priority` : Niveau de priorité (1-5, 1 étant le plus élevé)

### `get_favorite_sessions`
Obtenir les sessions d'une liste de favoris :
- `list_name` : Nom de la liste ou 'all' pour toutes les listes (défaut: all)

### `remove_session_from_favorites`
Supprimer une session d'une liste de favoris :
- `session_id` : ID de session ou ID court (requis)
- `list_name` : Nom de la liste (requis)

### `create_favorite_list`
Créer une liste de favoris personnalisée :
- `list_name` : Nom de la nouvelle liste (requis)
- `description` : Description de la liste

### Export et intégration

### `export_schedule_to_ical`
Exporter votre planning au format iCal pour Outlook :
- `list_name` : Liste de favoris à exporter ('all' pour toutes, défaut: all)
- `include_personal_events` : Inclure les événements personnels (défaut: true)
- `filename` : Nom du fichier de sortie sans extension (défaut: reinvent_schedule)

## 🚀 Installation

### Installation automatique
```bash
chmod +x install.sh
./install.sh
```

### Installation manuelle
```bash
# Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Exécuter les tests
make test
```

### Configuration MCP pour Kiro
Le fichier `.kiro/settings/mcp.json` est automatiquement configuré :
```json
{
  "mcpServers": {
    "reinvent-planner": {
      "command": "./reinvent-planner/venv/bin/python",
      "args": ["./reinvent-planner/server.py"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 🧪 Tests

```bash
# Tests unitaires
make test

# Tests avec APIs externes (nécessite internet)
make test-integration

# Autres commandes
make clean          # Nettoyer les fichiers temporaires
make help           # Voir toutes les commandes
```

## 📊 Base de données SQLite

Le serveur stocke automatiquement toutes les données dans `reinvent_data.db` :

- **sessions** : Toutes les sessions avec historique des modifications
- **rss_items** : Nouvelles sessions du flux RSS
- **aws_events** : Événements officiels AWS
- **sync_log** : Historique complet des synchronisations
- **personal_events** : Vos événements personnels
- **favorite_lists** : Listes de sessions favorites (preselection, plan_a, plan_b, plan_c)
- **favorite_sessions** : Sessions sauvegardées avec notes et priorités

## 🎯 Exemples d'utilisation

### Sessions
- Rechercher toutes les sessions sur l'IA le mardi :
  `search_sessions(query="AI", day="Tuesday")`
- Trouver les sessions de niveau 300 sur Kubernetes :
  `search_sessions(service="Kubernetes", level=300)`
- Voir le planning du mercredi au Venetian :
  `get_schedule_by_day(day="Wednesday", venue="Venetian")`
- Obtenir les détails d'une session :
  `get_session_details(session_id="DVT222-S")`

### Mises à jour et événements
- Voir les dernières sessions ajoutées :
  `get_rss_updates(limit=5)`
- Synchroniser toutes les données :
  `sync_all_data()`
- Voir les keynotes AWS :
  `get_aws_events(event_type="Keynote")`
- Voir l'historique des synchronisations :
  `get_sync_history(limit=10)`

### Gestion personnelle
- Ajouter un événement personnel :
  `add_personal_event(title="Réunion équipe", start_datetime="2025-12-02 09:00", end_datetime="2025-12-02 10:00", location="Hotel Venetian")`
- Voir vos événements :
  `get_personal_events(day="Tuesday")`
- Ajouter une session aux favoris :
  `add_session_to_favorites(session_id="DVT222-S", list_name="plan_a", notes="Session prioritaire", priority=1)`
- Voir vos sessions favorites :
  `get_favorite_sessions(list_name="plan_a")`
- Exporter vers Outlook :
  `export_schedule_to_ical(list_name="all", filename="mon_planning_reinvent")`

### Analyses avancées
- Rechercher sessions IA au Venetian :
  `search_sessions(query="AI", venue="Venetian", limit=50)`
- Sessions niveau expert :
  `search_sessions(level=400, venue="Venetian")`
- Planning complet Venetian mardi :
  `get_schedule_by_day(day="Tuesday", venue="Venetian")`

## 🌐 Sources de données

Ce serveur utilise plusieurs sources :

- **API Sessions** : https://reinvent-planner.cloud/api/catalog (1868 sessions)
- **Flux RSS** : https://reinvent-planner.cloud/api/feed/rss (107 mises à jour)
- **Agenda AWS** : https://reinvent.awsevents.com/agenda/ (140 événements officiels)

Les données sont mises en cache pendant 30 minutes et stockées en permanence dans SQLite pour l'historique.

## 🏢 Analyse des lieux

### Venetian (268 sessions - 14.3% du total)
**Le hub technique de re:Invent**
- **Par niveau** : 50% niveau 200, 33% niveau 300, 13% niveau 100, 4% niveau 400
- **Par sujet** : 33% IA, 12% Developer Tools, 10% Business Apps, 9% Migration
- **Types** : Lightning talks (20min), Breakout sessions (60min), Workshops (2h)
- **Focus** : Sessions techniques pour praticiens expérimentés

## 📁 Structure du projet

```
reinvent-planner/
├── server.py              # Serveur MCP principal (20 outils)
├── requirements.txt       # Dépendances Python
├── README.md              # Documentation principale
├── config.json            # Configuration et métadonnées
├── Makefile               # Commandes de développement
├── pytest.ini             # Configuration des tests
├── install.sh             # Script d'installation
├── .gitignore             # Fichiers à ignorer par Git
├── docs/                  # Documentation détaillée
│   ├── examples.md        # 35 exemples d'utilisation
│   ├── CHANGELOG.md       # Historique des versions
│   └── STRUCTURE.md       # Structure détaillée
└── tests/                 # Suite de tests
    ├── test_server.py     # Tests unitaires
    ├── test_integration.py # Tests d'intégration
    └── conftest.py        # Configuration pytest

Base de données (créée automatiquement) :
└── reinvent_data.db       # SQLite avec 8 tables
```

## 📈 Statistiques actuelles

- **18 outils MCP** : Sessions, RSS, événements AWS, personnel, favoris, export
- **7 tables SQLite** : Stockage complet avec historique
- **1868 sessions** : Catalogue complet re:Invent 2025 (mis à jour)
- **268 sessions au Venetian** : 14.3% du total, focus technique
- **Tests complets** : 8 tests unitaires + 4 tests d'intégration
- **Export iCal** : Compatible Outlook, Google Calendar, Apple Calendar
- **Serveur opérationnel** : Connecté et fonctionnel dans Kiro ✅