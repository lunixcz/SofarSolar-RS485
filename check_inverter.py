#script for reading values from Sofar Solar HYD 5K-20KTL-3PH via RS485
#REQUIRED pymodbus          3.4.1 from PIP, dist 3.0.0 complains about usage of unit=
from pymodbus.client import ModbusSerialClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder, Endian

client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=2, stopbits = 1, bytesize = 8,  parity='N', baudrate= 9600)
client.connect()
idslave = 0x01

def read_register(address,idslave,count):
     global success
     try:
          result  = client.read_holding_registers(unit=idslave,address=address,count=count)
          decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)
     except:
          print('read error')
          success=False
     else:
          return decoder.decode_16bit_int()

success=False

while success==False:
     success=True

     griddraw=read_register(0x0488,idslave,1)
     pv1draw=read_register(0x0586,idslave,1)
     pv1voltage=read_register(0x0584,idslave,1)
     bat1draw=read_register(0x0606,idslave,1)
     bat1charge=read_register(0x0608,idslave,1)
     bat1max=read_register(0x060A,idslave,1)
     bat1temp=read_register(0x0607,idslave,1)
     bat1cycles=read_register(0x060A,idslave,1)

print('DRAW GRID(+sell/-buy)',griddraw*10)
print('DRAW PV1',pv1draw*10)
print('DRAW BAT1(+charge/-discharge)',bat1draw*10)
print('TOTAL CONSUMPTION',griddraw*10*-1+pv1draw*10+bat1draw*10*-1)
print('PV1 voltage', pv1voltage)
print('BAT1 charge', bat1charge)
print('BAT1 max', bat1max)
print('BAT1 cycles', bat1cycles)