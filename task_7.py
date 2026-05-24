import random
import matplotlib.pyplot as plt


def main():
    num_of_throws = 1000000

    analytical = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

    result = {}
    for _ in range(num_of_throws):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        sum_of_dices = dice_1 + dice_2
        if sum_of_dices in result.keys():
            result[sum_of_dices] += 1
        else:
            result[sum_of_dices] = 1

    probability = {}
    for dice, throws in result.items():
        probability[dice] = throws / num_of_throws

    sorted_result = dict(sorted(result.items()))
    sorted_probability = dict(sorted(probability.items()))

    # Кількість випадань кожної суми
    print(f"\n{'Сума':<6} | {'Кількість':<12}")
    print("-" * 22)
    for dice, count in sorted_result.items():
        print(f"{dice:<6} | {count:<12}")

    # Таблиця порівняння з аналітичними значеннями
    print(f"\n{'Сума':<6} | {'Монте-Карло':<14} | {'Аналітична':<14} | {'Різниця':<10}")
    print("-" * 52)
    for dice, prob in sorted_probability.items():
        an = analytical[dice]
        diff = abs(prob - an)
        print(f"{dice:<6} | {prob:<14.2%} | {an:<14.2%} | {diff:<10.2%}")

    sums = list(sorted_probability.keys())
    mc_values = [sorted_probability[s] for s in sums]
    an_values = [analytical[s] for s in sums]

    x = range(len(sums))
    width = 0.35

    plt.bar([i - width/2 for i in x], mc_values, width, label="Монте-Карло", color="#E8636E")
    plt.bar([i + width/2 for i in x], an_values, width, label="Аналітична", color="#4A90D9")
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.xticks(list(x), sums)
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()