# https://www.acmicpc.net/problem/27077
import sys
from copy import deepcopy
input = sys.stdin.readline
#print = lambda x: sys.stdout.write(str(x))

korea = "korea"
uruguay = "uruguay"
ghana = "ghana"
portugal = "portugal"

cry = "cry"
unhappy = "unhappy"

class Team:
    def __init__(self,
                 teamname: str,
                 gain_score: int = 0,
                 lose_score: int = 0,
                 win_score: int = 0):
        self.teamname = teamname
        self.gain_score = gain_score
        self.lose_score = lose_score
        self.win_score = win_score

    def __str__(self):
        return self.teamname


class Game:
    def __init__(self,
                 team1: Team,
                 team2: Team):
        self.team1 = team1
        self.team2 = team2

        self.team1_score = 0
        self.team2_score = 0

    def goal_team1(self):
        self.team1.gain_score += 1
        self.team2.lose_score += 1
        self.team1_score += 1

    def goal_team2(self):
        self.team2.gain_score += 1
        self.team1.lose_score += 1
        self.team2_score += 1

    def end_game(self):
        if self.team1_score > self.team2_score:
            self.team1.win_score += 3
        elif self.team1_score < self.team2_score:
            self.team2.win_score += 3
        else:
            self.team1.win_score += 1
            self.team2.win_score += 1

def sort_key(team: Team) -> int:
    score = 10000*10000*team.win_score
    score += 10000*(team.gain_score-team.lose_score)
    score += team.gain_score
    return score

if __name__ == "__main__":
    # Initialize Variable
    teams = []
    score = []
    result = []

    # Input
    for teamname in [korea, uruguay, ghana, portugal]:
        teams.append(Team(teamname, *map(int, input().split())))
    N = int(input())
    for _ in range(N):
        score.append(input())

    # Compute
    game_kp = Game(teams[0], teams[3])
    game_ug = Game(teams[2], teams[1])

    teams.sort(key=sort_key, reverse=True)
    print(list(map(str, teams)))
    result.append("cry" if korea == str(teams[0]) or korea == str(teams[1]) else "unhappy")

    for goal_team in score:
        if goal_team == korea:
            game_kp.goal_team1()
        elif goal_team == portugal:
            game_kp.goal_team2()
        elif goal_team == uruguay:
            game_ug.goal_team1()
        else:
            game_ug.goal_team2()

        old_teamlist = deepcopy(teams)

        game_kp.end_game()
        game_ug.end_game()

        teams = [game_kp.team1, game_kp.team2, game_ug.team1, game_ug.team2]
        teams.sort(key=sort_key, reverse=True)
        print(list(map(str, teams)))
        result.append("cry" if korea == str(teams[0]) or korea == str(teams[1]) else "unhappy")

        teams = old_teamlist
    # Print
    print("\n".join(result))
