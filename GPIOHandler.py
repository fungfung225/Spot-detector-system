import threading
import time

from libs.Log import Log


class DummyGPIO:
    BCM = "BCM"
    HIGH = "HIGH"
    LOW = "LOW"
    OUT = "OUT"
    IN = "IN"
    PIN = {}

    @staticmethod
    def setwarnings(v: bool):
        Log.info(f"set warnings: {v}")

    @staticmethod
    def setmode(v):
        Log.info(f"set mode: {v}")

    @staticmethod
    def setup(pin, mode, initial="LOW"):
        Log.info(f"setup pin={pin} set to {mode}, init = {initial}")
        DummyGPIO.PIN[pin] = initial

    @staticmethod
    def output(pin, v):
        if DummyGPIO.PIN[pin] != v:
            Log.info(f"output pin={pin}: {v}")
        DummyGPIO.PIN[pin] = v

    @staticmethod
    def input(pin):
        if pin not in DummyGPIO.PIN:
            DummyGPIO.PIN[pin] = 0
        return DummyGPIO.PIN[pin]

    @staticmethod
    def cleanup():
        Log.info(f"Clean up GPIO")


try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = DummyGPIO

LED_PIN = 21

ALARM_PIN = 22
ALARM_HIGH_TIME = 2.5
ALARM_LOW_TIME = .5

SIGNAL_PIN = 23
SIGNAL_TIME = 2


class GPIOHandler:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT,    initial=GPIO.HIGH)
        GPIO.setup(ALARM_PIN, GPIO.OUT,  initial=GPIO.LOW)
        GPIO.setup(SIGNAL_PIN, GPIO.OUT, initial=GPIO.LOW)
        self.alarm_timer = time.time()
        self.sending_signal = False

    def _send_signal(self):
        self.sending_signal = True
        self.signal_high()
        time.sleep(SIGNAL_TIME)
        self.signal_low()
        self.sending_signal = False

    def send_signal(self):
        if not self.sending_signal:
            t = threading.Thread(target=self._send_signal)
            t.setDaemon(True)
            t.start()

    @staticmethod
    def signal_high():
        GPIO.output(SIGNAL_PIN, GPIO.HIGH)

    @staticmethod
    def signal_low():
        GPIO.output(SIGNAL_PIN, GPIO.LOW)

    @staticmethod
    def alarm_high():
        GPIO.output(ALARM_PIN, GPIO.HIGH)

    @staticmethod
    def alarm_low():
        GPIO.output(ALARM_PIN, GPIO.LOW)

    @staticmethod
    def cleanup():
        GPIO.cleanup()


if __name__ == '__main__':
    gh = GPIOHandler()
    gh.alarm_high()
    time.sleep(30)
    gh.cleanup()
