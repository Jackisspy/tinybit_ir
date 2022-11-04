Mbit_IR.onPressEvent(RemoteButton.Power, function () {
    Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
})
Mbit_IR.onPressEvent(RemoteButton.TRight, function () {
    for (let i = 0; i <= 255; i++) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, i)
        basic.pause(100)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
    }
})
Mbit_IR.onPressEvent(RemoteButton.Right, function () {
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Right, 100)
    basic.pause(100)
    Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
})
Mbit_IR.onPressEvent(RemoteButton.NUM0, function () {
    Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
})
Mbit_IR.onPressEvent(RemoteButton.Up, function () {
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 255)
    basic.pause(100)
    Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
})
Mbit_IR.onPressEvent(RemoteButton.Light, function () {
    Tinybit.RGB_Car_Big(Tinybit.enColor.White)
})
Mbit_IR.onPressEvent(RemoteButton.Left, function () {
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Left, 100)
    basic.pause(100)
    Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
})
Mbit_IR.onPressEvent(RemoteButton.Down, function () {
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Back, 255)
    basic.pause(100)
    Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
})
Mbit_IR.onPressEvent(RemoteButton.TLeft, function () {
    for (let i = 0; i <= 255; i++) {
        // In Youtube use SpinRight
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinLeft, i)
        basic.pause(100)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
    }
})
Mbit_IR.onPressEvent(RemoteButton.BEEP, function () {
    music.ringTone(262)
    basic.pause(500)
    music.rest(music.beat(BeatFraction.Quarter))
})
Mbit_IR.init(Pins.P8)
basic.forever(function () {
    basic.showString("Hello Tinn")
})
