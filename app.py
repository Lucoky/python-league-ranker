import argparse
import sys
from league_logic import process_results, display_rankings


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
            print("Enter match results (e.g., 'TeamA 1, TeamB 2'). Press Ctrl+D when done:")
            input_data = sys.stdin.readlines()

        rankings = process_results(input_data)
        display_rankings(rankings)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
