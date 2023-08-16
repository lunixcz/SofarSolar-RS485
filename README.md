# SofarSolar-RS485 (for HYD 5-20K-3PH)

check_inverter.py - Script for reading and printing values from Sofar Solar HYD 5K-20KTL-3PH via RS485
#REQUIRED pymodbus          3.4.1 from PIP, dist 3.0.0 complains about usage of unit=

HYD 5-20K-3PH Modbus (Client).xlsx - Registry documentation from Sofar support


# Checklist
1/ Physical connection
RS485+ should be connected to PIN 1 or 2, RS485- should be connected to PIN 3 or 4
The remaining PINs should be terminated using 120 Ohm resistor. This might work fine without the resistor too.

I use PINs 2+,3- and I have resistor conneted in between 1 and 4, it's the easiest option how to physically connected to resistor.

I use this cheap USB to RS485 converter:
https://www.aliexpress.com/item/1005004947333084.html?spm=a2g0o.order_list.order_list_main.96.78941802BSRB7n
Original Industrial USB to RS485 Serial Converter Half Duplex FT232RL Communication Module CH343G Industrial Win8 10 Linux Mac

I use FTP cable and using one pair for + and another pair for - as the single wires are very tiny.


2/ Invertor settings
Under communication options make sure the baud rate and client ID matches the values in the script.

ID 01 on inverter should be configured as 0x01 in the script.

3/ Unreliable comm
The communication is not reliable, that means sometimes read error occurs. I've put all in while cycle an in case of some read fails the script reads all values again before printing them. In my case approx 1 in 10 tries fails.
