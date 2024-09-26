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
best_profit = 0
best_combination = []
best_cost = 0
enumeration_count = 0

for i in range(len(actions)):
    action1 = actions[i]
    cost1 = action1[1]
    profit1 = (action1[1] * action1[2]) / 100
    enumeration_count += 1

    if cost1 <= max_budget and profit1 > best_profit:
        best_profit = profit1
        best_combination = [action1]
        best_cost = cost1

    for j in range(i + 1, len(actions)):
        action2 = actions[j]
        cost2 = cost1 + action2[1]
        profit2 = profit1 + (action2[1] * action2[2]) / 100
        enumeration_count += 1

        if cost2 <= max_budget and profit2 > best_profit:
            best_profit = profit2
            best_combination = [action1, action2]
            best_cost = cost2

        for k in range(j + 1, len(actions)):
            action3 = actions[k]
            cost3 = cost2 + action3[1]
            profit3 = profit2 + (action3[1] * action3[2]) / 100
            enumeration_count += 1

            if cost3 <= max_budget and profit3 > best_profit:
                best_profit = profit3
                best_combination = [action1, action2, action3]
                best_cost = cost3

            for l in range(k + 1, len(actions)):
                action4 = actions[l]
                cost4 = cost3 + action4[1]
                profit4 = profit3 + (action4[1] * action4[2]) / 100
                enumeration_count += 1

                if cost4 <= max_budget and profit4 > best_profit:
                    best_profit = profit4
                    best_combination = [action1, action2, action3, action4]
                    best_cost = cost4

                for m in range(l + 1, len(actions)):
                    action5 = actions[m]
                    cost5 = cost4 + action5[1]
                    profit5 = profit4 + (action5[1] * action5[2]) / 100
                    enumeration_count += 1

                    if cost5 <= max_budget and profit5 > best_profit:
                        best_profit = profit5
                        best_combination = [action1, action2, action3, action4, action5]
                        best_cost = cost5

                    for n in range(m + 1, len(actions)):
                        action6 = actions[n]
                        cost6 = cost5 + action6[1]
                        profit6 = profit5 + (action6[1] * action6[2]) / 100
                        enumeration_count += 1

                        if cost6 <= max_budget and profit6 > best_profit:
                            best_profit = profit6
                            best_combination = [action1, action2, action3, action4, action5, action6]
                            best_cost = cost6


print("Meilleure combinaison d'actions :")
for action in best_combination:
    print(f"{action[0]} - Coût : {action[1]}€, Bénéfice : {action[2]}%")
print(f"\nCoût total : {best_cost}€")
print(f"Profit total après 2 ans : {best_profit:.2f}€")
print(f"\nNombre total d'énumérations : {enumeration_count}")
