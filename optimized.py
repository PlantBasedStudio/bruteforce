actions = [
    ("Action-1", 20, 5),
    ("Action-2", 30, 10),
    ("Action-3", 50, 15),
    ("Action-4", 70, 20),
    ("Action-5", 60, 17),
    ("Action-6", 80, 25),
    ("Action-7", 22, 7),
    ("Action-8", 26, 11),
    ("Action-9", 48, 13),
    ("Action-10", 34, 27),
    ("Action-11", 42, 17),
    ("Action-12", 110, 9),
    ("Action-13", 38, 23),
    ("Action-14", 14, 1),
    ("Action-15", 18, 3),
    ("Action-16", 8, 8),
    ("Action-17", 4, 12),
    ("Action-18", 10, 14),
    ("Action-19", 24, 21),
    ("Action-20", 114, 18),
]

max_budget = 500

n = len(actions)
# Matrice = Stockage de combinaisons (tableau sur 2 dimension)
dp = [[0] * (max_budget + 1) for _ in
      range(n + 1)]  # Ici dp[i][w] représente la matrice de la meilleure combinaison action/budget
# n+1 = une ligne par action + ligne vide (0)


enumeration_count = 0

for i in range(1, n + 1):
    name, cost, benefit = actions[i - 1]  # 0,1,2,3... par ex Action -1, 20, 5
    profit = (cost * benefit) / 100  # (20 * 5) * 100 = 1.0
    for w in range(max_budget + 1):  # Budget de 0 a 500
        enumeration_count += 1
        if cost <= w:
            # noinspection PyTypeChecker
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + profit)
        else:
            dp[i][w] = dp[i - 1][w]

best_profit = dp[n][max_budget]
w = max_budget
best_combination = []

for i in range(n, 0,
               -1):  # On parcourt les actions en sens inverse pour determiner si la matrice est différente et déterminer la meilleure action. On incrémente alors ça dans best_combination
    if dp[i][w] != dp[i - 1][w]:
        name, cost, benefit = actions[i - 1]
        best_combination.append(actions[i - 1])
        w -= cost

print("Meilleure combinaison d'actions :")
for action in best_combination:
    print(f"{action[0]} - Coût : {action[1]}€, Bénéfice : {action[2]}%")
print(f"\nCoût total : {sum(a[1] for a in best_combination)}€")
print(f"Profit total après 2 ans : {best_profit:.2f}€")
print(f"\nNombre total d'énumérations : {enumeration_count}")
