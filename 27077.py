# https://www.acmicpc.net/problem/27077
import sys
from functools import cmp_to_key
input = lambda : sys.stdin.readline().replace("\n", "")
#print = lambda x: sys.stdout.write(str(x))

korea = "korea"
uruguay = "uruguay"
ghana = "ghana"
portugal = "portugal"


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

class TeamRapper:
    def __init__(self,
                 team_korea: Team,
                 team_uruguay: Team,
                 team_ghana: Team,
                 team_portugal: Team):
        self.team_korea = team_korea
        self.team_uruguay = team_uruguay
        self.team_ghana = team_ghana
        self.team_portugal = team_portugal

        self.score_korea = 0
        self.score_uruguay = 0
        self.score_ghana = 0
        self.score_portugal = 0

    def goal(self, key: str):
        if key == korea:
            self.team_korea.gain_score += 1
            self.team_portugal.lose_score += 1
            self.score_korea += 1
        elif key == uruguay:
            self.team_uruguay.gain_score += 1
            self.team_ghana.lose_score += 1
            self.score_uruguay += 1
        elif key == ghana:
            self.team_ghana.gain_score += 1
            self.team_uruguay.lose_score += 1
            self.score_ghana += 1
        elif key == portugal:
            self.team_portugal.gain_score += 1
            self.team_korea.lose_score += 1
            self.score_portugal += 1

    def end_game(self):
        bonus_korea = 0
        bonus_uruguay = 0
        bonus_ghana = 0
        bonus_portugal = 0

        if self.score_korea > self.score_portugal:
            bonus_korea = 3
        elif self.score_korea < self.score_portugal:
            bonus_portugal = 3
        else:
            bonus_korea = 1
            bonus_portugal = 1

        if self.score_uruguay > self.score_ghana:
            bonus_uruguay = 3
        elif self.score_uruguay < self.score_ghana:
            bonus_ghana = 3
        else:
            bonus_uruguay = 1
            bonus_ghana = 1

        teams = [(self.team_korea, bonus_korea),
                 (self.team_uruguay, bonus_uruguay),
                 (self.team_ghana, bonus_ghana),
                 (self.team_portugal, bonus_portugal)]

        teams.sort(key=cmp_to_key(compare), reverse=True)

        korea_ind = 0
        for ind, (team, bonus) in enumerate(teams):
            if str(team)==korea:
                korea_ind = ind
                break
        return "cry" if (0 <= korea_ind <= 1) and compare(teams[korea_ind], teams[2]) > 0 else "unhappy"

def compare(t1, t2):
    team1, bonus1 = t1
    team2, bonus2 = t2

    if team1.win_score+bonus1 > team2.win_score+bonus2:
        return 1
    elif team1.win_score+bonus1 < team2.win_score+bonus2:
        return -1
    else:
        if (team1.gain_score-team1.lose_score) > (team2.gain_score-team2.lose_score):
            return 1
        elif (team1.gain_score-team1.lose_score) < (team2.gain_score-team2.lose_score):
            return -1
        else:
            if team1.gain_score > team2.gain_score:
                return 1
            elif team1.gain_score < team2.gain_score:
                return -1
            else:
                return 0


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
    teamRapper = TeamRapper(*teams)

    # Compute
    result.append(teamRapper.end_game())
    for goal_team in score:
        teamRapper.goal(goal_team)
        result.append(teamRapper.end_game())

    # Print
    print("\n".join(result))