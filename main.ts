let number = 0
input.onButtonPressed(Button.A, function () {
    number += 1
})
input.onButtonPressed(Button.B, function () {
    number += -1
})
basic.forever(function () {
    basic.showNumber(number)
})
