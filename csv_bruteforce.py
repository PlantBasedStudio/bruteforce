import csv

actions = []


def load_actions_from_csv(file_path_):
    with open(file_path_, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            name = row[0]
            cost = float(row[1])
            benefit = float(row[2])
            if cost > 0:
                actions.append((name, cost, benefit))
    return actions


def best_investment(_actions, _max_budget):
    n = len(_actions)
    max_budget_centimes = int(_max_budget * 100)
    dp = [[0] * (max_budget_centimes + 1) for _ in range(n + 1)]
    _enumeration_count = 0

    for i in range(1, n + 1):
        name, cost, benefit = actions[i - 1]
        cost_centimes = int(cost * 100)
        profit = cost * (benefit / 100) * 2

        if cost_centimes > max_budget_centimes:
            continue

        for w in range(max_budget_centimes + 1):
            _enumeration_count += 1
            if cost_centimes <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost_centimes] + profit)
            else:
                dp[i][w] = dp[i - 1][w]

    _best_profit = dp[n][max_budget_centimes]
    w = max_budget_centimes
    _best_combination = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, cost, benefit = actions[i - 1]
            _best_combination.append(actions[i - 1])
            w -= int(cost * 100)

    return _best_combination, _best_profit, _enumeration_count


file_path = "dataset2_Python+P7.csv"
actions = load_actions_from_csv(file_path)
max_budget = 500

best_combination, best_profit, enumeration_count = best_investment(actions, max_budget)


print("Meilleure combinaison d'actions :")
for action in best_combination:
    print(f"{action[0]} - Coût : {action[1]}€, Bénéfice : {action[2]}%")
print(f"\nCoût total : {sum(a[1] for a in best_combination)}€")
print(f"Profit total après 2 ans : {best_profit:.2f}€")
print(f"\nNombre total d'énumérations : {enumeration_count}")
