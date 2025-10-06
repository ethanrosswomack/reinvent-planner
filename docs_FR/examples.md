# Exemples d'utilisation du serveur MCP re:Invent Planner

## Recherches courantes

### 1. Trouver des sessions sur l'IA
```
search_sessions(query="AI", limit=10)
```

### 2. Sessions de niveau débutant le lundi
```
search_sessions(day="Monday", level=100)
```

### 3. Sessions sur Amazon Bedrock
```
search_sessions(service="Bedrock")
```

### 4. Sessions au Venetian sur Kubernetes
```
search_sessions(venue="Venetian", query="Kubernetes")
```

### 5. Sessions sur la sécurité de niveau avancé
```
search_sessions(topic="Security", level=300)
```

## Planification

### 6. Planning complet du mercredi
```
get_schedule_by_day(day="Wednesday")
```

### 7. Planning du jeudi au MGM uniquement
```
get_schedule_by_day(day="Thursday", venue="MGM")
```

## Exploration des données

### 8. Voir tous les services AWS disponibles
```
list_available_filters(filter_type="services")
```

### 9. Voir tous les sujets disponibles
```
list_available_filters(filter_type="topics")
```

### 10. Voir tous les lieux disponibles
```
list_available_filters(filter_type="venues")
```

## Détails de sessions

### 11. Obtenir les détails d'une session spécifique
```
get_session_details(session_id="DVT222-S")
```

## Recherches avancées

### 12. Sessions sur le machine learning pour développeurs
```
search_sessions(query="machine learning", area_of_interest="Developer Tools")
```

### 13. Sessions de type "Breakout session" sur le cloud computing
```
search_sessions(type="Breakout session", topic="Cloud Computing")
```

### 14. Sessions pour les architectes solutions
```
search_sessions(area_of_interest="Solution Architecture")
```

### 15. Sessions sponsorisées par des partenaires AWS
```
search_sessions(query="sponsored")
```

## Nouveaux exemples avec les fonctionnalités étendues

### 16. Voir les dernières sessions ajoutées
```
get_rss_updates(limit=10)
```

### 17. Synchroniser toutes les données
```
sync_all_data()
```

### 18. Voir les keynotes AWS
```
get_aws_events(event_type="Keynote")
```

### 19. Planning officiel du mardi
```
get_aws_events(day="Tuesday")
```



### 22. Historique des synchronisations
```
get_sync_history(limit=10)
```

### 23. Synchronisations RSS uniquement
```
get_sync_history(source="rss")
```

### 24. Nouvelles sessions Keynote
```
get_rss_updates(category="Keynote")
```

### 25. Synchroniser uniquement le flux RSS
```
sync_rss_feed()
```

## Gestion personnelle

### 26. Ajouter un événement personnel
```
add_personal_event(
    title="Réunion équipe",
    description="Planification re:Invent",
    start_datetime="2025-12-02 09:00",
    end_datetime="2025-12-02 10:00",
    location="Hotel Venetian - Lobby",
    event_type="meeting",
    notes="Préparer les questions"
)
```

### 27. Voir mes événements du mardi
```
get_personal_events(day="Tuesday")
```

### 28. Ajouter une session aux favoris
```
add_session_to_favorites(
    session_id="DVT222-S",
    list_name="plan_a",
    notes="Session très intéressante sur l'observabilité",
    priority=1
)
```

### 29. Voir mes sessions plan A
```
get_favorite_sessions(list_name="plan_a")
```

### 30. Voir toutes mes sessions favorites
```
get_favorite_sessions(list_name="all")
```

### 31. Créer une liste personnalisée
```
create_favorite_list(
    list_name="must_see",
    description="Sessions absolument à voir"
)
```

### 32. Supprimer une session des favoris
```
remove_session_from_favorites(
    session_id="DVT222-S",
    list_name="plan_a"
)
```

### 33. Exporter mon planning vers Outlook
```
export_schedule_to_ical(
    list_name="all",
    include_personal_events=True,
    filename="mon_planning_reinvent"
)
```

### 34. Exporter seulement le plan A
```
export_schedule_to_ical(
    list_name="plan_a",
    include_personal_events=False,
    filename="plan_a_sessions"
)
```

### 35. Supprimer un événement personnel
```
delete_personal_event(event_id=1)
```

## Conseils d'utilisation

- Utilisez `sync_all_data()` au début pour récupérer toutes les données
- `limit` contrôle le nombre de résultats pour toutes les requêtes
- Combinez plusieurs filtres pour des recherches précises
- Les recherches textuelles (`query`) cherchent dans le titre, résumé et noms des speakers
- Les filtres sont insensibles à la casse
- Utilisez `list_available_filters()` pour découvrir toutes les options disponibles
- L'historique SQLite permet de suivre l'évolution des données dans le temps
- Les synchronisations manuelles permettent d'avoir les données les plus récentes
- Utilisez les 4 listes de favoris pour organiser vos sessions : preselection, plan_a, plan_b, plan_c
- Les événements personnels permettent d'ajouter réunions, repas, déplacements à votre planning
- L'export iCal génère un fichier .ics compatible avec Outlook, Google Calendar, Apple Calendar
- Les priorités (1-5) permettent de classer vos sessions par importance
- Les notes personnelles vous aident à vous rappeler pourquoi une session vous intéresse