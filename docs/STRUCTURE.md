# re:Invent Planner MCP Server v3.0 Project Structure

```text
reinvent-planner/
├── server.py                    # Main MCP server with 20 tools
├── requirements.txt             # Python dependencies
├── README.md                   # Main documentation
├── PROJECT_SUMMARY.md          # Project summary
├── config.json                 # Configuration and metadata
├── install.sh                  # Automatic installation script
├── run_server.sh               # Server startup script
├── Makefile                    # Development tasks
├── pytest.ini                 # Pytest configuration
├── .gitignore                  # Files ignored by Git
├── reinvent_data.db           # SQLite database (created automatically)
├── venv/                      # Python virtual environment
├── docs/                      # French documentation
│   ├── STRUCTURE.md           # Project structure (French)
│   ├── examples.md            # Detailed usage examples (French)
│   └── CHANGELOG.md           # Version history (French)
├── docs_EN/                   # English documentation
│   ├── README.md              # English docs index
│   ├── STRUCTURE.md           # This file (English)
│   ├── examples.md            # Detailed usage examples (English)
│   └── CHANGELOG.md           # Version history (English)
├── tests/                     # Automated tests
│   ├── __init__.py
│   ├── conftest.py            # Pytest configuration
│   ├── test_server.py         # Unit tests (8 tests)
│   └── test_integration.py    # Integration tests (4 tests)
├── generated-docs/            # Generated documentation
│   └── repomix_output.xml
└── .git/                      # Git repository

MCP Configuration:
../.kiro/settings/mcp.json      # Configuration for Kiro
```

## Main Files

### `server.py` (2000+ lines)

- Complete MCP server with 20 tools
- SQLite management with 8 tables
- RSS, HTML and JSON API parsing
- Smart cache and error handling
- Personal events and favorites management
- iCal export for Outlook/Google Calendar

### `reinvent_data.db` (SQLite)

- **sessions**: 1868 sessions with complete details
- **rss_items**: RSS updates of new sessions
- **aws_events**: Official AWS events (keynotes, expo, etc.)

- **personal_events**: User's personal events
- **favorite_lists**: Custom favorite lists
- **favorite_sessions**: Favorite sessions with notes and priorities
- **sync_log**: Complete synchronization history

## 20 Available MCP Tools

### Sessions and Data (4 tools)

1. **search_sessions** - Flexible session search with multiple filters
2. **get_session_details** - Complete details of a specific session
3. **list_available_filters** - List all available filters
4. **get_schedule_by_day** - Complete schedule for a day

### RSS Updates (2 tools)

5. **get_rss_updates** - Latest RSS feed updates
6. **sync_rss_feed** - Manual RSS synchronization

### Official AWS Agenda (2 tools)

7. **get_aws_events** - Official AWS events
8. **sync_aws_events** - AWS agenda synchronization

### Synchronization and History (2 tools)

11. **sync_all_data** - Complete synchronization of all sources
12. **get_sync_history** - Synchronization history

### Personal Events (3 tools)

13. **add_personal_event** - Add a personal event
14. **get_personal_events** - Get personal events
15. **delete_personal_event** - Delete a personal event

### Favorite Sessions (4 tools)

16. **add_session_to_favorites** - Add session to favorites
17. **get_favorite_sessions** - Get favorite sessions
18. **remove_session_from_favorites** - Remove session from favorites
19. **create_favorite_list** - Create custom favorite list

### Export and Integration (1 tool)

20. **export_schedule_to_ical** - iCal export for Outlook/Google Calendar

## Data Sources

- **Sessions API**: 1868 re:Invent 2025 sessions
- **RSS Feed**: New sessions added in real-time
- **AWS Agenda**: Official events (keynotes, expo, receptions)

- **Personal Data**: User events and favorites

## Tests and Quality

### Complete Test Suite

- **Unit tests**: 8 tests covering database and functionality
- **Integration tests**: 4 tests verifying API connectivity
- **Pytest configuration**: Automated execution with `pytest`
- **Coverage**: Tests of critical functionality

### Development Commands

```bash
# Installation and configuration
./install.sh                    # Complete automatic installation
make install                    # Installation via Makefile

# Tests
make test                       # Run all tests
pytest tests/                   # Tests with pytest
pytest tests/test_server.py     # Unit tests only

# Development
make run                        # Start server
make clean                      # Clean temporary files
```

## Kiro Integration

### Automatic MCP Configuration

The server is automatically configured in Kiro with:

- **Auto-approval**: All 20 tools are pre-approved
- **Error handling**: Detailed logs and automatic recovery
- **Performance**: Smart cache and optimizations
- **Security**: Input validation and permission management

### Production Usage

The server is ready for production use with:

- ✅ Robust SQLite database
- ✅ Complete error handling
- ✅ Smart cache (30 minutes)
- ✅ Complete automated tests
- ✅ Comprehensive documentation
- ✅ iCal export for calendar integration
- ✅ Personal events management
- ✅ Advanced favorites system
