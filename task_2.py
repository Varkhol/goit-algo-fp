import turtle
import math


def pythagoras_tree(t, branch_length, order):
    if order == 0:
        return

    t.forward(branch_length)
    t.left(45)
    pythagoras_tree(t, branch_length * math.cos(math.radians(45)), order - 1)
    t.right(90)
    pythagoras_tree(t, branch_length * math.cos(math.radians(45)), order - 1)
    t.left(45)
    t.backward(branch_length)


def draw_pythagoras_tree(order, size=120):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title(f"Дерево Піфагора — рівень рекурсії: {order}")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)
    t.color("#2d6a4f")
    t.pensize(2)

    pythagoras_tree(t, size, order)

    t.hideturtle()

    try:
        screen.mainloop()
    except turtle.Terminator:
        pass
    finally:
        try:
            turtle.bye()
        except turtle.Terminator:
            pass


if __name__ == "__main__":
    while True:
        while True:
            try:
                order = int(input("Введіть рівень рекурсії (бажано не більше 10): "))
                if order < 0:
                    print("Значення не може бути від'ємним. Спробуйте ще раз.")
                else:
                    break
            except ValueError:
                print("Будь ласка, введіть ціле число.")

        draw_pythagoras_tree(order)

        again = input("Намалювати ще раз? (y/n): ").strip().lower()
        if again != "y":
            break