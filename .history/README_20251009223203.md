# AWS re:Invent Planner MCP Server v3.0

An MCP (Model Context Protocol) server for AWS re:Invent 2025. Queries the re:Invent Planner API, monitors RSS updates, and fetches the official AWS agenda. Includes personal management with events and favorite lists, plus iCal export for Outlook.

## 🚀 Features

### 📊 Sessions and data

- **Session search**: Flexible search with multiple filters
- **Session details**: Complete information about a specific session
- **Available filters**: List all possible filters (days, venues, levels, etc.)
- **Daily schedule**: Complete schedule display for a day
- **RSS updates**: Monitor newly added sessions
- **Official AWS agenda**: Events, keynotes, expo, receptions

> ℹ️ **Info**: For parties and networking events, check out https://conferenceparties.com/reinvent2025/ which lists all the parties and social events for re:Invent 2025!

### 👤 Personal management

- **Personal events**: Add meetings, meals, travel
- **Favorite lists**: 4 lists (preselection, plan_a, plan_b, plan_c) + custom lists
- **Notes and priorities**: Organize your sessions with personal notes
- **iCal export**: Complete export to Outlook, Google Calendar, Apple Calendar

### 🗄️ Storage and history

- **SQLite database**: Complete synchronization history
- **Smart cache**: Performance optimization
- **Change tracking**: Update history

## 🛠️ 18 Available MCP Tools

### Sessions (Main API)

### `search_sessions`

Search sessions with flexible filtering options:

- `query`: Text search in title, summary, or speaker names
- `day`: Filter by day (Monday, Tuesday, Wednesday, Thursday, Friday)
- `venue`: Filter by venue (e.g., 'Venetian', 'MGM')
- `level`: Filter by level (100, 200, 300, 400)
- `service`: Filter by AWS service
- `topic`: Filter by topic
- `type`: Filter by session type
- `area_of_interest`: Filter by area of interest
- `limit`: Maximum number of results (default: 50)

### `get_session_details`

Get detailed information about a specific session:

- `session_id`: Session ID or short ID (e.g., 'DVT222-S')

### `list_available_filters`

List all available filter values:

- `filter_type`: Filter type ('days', 'venues', 'levels', 'services', 'topics', 'types', 'areas_of_interest', 'all')

### `get_schedule_by_day`

Get the complete schedule for a day:

- `day`: Day to display
- `venue`: Optional, filter by specific venue

### RSS Updates

### `get_rss_updates`

Get the latest RSS feed updates:

- `limit`: Maximum number of results (default: 10)
- `category`: Filter by category (e.g., 'Keynote', 'Breakout session')

### `sync_rss_feed`

Manually synchronize the RSS feed to retrieve new sessions

### Official AWS Agenda

### `get_aws_events`

Get official AWS events:

- `day`: Filter by day
- `event_type`: Filter by type (Keynote, Session, Expo, Social, Meal, General)
- `limit`: Maximum number of events (default: 50)

### `sync_aws_events`

Manually synchronize the official AWS agenda

### Synchronization and History

### `sync_all_data`

Synchronize all data sources (RSS, AWS events, sessions)

### `get_sync_history`

Get synchronization history:

- `source`: Filter by source (catalog, rss, aws_events)
- `limit`: Maximum number of records (default: 20)

### Personal Events

### `add_personal_event`

Add a personal event to your schedule:

- `title`: Event title (required)
- `description`: Event description
- `start_datetime`: Start date/time (format: YYYY-MM-DD HH:MM) (required)
- `end_datetime`: End date/time (format: YYYY-MM-DD HH:MM) (required)
- `location`: Event location
- `event_type`: Event type (meeting, meal, travel, personal, etc.)
- `notes`: Additional notes

### `get_personal_events`

Get your personal events:

- `day`: Filter by day (Monday, Tuesday, etc.)
- `event_type`: Filter by event type

### `delete_personal_event`

Delete a personal event:

- `event_id`: ID of the event to delete (required)

### Favorite Sessions

### `add_session_to_favorites`

Add a session to a favorite list:

- `session_id`: Session ID or short ID (required)
- `list_name`: List name (preselection, plan_a, plan_b, plan_c) (required)
- `notes`: Personal notes about this session
- `priority`: Priority level (1-5, 1 being highest)

### `get_favorite_sessions`

Get sessions from a favorite list:

- `list_name`: List name or 'all' for all lists (default: all)

### `remove_session_from_favorites`

Remove a session from a favorite list:

- `session_id`: Session ID or short ID (required)
- `list_name`: List name (required)

### `create_favorite_list`

Create a custom favorite list:

- `list_name`: New list name (required)
- `description`: List description

### Export and Integration

### `export_schedule_to_ical`

Export your schedule to iCal format for Outlook:

- `list_name`: Favorite list to export ('all' for all, default: all)
- `include_personal_events`: Include personal events (default: true)
- `filename`: Output filename without extension (default: reinvent_schedule)

## 🚀 Installation

### Automatic Installation

```bash
chmod +x install.sh
./install.sh
```

### Manual Installation

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
make test
```

### MCP Configuration for Kiro

The `.kiro/settings/mcp.json` file is automatically configured:

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
# Unit tests
make test

# Tests with external APIs (requires internet)
make test-integration

# Other commands
make clean          # Clean temporary files
make help           # See all commands
```

## 📊 SQLite Database

The server automatically stores all data in `reinvent_data.db`:

- **sessions**: All sessions with modification history
- **rss_items**: New sessions from RSS feed
- **aws_events**: Official AWS events
- **sync_log**: Complete synchronization history
- **personal_events**: Your personal events
- **favorite_lists**: Favorite session lists (preselection, plan_a, plan_b, plan_c)
- **favorite_sessions**: Saved sessions with notes and priorities

## 🎯 Usage Examples

### Sessions

- Search all AI sessions on Tuesday:
  `search_sessions(query="AI", day="Tuesday")`
- Find level 300 sessions on Kubernetes:
  `search_sessions(service="Kubernetes", level=300)`
- View Wednesday schedule at Venetian:
  `get_schedule_by_day(day="Wednesday", venue="Venetian")`
- Get session details:
  `get_session_details(session_id="DVT222-S")`

### Updates and Events

- View latest added sessions:
  `get_rss_updates(limit=5)`
- Synchronize all data:
  `sync_all_data()`
- View AWS keynotes:
  `get_aws_events(event_type="Keynote")`
- View synchronization history:
  `get_sync_history(limit=10)`

### Personal Management

- Add a personal event:
  `add_personal_event(title="Team Meeting", start_datetime="2025-12-02 09:00", end_datetime="2025-12-02 10:00", location="Hotel Venetian")`
- View your events:
  `get_personal_events(day="Tuesday")`
- Add session to favorites:
  `add_session_to_favorites(session_id="DVT222-S", list_name="plan_a", notes="Priority session", priority=1)`
- View favorite sessions:
  `get_favorite_sessions(list_name="plan_a")`
- Export to Outlook:
  `export_schedule_to_ical(list_name="all", filename="my_reinvent_schedule")`

### Advanced Analysis

- Search AI sessions at Venetian:
  `search_sessions(query="AI", venue="Venetian", limit=50)`
- Expert level sessions:
  `search_sessions(level=400, venue="Venetian")`
- Complete Venetian Tuesday schedule:
  `get_schedule_by_day(day="Tuesday", venue="Venetian")`

## 🌐 Data Sources

This server uses multiple sources:

- **Sessions API**: https://reinvent-planner.cloud/api/catalog (1868 sessions)
- **RSS Feed**: https://reinvent-planner.cloud/api/feed/rss (107 updates)
- **AWS Agenda**: https://reinvent.awsevents.com/agenda/ (140 official events)

Data is cached for 30 minutes and permanently stored in SQLite for history.

## 🏢 Venue Analysis

### Venetian (268 sessions - 14.3% of total)

**The technical hub of re:Invent**

- **By level**: 50% level 200, 33% level 300, 13% level 100, 4% level 400
- **By topic**: 33% AI, 12% Developer Tools, 10% Business Apps, 9% Migration
- **Types**: Lightning talks (20min), Breakout sessions (60min), Workshops (2h)
- **Focus**: Technical sessions for experienced practitioners

## 📁 Project Structure

```
reinvent-planner/
├── server.py              # Main MCP server (20 tools)
├── requirements.txt       # Python dependencies
├── README.md              # Main documentation
├── config.json            # Configuration and metadata
├── Makefile               # Development commands
├── pytest.ini             # Test configuration
├── install.sh             # Installation script
├── .gitignore             # Git ignore files
├── docs/                  # French documentation
│   ├── examples.md        # 35 usage examples (French)
│   ├── CHANGELOG.md       # Version history (French)
│   └── STRUCTURE.md       # Detailed structure (French)
├── docs_EN/               # English documentation
│   ├── README.md          # English docs index
│   ├── examples.md        # 35 usage examples (English)
│   ├── CHANGELOG.md       # Version history (English)
│   └── STRUCTURE.md       # Detailed structure (English)
└── tests/                 # Test suite
    ├── test_server.py     # Unit tests
    ├── test_integration.py # Integration tests
    └── conftest.py        # Pytest configuration

Database (created automatically):
└── reinvent_data.db       # SQLite with 8 tables
```

## 📈 Current Statistics

- **18 MCP tools**: Sessions, RSS, AWS events, personal, favorites, export
- **7 SQLite tables**: Complete storage with history
- **1868 sessions**: Complete re:Invent 2025 catalog (updated)
- **268 Venetian sessions**: 14.3% of total, technical focus
- **Complete tests**: 8 unit tests + 4 integration tests
- **iCal export**: Compatible with Outlook, Google Calendar, Apple Calendar
- **Operational server**: Connected and functional in Kiro ✅
