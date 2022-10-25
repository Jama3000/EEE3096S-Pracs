  2.6 Software requirements

You need to do the following:
• Set up the EEPROM.
• Create a thread for reading from the ADC. The value read from the temperature sensor
needs to be converted to degrees Celsius. See the datasheet (linked above) for the
formula.
• Create interrupts for all the button functionality (don’t forget to debounce your inputs)
• Create an output signal to trigger the buzzer (bonus marks)
• In the main() loop, print values to the screen as described in Section 2.7
  
  2.7 Description

• By default, the system continuously monitors the sensors every 5s using this format:

Time        Sys-Timer   Temp    Buzzer
10:17:15    00:00:00    25 C    *
10:17:20    00:00:05    25 C
10:17:25    00:00:10    25 C
10:17:30    00:00:15    25 C
10:17:35    00:00:20    25 C
10:17:35    00:00:20    25 C    *

• The stop switch stops or starts the monitoring of the sensors. The system timer is not
affected by this functionality. The screen must also be cleared when logging is stopped,
and a message printed to display to inform the user that the logging has stopped.
