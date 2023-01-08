"""
Big thanks to bkobe for his assistance in deciphering the registers I needed to send to

This script just takes one argument and sets one of 4 options 

the init argument initializes the operacake on first startup

A0<>A1 and B0<>B1
A0<>A2 and B0<>B2
A0<>A3 and B0<>B3
A0<>A4 and B0<>B4

The device Address is 0x18

The register values to set ports are comprised of 8 bits. Set the 8 bits you want accordingly and then send it as a hex value via i2c

+---------------------------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------------+-------------+------------+
|             x             |           x           |           x           |           x           |           x           |              x              |      x      |     x      |
+---------------------------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------------+-------------+------------+
| gpio disable(1) enable(0) | A side 2 bits for 0-3 | A side 2 bits for 0-3 | B side 2 bits for 0-3 | B side 2 bits for 0-3 | Sameside(1) or Crossover(2) | LED Enable2 | LED Enable |
+---------------------------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------------+-------------+------------+


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
