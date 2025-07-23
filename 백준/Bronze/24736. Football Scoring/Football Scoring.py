T1, F1, S1, P1, C1 = map(int, input().split())
T2, F2, S2, P2, C2 = map(int, input().split())

visiting_team_score = T1*6 + F1*3 + S1*2 + P1 + C1*2
home_team_score = T2*6 + F2*3 + S2*2 + P2 + C2*2

print(visiting_team_score, home_team_score)