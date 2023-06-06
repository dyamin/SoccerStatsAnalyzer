import unittest

from src import config
from src.SoccerDataLoader import SoccerDataLoader
from src.analysis.TopPlayerScorersStrategy import TopPlayerScorersStrategy


class TestTopPlayerScorersStrategy(unittest.TestCase):
    def setUp(self):
        self.data_loader = SoccerDataLoader(config.database_path)
        self.strategy = TopPlayerScorersStrategy(self.data_loader)

    def test_analyze(self):
        expected_rows, expected_cols = 3, 2
        result = self.strategy.analyze(expected_rows)

        self.assertEqual(result.shape, (expected_rows, expected_cols))
        self.assertIn('Lionel Messi', result['player_name'].values)


if __name__ == '__main__':
    unittest.main()
