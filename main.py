def my_function():
    Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
Mbit_IR.on_press_event(RemoteButton.POWER, my_function)

def my_function2():
    for i in range(256):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, i)
        basic.pause(100)
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
Mbit_IR.on_press_event(RemoteButton.TRIGHT, my_function2)

def my_function3():
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RIGHT, 100)
    basic.pause(100)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
Mbit_IR.on_press_event(RemoteButton.RIGHT, my_function3)

def my_function4():
    Tinybit.RGB_Car_Big(Tinybit.enColor.GREEN)
Mbit_IR.on_press_event(RemoteButton.NUM0, my_function4)

def my_function5():
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 255)
    basic.pause(100)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
Mbit_IR.on_press_event(RemoteButton.UP, my_function5)

def my_function6():
    Tinybit.RGB_Car_Big(Tinybit.enColor.WHITE)
Mbit_IR.on_press_event(RemoteButton.LIGHT, my_function6)

def my_function7():
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_LEFT, 100)
    basic.pause(100)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
Mbit_IR.on_press_event(RemoteButton.LEFT, my_function7)

def my_function8():
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_BACK, 255)
    basic.pause(100)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
Mbit_IR.on_press_event(RemoteButton.DOWN, my_function8)

def my_function9():
    for j in range(256):
        # In Youtube use SpinRight
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, j)
        basic.pause(100)
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
Mbit_IR.on_press_event(RemoteButton.TLEFT, my_function9)

def my_function10():
    music.ring_tone(262)
    basic.pause(500)
    music.rest(music.beat(BeatFraction.QUARTER))
Mbit_IR.on_press_event(RemoteButton.BEEP, my_function10)

Mbit_IR.init(Pins.P8)

def on_forever():
    basic.show_string("Hello Tinn")
basic.forever(on_forever)
