#seven tone with the 3 buttons of maker board
from machine import Pin,PWM

#buzzer/pins are picked for maker pi pico board
pins=[20,21,22]
buzzer = PWM(Pin(18))

def tone( frequency):
    buzzer.freq(int(frequency))
    buzzer.duty_u16(30000)
def tone_stop():
    buzzer.duty_u16(0)

#formula for frequencies: frequency=440×2^(n/12)
#with the built in 3 buttons we can play 7 distinct tones (2^3-1)
tones=[261.63,293.66,329.63,349.23,392,440,493.88]
# C,D,E,F, G,A,B
while True:
    pressed=[0,0,0]
    pinptr=0
    for pinptr in range(len(pins)):
        pin=pins[pinptr]
        button = Pin(pin, Pin.IN, Pin.PULL_DOWN)
        state = button.value()  # 1 = HIGH, 0 = LOW
        if state==0:
            pressed[pinptr]=1
    if pressed==[0,0,0]:
        tone_stop()
        continue
    freqptr=pressed[0]+2*pressed[1]+4*pressed[2]-1
    tone(tones[freqptr])