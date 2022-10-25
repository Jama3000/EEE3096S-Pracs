                                                                                      
import busio
import digitalio
import board
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import threading
import datetime
import time
import math
#import analogio
from os import system, name

import ES2EEPROMUtils

#set GPIO mode
GPIO.setmode(GPIO.BCM)

startTime = datetime.datetime.now()

sleep = 0
#buzzer = 13
pwm = None
c=0
ss = 1
switch = 1

eeprom = ES2EEPROMUtils.ES2EEPROM()
storage = [] #temperature storage array
i = 0

    # create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

    # create the mcp object
mcp = MCP.MCP3008(spi, cs)

    # create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
    #pin = AnalogIn(board.CE1)

def startUp():
    global pwm

    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(17, GPIO.FALLING, callback=alterSample, bouncetime=200)

    GPIO.setup(13,GPIO.OUT)
    pwm = GPIO.PWM(13,50)
    pass
#    GPIO.output(buzzer,GPIO.LOW)
#    if GPIO.input(17)==1:
#        print("HIGH")
#    print( 'Raw ADC Value:  ', chan.value)
#    print( 'ADC Voltage:  ' + str(chan.voltage) + 'V')

    #if board.17:
    #    print("GPIO is high")
    #else:
    #    print("GPIO is LOW")

def print_time():

    global sleep,c,switch,ss,i,storage

    thread = threading.Timer(5,print_time)
    thread.daemon = True
#    time.sleep(sleep)
    thread.start()
    endTime = datetime.datetime.now()
    runtime = (endTime-startTime)
    runtime = runtime - datetime.timedelta(microseconds=runtime.microseconds)
    temp = round(((1000*chan.voltage)-500)/10)

    if ss == 1:

        #print(datetime.datetime.now().strftime("%H:%M:%S"),"\t",(runtime),"\t",str(temp),"C")

        if i<20:
            storage.append(temp)
            eeprom.write_block(i,temp)
            i=i+1
        elif i==20:
            storage.popleft(0)
            storage.append(temp)
            st = storage

        for i in range(20):
            item = st.popleft()
            eeprom.write_block(i,[item])


        if runtime.seconds==0:
            c = c+1
            pwm.start(10)
            print(datetime.datetime.now().strftime("%H:%M:%S"),"\t",(runtime),"\t",str(temp),"C","\t","*")
        elif runtime.seconds%20==0:
            c = c+1
            pwm.start(10)
            print(datetime.datetime.now().strftime("%H:%M:%S"),"\t",(runtime),"\t",str(temp),"C","\t","*")
        else:
            c = c+1
            pwm.stop()
            print(datetime.datetime.now().strftime("%H:%M:%S"),"\t",(runtime),"\t",str(temp),"C")

    elif ss == 0:
        _ = system('clear')
 #   sleep = 0

def alterSample(ch):

    global ss, switch
    #sleep = 2
    #return sleep
    if GPIO.event_detected(ch):

    global ss, switch
    #sleep = 2
    #return sleep
    if GPIO.event_detected(ch):
        if switch == 1:
          ss = 0
          switch = 0
        elif switch == 0:
          ss = 1
          switch = 1
     #     return interval
      #  elif interval == 5:
       #   interval = 1
        #  return interval
       # interval = 10
        #return sleep
    pass

if __name__ == "__main__":

    print("Time","\t\t","Runtime","\t","Temp","\t","Buzzer")
    startUp()
    print_time()
    while True:
        pass

#    if board.GPIO17:
#        print("HIGH")



