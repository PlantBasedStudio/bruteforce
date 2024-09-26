import itertools

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


def calculate_profit(selected_actions):
    total_cost = sum(action[1] for action in selected_actions)
    total_profit = sum((action[1] * action [2] / 100) for action in selected_actions)
    return total_cost, total_profit


def best_result():
    best_combination = []
    best_profit = 0
    best_cost = 0

    for i in range(1, len(actions) + 1):
        for combination in itertools.combinations(actions, i):
            total_cost, total_profit = calculate_profit(combination)

            if total_cost <= max_budget:
                if total_profit > best_profit:
                    best_combination = combination
                    best_profit = total_profit
                    best_cost = total_cost

    return best_combination, best_cost, best_profit

combinations, cost, profit = best_result()

print("Best combination :")
for action in combinations:
    print(f"{action[0]} - Cost : {action[1]}€, Profit : {action[2]}%")
print(f"\n Total Cost : {cost}€")
print(f"Total profit after 2 years : {profit:.2f}€")