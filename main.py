number = 0

def on_button_pressed_a():
    global number
    number += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global number
    number += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_number(number)
basic.forever(on_forever)
