
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
# import time

def onTemperatureChange(self, temperature):
    print("Temperature: " + str(temperature))

def main():
    temperatureSensor0 = TemperatureSensor()

    temperatureSensor0.setOnTemperatureChangeHandler(onTemperatureChange)

    temperatureSensor0.openWaitForAttachment(5000)

    try:
            input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
            pass

    temperatureSensor0.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
