import random
from dataclasses import dataclass, field


@dataclass
class TeamMaker:
    players: list = field(default_factory=list)

    def make_teams(self, n_team):
        random.shuffle(self.players)
        teams = {i: [] for i in range(n_team)}
        for player in self.players:
            team = min(teams, key=lambda x: len(teams[x]))
            teams[team].append(player)
        return teams.values()


    def make_teams_with_seed(self, seed, n_team):
        random.seed(seed)
        return self.make_teams(n_team)


if __name__=="__main__":
    players = ["player1", "player2", "player3", "player4", "player5", "player6", "player7", "player8"]
    n_team = 3
    tm = TeamMaker(players)

    teams = tm.make_teams(n_team)
    print(f"참여자 명단: {', '.join(players)}")
    for i, team in enumerate(teams):
        print(f"{i+1}팀: {', '.join(team)}")
