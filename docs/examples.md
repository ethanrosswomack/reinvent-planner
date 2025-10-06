# Usage Examples for re:Invent Planner MCP Server

## Common Searches

### 1. Find AI sessions
```
search_sessions(query="AI", limit=10)
```

### 2. Beginner level sessions on Monday
```
search_sessions(day="Monday", level=100)
```

### 3. Amazon Bedrock sessions
```
search_sessions(service="Bedrock")
```

### 4. Kubernetes sessions at Venetian
```
search_sessions(venue="Venetian", query="Kubernetes")
```

### 5. Advanced security sessions
```
search_sessions(topic="Security", level=300)
```

## Planning

### 6. Complete Wednesday schedule
```
get_schedule_by_day(day="Wednesday")
```

### 7. Thursday schedule at MGM only
```
get_schedule_by_day(day="Thursday", venue="MGM")
```

## Data Exploration

### 8. View all available AWS services
```
list_available_filters(filter_type="services")
```

### 9. View all available topics
```
list_available_filters(filter_type="topics")
```

### 10. View all available venues
```
list_available_filters(filter_type="venues")
```

## Session Details

### 11. Get details of a specific session
```
get_session_details(session_id="DVT222-S")
```

## Advanced Searches

### 12. Machine learning sessions for developers
```
search_sessions(query="machine learning", area_of_interest="Developer Tools")
```

### 13. "Breakout session" type sessions on cloud computing
```
search_sessions(type="Breakout session", topic="Cloud Computing")
```

### 14. Sessions for solution architects
```
search_sessions(area_of_interest="Solution Architecture")
```

### 15. AWS partner sponsored sessions
```
search_sessions(query="sponsored")
```

## New Examples with Extended Features

### 16. View latest added sessions
```
get_rss_updates(limit=10)
```

### 17. Synchronize all data
```
sync_all_data()
```

### 18. View AWS keynotes
```
get_aws_events(event_type="Keynote")
```

### 19. Official Tuesday schedule
```
get_aws_events(day="Tuesday")
```



### 22. Synchronization history
```
get_sync_history(limit=10)
```

### 23. RSS synchronizations only
```
get_sync_history(source="rss")
```

### 24. New Keynote sessions
```
get_rss_updates(category="Keynote")
```

### 25. Synchronize RSS feed only
```
sync_rss_feed()
```

## Personal Management

### 26. Add a personal event
```
add_personal_event(
    title="Team Meeting",
    description="re:Invent planning",
    start_datetime="2025-12-02 09:00",
    end_datetime="2025-12-02 10:00",
    location="Hotel Venetian - Lobby",
    event_type="meeting",
    notes="Prepare questions"
)
```

### 27. View my Tuesday events
```
get_personal_events(day="Tuesday")
```

### 28. Add session to favorites
```
add_session_to_favorites(
    session_id="DVT222-S",
    list_name="plan_a",
    notes="Very interesting session on observability",
    priority=1
)
```

### 29. View my plan A sessions
```
get_favorite_sessions(list_name="plan_a")
```

### 30. View all my favorite sessions
```
get_favorite_sessions(list_name="all")
```

### 31. Create a custom list
```
create_favorite_list(
    list_name="must_see",
    description="Absolutely must-see sessions"
)
```

### 32. Remove session from favorites
```
remove_session_from_favorites(
    session_id="DVT222-S",
    list_name="plan_a"
)
```

### 33. Export my schedule to Outlook
```
export_schedule_to_ical(
    list_name="all",
    include_personal_events=True,
    filename="my_reinvent_schedule"
)
```

### 34. Export plan A only
```
export_schedule_to_ical(
    list_name="plan_a",
    include_personal_events=False,
    filename="plan_a_sessions"
)
```

### 35. Delete a personal event
```
delete_personal_event(event_id=1)
```

## Usage Tips

- Use `sync_all_data()` at the beginning to retrieve all data
- `limit` controls the number of results for all queries
- Combine multiple filters for precise searches
- Text searches (`query`) search in title, summary, and speaker names
- Filters are case-insensitive
- Use `list_available_filters()` to discover all available options
- SQLite history allows tracking data evolution over time
- Manual synchronizations ensure you have the most recent data
- Use the 4 favorite lists to organize your sessions: preselection, plan_a, plan_b, plan_c
- Personal events allow adding meetings, meals, travel to your schedule
- iCal export generates a .ics file compatible with Outlook, Google Calendar, Apple Calendar
- Priorities (1-5) allow ranking your sessions by importance
- Personal notes help you remember why a session interests you
