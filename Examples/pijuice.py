from pijuice import PiJuice # Import pijuice module
pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
print pijuice.status.GetChargeLevel()[data] # Read PiJuice staus.
