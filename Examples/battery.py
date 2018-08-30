#!/usr/bin/python

from pijuice import PiJuice

pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
print pijuice.status.GetStatus()[4]
