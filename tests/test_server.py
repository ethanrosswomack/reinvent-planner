#!/usr/bin/env python3
"""
Tests unitaires pour le serveur MCP re:Invent Planner
"""

import asyncio
import pytest
import pytest_asyncio
import tempfile
import os
from pathlib import Path
import sys

# Add parent directory to path to import server
sys.path.insert(0, str(Path(__file__).parent.parent))

from server import ReinventPlannerServer

class TestReinventPlannerServer:
    """Tests pour le serveur MCP re:Invent Planner"""
    
    @pytest_asyncio.fixture
    async def server(self):
        """Fixture pour créer une instance du serveur avec une DB temporaire"""
        # Create temporary database
        temp_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        temp_db.close()
        
        # Patch the DB_PATH
        original_db_path = Path(__file__).parent.parent / "reinvent_data.db"
        import server
        server.DB_PATH = Path(temp_db.name)
        
        server_instance = ReinventPlannerServer()
        await server_instance.init_database()
        
        yield server_instance
        
        # Cleanup
        os.unlink(temp_db.name)
        server.DB_PATH = original_db_path
    
    @pytest.mark.asyncio
    async def test_database_initialization(self, server):
        """Test l'initialisation de la base de données"""
        # La base devrait être initialisée par la fixture
        assert server is not None
        
        # Vérifier que les tables par défaut sont créées
        import aiosqlite
        import server as server_module
        async with aiosqlite.connect(server_module.DB_PATH) as db:
            cursor = await db.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in await cursor.fetchall()]
            
            expected_tables = [
                'sessions', 'rss_items', 'aws_events', 'sync_log',
                'personal_events', 'favorite_lists', 'favorite_sessions'
            ]
            
            for table in expected_tables:
                assert table in tables, f"Table {table} manquante"
    
    @pytest.mark.asyncio
    async def test_add_personal_event(self, server):
        """Test l'ajout d'un événement personnel"""
        result = await server.add_personal_event(
            title="Test Event",
            start_datetime="2025-12-02 09:00",
            end_datetime="2025-12-02 10:00",
            location="Test Location",
            event_type="meeting",
            notes="Test notes"
        )
        
        assert len(result) == 1
        assert "✅" in result[0].text
        assert "Test Event" in result[0].text
    
    @pytest.mark.asyncio
    async def test_get_personal_events(self, server):
        """Test la récupération des événements personnels"""
        # Ajouter un événement d'abord
        await server.add_personal_event(
            title="Test Event",
            start_datetime="2025-12-02 09:00",
            end_datetime="2025-12-02 10:00"
        )
        
        # Récupérer les événements
        result = await server.get_personal_events()
        
        assert len(result) == 1
        assert "Test Event" in result[0].text
        assert "1 événements" in result[0].text
    
    @pytest.mark.asyncio
    async def test_delete_personal_event(self, server):
        """Test la suppression d'un événement personnel"""
        # Ajouter un événement d'abord
        await server.add_personal_event(
            title="Test Event to Delete",
            start_datetime="2025-12-02 09:00",
            end_datetime="2025-12-02 10:00"
        )
        
        # Supprimer l'événement (ID 1)
        result = await server.delete_personal_event(1)
        
        assert len(result) == 1
        assert "✅" in result[0].text
        assert "supprimé" in result[0].text
    
    @pytest.mark.asyncio
    async def test_create_favorite_list(self, server):
        """Test la création d'une liste de favoris"""
        result = await server.create_favorite_list(
            list_name="test_list",
            description="Liste de test"
        )
        
        assert len(result) == 1
        assert "✅" in result[0].text
        assert "test_list" in result[0].text
    
    @pytest.mark.asyncio
    async def test_invalid_datetime_format(self, server):
        """Test la validation du format de date/heure"""
        result = await server.add_personal_event(
            title="Invalid Event",
            start_datetime="invalid-date",
            end_datetime="2025-12-02 10:00"
        )
        
        assert len(result) == 1
        assert "❌" in result[0].text
        assert "Invalid datetime format" in result[0].text
    
    @pytest.mark.asyncio
    async def test_duplicate_favorite_list(self, server):
        """Test la création d'une liste de favoris en double"""
        # Créer la première liste
        await server.create_favorite_list("duplicate_test", "Test")
        
        # Essayer de créer la même liste
        result = await server.create_favorite_list("duplicate_test", "Test 2")
        
        assert len(result) == 1
        assert "❌" in result[0].text
        assert "existe déjà" in result[0].text
    
    @pytest.mark.asyncio
    async def test_export_ical_empty(self, server):
        """Test l'export iCal sans données"""
        result = await server.export_schedule_to_ical(
            list_name="all",
            filename="test_empty"
        )
        
        assert len(result) == 1
        assert "✅" in result[0].text
        assert "test_empty.ics" in result[0].text
        
        # Vérifier que le fichier a été créé
        assert Path("test_empty.ics").exists()
        
        # Nettoyer
        Path("test_empty.ics").unlink()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])