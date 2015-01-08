import RPi.GPIO as GPIO
from time import sleep

data = 18
clock = 23
latch = 24
chain = 2


def init(data_pin=18, clock_pin=23, latch_pin=24, chain_number=1):
    global data, clock, latch, chain
    data = data_pin
    clock = clock_pin
    latch = latch_pin
    chain = chain_number
    setup()


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(data, GPIO.OUT)
    GPIO.setup(clock, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(latch, GPIO.OUT, initial=GPIO.LOW)
    write_all(0)


def write_latch():
    GPIO.output(latch, 1)
    GPIO.output(latch, 0)


def push_bit(bit):
    GPIO.output(clock, 0)
    GPIO.output(data, bit)
    GPIO.output(clock, 1)


def write_all(val):
    for i in range(8*chain):
        push_bit(val)
    write_latch()


def get_bit(value, n):
    if value & (1 << n):
        return 1
    else:
        return 0


def write(value):
    if value.bit_length() > (8*chain):
        raise ValueError("Tried to write more bits than available")
    for i in reversed(range(8*chain)):
        push_bit(get_bit(value, i))
    write_latch()


def test_pins():
    for i in range(8*chain):
        write(pow(2, i))
        sleep(.125)
