# cows and constraints and answer
cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
cows.sort()
cnsts = []
ans = []

N = int(input())
for i in range(N):
    cnst = input().split(" must be milked beside ")
    cnsts.append((cnst[0], cnst[1]))

# make adjacency matrix for cows
cows_adj = [[], [], [], [], [], [], [], []]
for cnst in cnsts:
    cows_adj[cows.index(cnst[0])].append(cnst[1])
    cows_adj[cows.index(cnst[1])].append(cnst[0])

# find all the cows that less than 2 constraints
one_or_none_cnsts = []
for cow_adj in cows_adj:
    if len(cow_adj) < 2:
        one_or_none_cnsts.append(cows_adj.index(cow_adj))
one_or_none_cnsts.sort()

# add the first and last cow to the answer and remove them from the one or none constraints list
ans[0] = one_or_none_cnsts[0]
one_or_none_cnsts.pop(0)
ans.append(one_or_none_cnsts[-1])
one_or_none_cnsts.pop()
