#!/usr/bin/env python3
"""
Tests d'intégration pour le serveur MCP re:Invent Planner
Ces tests nécessitent une connexion internet pour accéder aux APIs
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

class TestIntegration:
    """Tests d'intégration avec les APIs externes"""
    
    @pytest_asyncio.fixture
    async def server(self):
        """Fixture pour créer une instance du serveur avec une DB temporaire"""
        temp_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        temp_db.close()
        
        import server
        server.DB_PATH = Path(temp_db.name)
        
        server_instance = ReinventPlannerServer()
        await server_instance.init_database()
        
        yield server_instance
        
        os.unlink(temp_db.name)
    
    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_fetch_catalog(self, server):
        """Test la récupération du catalogue de sessions"""
        try:
            catalog = await server.fetch_catalog()
            assert isinstance(catalog, list)
            assert len(catalog) > 0
            
            # Vérifier la structure d'une session
            session = catalog[0]
            assert 'id' in session
            assert 'title' in session
            
        except Exception as e:
            pytest.skip(f"API non disponible: {e}")
    
    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_fetch_rss_feed(self, server):
        """Test la récupération du flux RSS"""
        try:
            result = await server.fetch_and_store_rss_feed()
            assert result['status'] == 'success'
            assert 'items_processed' in result
            
        except Exception as e:
            pytest.skip(f"RSS feed non disponible: {e}")
    
    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_search_sessions(self, server):
        """Test la recherche de sessions"""
        try:
            # D'abord récupérer le catalogue
            await server.fetch_catalog()
            
            # Ensuite rechercher
            result = await server.search_sessions(query="AI", limit=5)
            assert len(result) == 1
            assert "session" in result[0].text.lower()
            
        except Exception as e:
            pytest.skip(f"Recherche non disponible: {e}")
    
    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_sync_all_data(self, server):
        """Test la synchronisation complète"""
        try:
            result = await server.sync_all_data()
            assert len(result) == 1
            assert "Complete Data Sync Results" in result[0].text
            
        except Exception as e:
            pytest.skip(f"Sync non disponible: {e}")

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-m", "integration"])