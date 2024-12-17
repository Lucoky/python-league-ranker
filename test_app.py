import unittest
import io
from unittest.mock import patch
from league_logic import display_rankings, parse_line, process_results

class TestLeagueLogic(unittest.TestCase):
    def test_parse_line_valid(self):
        line = "Lions 3, Snakes 3"
        result = parse_line(line)
        self.assertEqual(result, ("Lions", 3, "Snakes", 3))

    def test_parse_same_team(self):
        line = "Lions 3, Lions 3"
        with self.assertRaises(ValueError):
            parse_line(line)

    def test_parse_negative_score(self):
        line = "Lions -3, Snakes 3"
        with self.assertRaises(ValueError):
            parse_line(line)

    def test_parse_invalid_score(self):
        line = "Lions 3, Snakes three"
        with self.assertRaises(ValueError):
            parse_line(line)

    def test_parse_line_invalid(self):
        line = "Invalid input"
        with self.assertRaises(ValueError):
            parse_line(line)

    def test_process_results(self):
        input_data = [
            "Lions 3, Snakes 3",
            "Tigers 1, Lions 2",
            "Snakes 0, Tigers 1",
        ]
        result = process_results(input_data)
        expected = [("Lions", 4), ("Tigers", 3), ("Snakes", 1)]
        self.assertEqual(result, expected)

    def test_process_results_empty(self):
        input_data = []
        result = process_results(input_data)
        self.assertEqual(result, [])

    def test_display_rankings_with_ties(self):
        team_points = [
            ("Lions", 4),
            ("Tigers", 4),
            ("Snakes", 3),
            ("Cheetahs", 3),
            ("Panthers", 1)
        ]
        expected_output = (
            "1. Lions, 4 pts\n"
            "1. Tigers, 4 pts\n"
            "3. Snakes, 3 pts\n"
            "3. Cheetahs, 3 pts\n"
            "5. Panthers, 1 pts\n"
        )

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            display_rankings(team_points)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_rankings_no_ties(self):
        team_points = [
            ("Lions", 4),
            ("Tigers", 3),
            ("Snakes", 2),
            ("Cheetahs", 1),
            ("Panthers", 0)
        ]
        expected_output = (
            "1. Lions, 4 pts\n"
            "2. Tigers, 3 pts\n"
            "3. Snakes, 2 pts\n"
            "4. Cheetahs, 1 pts\n"
            "5. Panthers, 0 pts\n"
        )

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            display_rankings(team_points)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
