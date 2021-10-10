from turtle import Turtle, Screen
import random
screen = Screen()
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
# Set width and height of screen
screen.setup(width=500, height=400)
all_turtles = []
is_race_on = False
user_bet = screen.textinput(title="Make your Bet!", prompt="Which turtle will win the race? Enter a colour: ").lower()
# print(user_bet)
num = 0
y_positions = [-70, -40, -10, 20, 50, 80]
position = 0

for _ in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[num])
    y = y_positions[position]
    new_turtle.goto(x=-230, y=y)
    num += 1
    position += 1
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            is_race_on = False
            winner = i.pencolor()
            if winner == user_bet:
                print(f"You have won! The {winner} turtle is the winner!")
            else:
                print(f"You lose! The {winner} turtle is the winner!")

            break
        move_distance = random.randint(0, 10)
        i.forward(move_distance)

screen.exitonclick()
