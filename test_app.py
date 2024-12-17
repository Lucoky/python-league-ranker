import unittest
from league_logic import parse_line, process_results

class TestLeagueLogic(unittest.TestCase):
    def test_parse_line_valid(self):
        line = "Lions 3, Snakes 3"
        result = parse_line(line)
        self.assertEqual(result, ("Lions", 3, "Snakes", 3))

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

if __name__ == "__main__":
    unittest.main()
