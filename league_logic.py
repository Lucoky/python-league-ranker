# league_logic.py

def parse_line(line):
    """
    Parses a single line of input and returns team names and scores.
    """
    try:
        team1_score, team2_score = line.strip().split(", ")
        team1, score1 = team1_score.rsplit(" ", 1)
        team2, score2 = team2_score.rsplit(" ", 1)

        if (team1 == team2):
            raise ValueError("Teams cannot play against themselves")

        if (not score1.isdigit() or not score2.isdigit()):
            raise ValueError("Scores must be integers")

        if (int(score1) < 0 or int(score2) < 0):
            raise ValueError("Scores cannot be negative")

        return team1, int(score1), team2, int(score2)
    except ValueError:
        raise ValueError("Invalid input format. Use: 'TeamA 1, TeamB 2'")

def update_points(team_points, team1, score1, team2, score2):
    """
    Updates team points based on match scores.
    """
    if score1 > score2:
        team_points[team1] = team_points.get(team1, 0) + 3
        team_points[team2] = team_points.get(team2, 0)
    elif score1 < score2:
        team_points[team2] = team_points.get(team2, 0) + 3
        team_points[team1] = team_points.get(team1, 0)
    else:  # It's a draw
        team_points[team1] = team_points.get(team1, 0) + 1
        team_points[team2] = team_points.get(team2, 0) + 1

def process_results(input_data):
    """
    Process match results to calculate and return the league rankings.
    """
    team_points = {}

    # Parse and update points
    for line in input_data:
        team1, score1, team2, score2 = parse_line(line)
        update_points(team_points, team1, score1, team2, score2)

    # Return sorted rankings
    return sorted(team_points.items(), key=lambda x: (-x[1], x[0]))

def display_rankings(team_points):
    """
    Displays the team rankings.
    """
    rank = 1
    prev_points = None
    displayed_rank = 1

    for i, (team, points) in enumerate(team_points):
        # If the current points are the same as the previous, keep the rank the same
        if points != prev_points:
            displayed_rank = rank

        print(f"{displayed_rank}. {team}, {points} pts")

        prev_points = points
        rank += 1
