import vxi11
import time

psu = vxi11.Instrument("192.168.150.145")
print(psu.ask("*IDN?"))

input("press Enter to continue")

v_set = input("Input Charge Voltage:")
i_set = input("Input Charge Current:")
i_cutoff = input("Input Cutoff Current:")

psu.write(":INST CH1")
psu.write(":CURR " + i_set)
psu.write(":VOLT " + v_set)

input("Confirm channel settings, and press ENTER to begin")

psu.write(":OUTP CH1,ON")

# wait for it to stabilize

time.sleep(1)

while(float(psu.ask(":MEASure:CURRent? CH1")) > float(i_cutoff)):
  print(psu.ask(":MEAS:VOLT? CH1"),"V")
  print(psu.ask(":MEAS:CURR? CH1"),"A")
  print("\n")
  time.sleep(1)

print("FINISHED. Turning off output.")

psu.write(":OUTP CH1,OFF")

input("Verify shutdown, press ENTER to close.")
