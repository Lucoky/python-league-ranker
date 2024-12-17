import argparse
import sys
from league_logic import process_results, display_rankings, parse_line


def main():
    parser = argparse.ArgumentParser(
        description="League Ranking CLI - Calculates and displays league rankings from match results."
    )
    parser.add_argument(
        "-f", "--file", type=str, help="Path to the input file containing match results."
    )

    args = parser.parse_args()

    try:
        if args.file:
            # Read input from file
            with open(args.file, "r") as f:
                input_data = f.readlines()
        else:
            # Read input from stdin
            print("Enter match results (e.g., 'TeamA 1, TeamB 2').")
            print("Press Ctrl+D (Linux/Mac) or Ctrl+Z + Enter (Windows) when done:")
            input_data = []
            while True:
                try:
                    line = input()

                    # Validate input format
                    try:
                        parse_line(line)
                    except ValueError as e:
                        print(f"Error: {e}")
                        print("Please try again.")
                        # Skip invalid input
                        continue

                    if line.strip():  # Only add non-empty lines
                        input_data.append(line)
                except EOFError:
                    break

        rankings = process_results(input_data)
        display_rankings(rankings)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
