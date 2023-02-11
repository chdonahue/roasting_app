from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
import time

def onTemperatureChange(self, temperature):
	converted_temp = 9/5*temperature + 32
	print("Temperature: " + str(converted_temp))

def main():
	temperatureSensor0 = TemperatureSensor()

	temperatureSensor0.setOnTemperatureChangeHandler(onTemperatureChange)

	temperatureSensor0.openWaitForAttachment(5000)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	temperatureSensor0.close()

main()
