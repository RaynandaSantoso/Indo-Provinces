import turtle
import pandas as pd

guessed_province = []

screen = turtle.Screen()
screen.title("Tebak Provinsi Indonesia")
image = "Indonesia_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("Province Indonesia Coords - Sheet1.csv")
list_province = data.Provinces.to_list()

while len(guessed_province) < len(list_province):
    user_guess = str.title(screen.textinput(f"{len(guessed_province)}/{len(list_province)} Provinces Guessed", "Make a guess"))

    if user_guess == "Exit":
        missed_province = [provinsi for provinsi in list_province if provinsi not in guessed_province]
        df = pd.DataFrame(missed_province)
        df.to_csv("Provinsi Yang Belum Hafal.csv")
        break

    if user_guess in list_province:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.Provinces == user_guess]
        t.goto(int(province_data.X), int(province_data.Y))
        t.write(province_data.Provinces.item(), font=("Arial", 12, 'normal'))
        guessed_province.append(user_guess)



screen.exitonclick()
