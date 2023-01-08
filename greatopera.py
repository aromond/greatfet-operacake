"""
This script just takes one argument and sets one of 4 options 

the init argument initializes the operacake on first startup

A0<>A1 and B0<>B1
A0<>A2 and B0<>B2
A0<>A3 and B0<>B3
A0<>A4 and B0<>B4
"""
import sys
from greatfet import GreatFET

gf = GreatFET()

if sys.argv[1] == "init" :
  gf.i2c.write(0x18,[0x01,0x86])
  gf.i2c.write(0x18,[0x01,0x87])
  gf.i2c.write(0x18,[0x03,1])
if sys.argv[1] == "1" :
  gf.i2c.write(0x18,[0x01,0x87])
elif sys.argv[1] == "2" :
  gf.i2c.write(0x18,[0x01,0xAF])
elif sys.argv[1] == "3" :
  gf.i2c.write(0x18,[0x01,0xD7])
elif sys.argv[1] == "4" :
  gf.i2c.write(0x18,[0x01,0xFF])
