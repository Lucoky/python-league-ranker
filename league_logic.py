# league_logic.py

def parse_line(line):
    """
    Parses a single line of input and returns team names and scores.
    """
    try:
        team1_score, team2_score = line.strip().split(", ")
        team1, score1 = team1_score.rsplit(" ", 1)
        team2, score2 = team2_score.rsplit(" ", 1)
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
    for team, points in team_points:
        print(f"{rank}. {team}, {points} pts")
        rank += 1
