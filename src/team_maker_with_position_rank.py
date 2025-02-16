import random

class Player:
    def __init__(self, name, position, skill_level):
        self.name = name
        if position not in ["공격수", "수비수", "미드필더"]:
            raise ValueError("포지션은 '공격수', '수비수', '미드필더' 중 하나여야 합니다.")
        self.position = position
        self.skill_level = skill_level

    def __repr__(self):
        return f"{self.name}({self.position}, {self.skill_level})"


def divide_teams(position_players, num_teams):
    teams = [[] for _ in range(num_teams)]
    for _position, players in position_players.items():
        random.shuffle(players)
        for i, player in enumerate(players):
            team_index = i % num_teams
            teams[team_index].append(player)
    teams = balance_teams(teams)
    return teams

def balance_teams(teams):
    # 각 팀의 실력 평균을 계산하고, 실력 차이를 맞추기 위한 조정
    team_averages = []

    for team in teams:
        average_skill = sum(player.skill_level for player in team) / len(team)
        team_averages.append(average_skill)

    # 실력 차이가 심한 팀을 찾아서 조정
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            # 실력 평균 차이가 너무 크면 선수 교환을 고려
            if abs(team_averages[i] - team_averages[j]) > 1:
                # 가장 실력 차이가 큰 팀들끼리 교환하여 실력의 균형을 맞춤
                swap_players(teams[i], teams[j])
                # 다시 평균 갱신
                team_averages[i] = sum(player.skill_level for player in teams[i]) / len(teams[i])
                team_averages[j] = sum(player.skill_level for player in teams[j]) / len(teams[j])

    return teams

def swap_players(team1, team2):
    # 두 팀에서 하나씩 선수를 교환
    if team1 and team2:
        player1 = team1.pop()
        player2 = team2.pop()
        team1.append(player2)
        team2.append(player1)

# 예시 사용
players = [
    Player("선수1", "공격수", 8),
    Player("선수2", "수비수", 6),
    Player("선수3", "미드필더", 7),
    Player("선수4", "공격수", 9),
    Player("선수5", "수비수", 9),
    Player("선수6", "미드필더", 6),
    Player("선수7", "공격수", 7),
    Player("선수8", "수비수", 8),
    Player("선수9", "미드필더", 5)
]

position_plyers = {
    position: [player for player in players if player.position == position]
    for position in ["공격수", "수비수", "미드필더"]
}
teams = divide_teams(position_plyers, 3)

# 팀 출력
for i, team in enumerate(teams, 1):
    print(f"팀 {i}: {team}")