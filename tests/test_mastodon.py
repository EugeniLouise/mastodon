from datetime import datetime
from datetime import timedelta
from unittest.mock import patch, MagicMock

from controller import TootController
from domain.toots import Toots
from proxy.mastodon_proxy import MastodonProxy
from repository.language_stats_repository import LanguageStatsRepository
from uses_cases.toot_by_language import TootByLanguage
from uses_cases.toot_collector import TootCollector


class TestMastodon:

    # Test to verify that get_latest_toots returns the correct toots
    def test_get_latest_toots(self):
        # Mock data representing the API response
        fake_toots = [
            {'content': 'Toot 1'},
            {'content': 'Toot 2'},
            {'content': 'Toot 3'},
        ]

        # Use patch to simulate the call to mastodon.timeline_public
        # Objeto mock para timeline_public, reemplaza timeline_public con un objeto mock solo durante la prueba (eficiencia rapidez)
        with patch('proxy.mastodon_proxy.Mastodon.timeline_public', return_value=fake_toots) as mock_timeline:
            proxy = MastodonProxy()
            result = proxy.get_latest_toots(limit=3)

            # Verify that the API call was made as expected
            mock_timeline.assert_called_once_with(limit=3)

            # Verify that the result is as expected
            assert result == fake_toots, "The method get_latest_toots should return the simulated toots"

    def test_collect_latest_toots(self):
        # Mock data representing the API response with raw toots
        fake_toots = [
            {
                'id': '1',
                'content': 'Toot 1',
                'account': {'username': 'user1'},
                'created_at': datetime.now(),
                'language': 'en'
            },
            {
                'id': '2',
                'content': 'Toot 2',
                'account': {'username': 'user2'},
                'created_at': datetime.now(),
                'language': 'es'
            }
        ]

        # Adjust datetime in fake_toots to include timezone info for the test
        for toot in fake_toots:
            toot['created_at'] = toot['created_at'].replace(tzinfo=datetime.now().astimezone().tzinfo)

        # Use patch to simulate the call to get_latest_toots and return the fake toots
        with patch.object(MastodonProxy, 'get_latest_toots', return_value=fake_toots):
            mastodon_proxy = MastodonProxy()
            toot_collector = TootCollector(mastodon_proxy=mastodon_proxy)
            collected_toots = toot_collector.collect_latest_toots()

            # Verify that collected_toots processes and adjusts the toots correctly
            assert len(collected_toots) == len(fake_toots), "Should collect the correct number of toots"
            for collected_toot, fake_toot in zip(collected_toots, fake_toots):
                assert collected_toot.id == fake_toot['id'], "Toot ID should match"
                assert collected_toot.content == fake_toot['content'], "Toot content should match"
                assert collected_toot.username == fake_toot['account']['username'], "Username should match"
                assert collected_toot.language == fake_toot.get('language', 'unknown'), "Language should match"
                # Verify the adjustment of created_at by checking it's one hour ahead of the mocked raw toot
                assert collected_toot.created_at == fake_toot['created_at'].replace(tzinfo=None) + timedelta(
                    hours=1), "created_at should be adjusted correctly"

    def test_calculate_language_stats(self):
        # Crear instancias de Toot con diferentes idiomas
        toots = [
            Toots(id='1', content='Toot 1', username='user1', language='en', created_at=datetime.now()),
            Toots(id='2', content='Toot 2', username='user2', language='es', created_at=datetime.now()),
            Toots(id='3', content='Toot 3', username='user3', language='en', created_at=datetime.now()),
        ]

        toot_by_language = TootByLanguage()
        language_stats = toot_by_language.calculate_language_stats(toots=toots)

        # Verificar que las estadísticas de idioma sean correctas
        assert 'en' in language_stats, "English should be in language stats"
        assert 'es' in language_stats, "Spanish should be in language stats"
        assert language_stats['en']['count'] == 2, "There should be 2 English toots"
        assert language_stats['es']['count'] == 1, "There should be 1 Spanish toot"
        assert language_stats['en']['last_user'] == 'user3', "The last user for English toots should be user3"
        assert language_stats['es']['last_user'] == 'user2', "The last user for Spanish toots should be user2"

    @patch('repository.language_stats_repository.pd.DataFrame.to_excel')
    def test_save_language_stats_to_excel(self, mock_to_excel):
        # Datos de entrada simulados
        language_stats = {
            'en': {'count': 2, 'last_user': 'user1'},
            'es': {'count': 1, 'last_user': 'user2'}
        }

        # Instancia de LanguageStatsRepository
        repository = LanguageStatsRepository()

        # Llamada al método que queremos probar
        repository.save_language_stats_to_excel(language_stats, filename="test_language_stats.xlsx")

        # Verificación de que to_excel fue llamado una vez
        mock_to_excel.assert_called_once()

    @patch('controller.MastodonProxy')
    @patch('controller.TootCollector')
    @patch('controller.TootRepository')
    @patch('controller.LanguageStatsRepository')
    def test_run(self, mock_language_stats_saver, mock_toot_saver, mock_toot_collector, mock_mastodon_proxy):
        # Configuramos los mocks
        mock_toot_collector_instance = MagicMock()
        mock_toot_collector.return_value = mock_toot_collector_instance
        mock_toot_collector_instance.collect_latest_toots.return_value = [{'id': '1', 'content': 'Test toot'}]

        mock_language_stats = MagicMock()
        mock_language_stats.return_value = {'en': {'count': 1, 'last_user': 'user1'}}
        TootByLanguage.calculate_language_stats = mock_language_stats

        # Creamos una instancia de TootController y ejecutamos el método run
        controller = TootController()
        controller.run()

        # Verificaciones
        mock_toot_collector_instance.collect_latest_toots.assert_called_once()
        mock_toot_saver.return_value.save_toots_to_excel.assert_called_once()
        mock_language_stats.assert_called_once()
        mock_language_stats_saver.return_value.save_language_stats_to_excel.assert_called_once()
