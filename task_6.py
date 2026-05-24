items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(budget, menu):
    your_meal = {}
    meals_ratio = {}
    total_calories = 0

    for meal, details in menu.items():
        ratio = details["calories"] / details["cost"]
        meals_ratio[meal] = ratio

    sorted_meals_ratio = dict(sorted(meals_ratio.items(), key=lambda x: x[1], reverse=True))

    for meal in sorted_meals_ratio.keys():
        if menu[meal]["cost"] <= budget:
            your_meal[meal] = menu[meal]["cost"]
            total_calories += menu[meal]["calories"]
            budget -= menu[meal]["cost"]

    return your_meal, total_calories, budget


def dynamic_programming(budget, menu):
    dp = [[0] * (budget + 1) for _ in range(len(menu) + 1)]

    for i, (item, item_info) in enumerate(menu.items(), 1):
        for j in range(1, budget + 1):
            if item_info["cost"] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_info["cost"]] + item_info["calories"])
            else:
                dp[i][j] = dp[i - 1][j]

    optimal_set = []
    j = budget
    for i in range(len(menu), 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            optimal_set.append(list(menu.keys())[i - 1])
            j -= menu[list(menu.keys())[i - 1]]["cost"]

    total_calories = dp[len(menu)][budget]
    return optimal_set, total_calories


def main():
    budget = 500

    print(f"Бюджет: {budget}\n")

    meal, calories, change = greedy_algorithm(budget, items)
    print(f"Жадібний алгоритм:")
    print(f"Меню: {meal}")
    print(f"Калорійність: {calories}")
    print(f"Решта: {change}\n")

    optimal_set, total_calories = dynamic_programming(budget, items)
    print(f"Динамічне програмування:")
    print(f"Меню: {optimal_set}")
    print(f"Калорійність: {total_calories}")


if __name__ == "__main__":
    main()