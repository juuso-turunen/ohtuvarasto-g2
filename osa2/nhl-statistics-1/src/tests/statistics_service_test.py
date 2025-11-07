import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
        PlayerReaderStub()
    )
        
    def test_search(self):
        search_result = self.stats.search("Kurri")

        self.assertEqual(search_result, self.stats._players[2])

    def test_search_not_found(self):
        search_result = self.stats.search("This will be not found")

        self.assertEqual(search_result, None)
        

    def test_team(self):
        result = self.stats.team("EDM")

        self.assertEqual(result, [self.stats._players[0], self.stats._players[2], self.stats._players[4]])

    def test_top(self):
        result = self.stats.top(1)

        self.assertEqual(result, [self.stats._players[4], self.stats._players[1]])