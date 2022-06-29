import serial

from libs.Log import *
from libs.ThreadRunnable import *


# dummy class for testing and debugging
class DummySerialHandler(Debugable):

    def __init__(self, timeout=5):
        Debugable.__init__(self)
        self.log_debug_msg(f"Opening serial port ...")
        self.log_debug_msg(f"Serial port opened.")

    def send_cmd(self, cmd):
        print(f"\tSEND: {cmd}")

    def receive_data_hex_lst(self):
        quiet___ = ['7e', 'ff', '06', '42', '00', '04', '00', 'fe', 'b5', 'ef']
        alarming = ['7e', 'ff', '06', '42', '00', '04', '01', 'fe', 'b4', 'ef']
        _FEEDBACK = ['7e', 'ff', '06', '41', '00', '00', '00', 'fe', 'ba', 'ef']
        data = _FEEDBACK
        print(f'\tRECE: {data}')
        return data

    def close_port(self):
        self.log_debug_msg("Closing Serial Port...")
        self.log_debug_msg("Serial Port Closed!")


class DummyAlarmHandler(ThreadRunnable):

    # just to let AlarmHandler have the ability to receive terminating signal
    def exit_nicely(self, *args):
        self.turn_off_alarm()
        self.serial.close_port()

    def on_start(self):
        pass

    def main_body(self):
        self.thread_stop()

    def on_end(self):
        pass

    def __init__(self):
        ThreadRunnable.__init__(self)  # not an actual thread runnable object
        self.serial = DummySerialHandler(timeout=1)
        self.is_alarming = False
        self.alarm_is_enabled = False

    def enable_alarm(self):
        self.alarm_is_enabled = True

    def disable_alarm(self):
        self.alarm_is_enabled = False
        self.turn_off_alarm()

    def turn_on_alarm(self):
        if not self.alarm_is_enabled or self.is_alarming:
            return
        Log.info("Alarm turned on.")
        self.is_alarming = True

    def turn_off_alarm(self):
        if not self.is_alarming:
            return
        Log.info("Alarm turned off.")
        self.is_alarming = False

    def check_alarm(self):
        pass


'''
Commands are for small alarm
'''

# Format：$S VER Len CMD Feedback para1 para2 checksum $O
b_next_ = "7E FF 06 01 00 00 00 EF"
b_prev_ = "7E FF 06 02 00 00 00 EF"


def b_play(n: int):
    return "7E FF 06 03 01 00 " + str(hex(n)).split('x')[1] + " EF"


def b_loop(n: int):
    return "7E FF 06 08 01 00 " + str(hex(n)).split('x')[1] + " EF"


b_volup = "7E FF 06 04 00 00 00 EF"
b_voldn = "7E FF 06 05 00 00 00 EF"
b_reset = "7E FF 06 0C 00 00 00 EF"
b_play_ = "7E FF 06 0D 00 00 00 EF"
b_pause = "7E FF 06 0E 00 00 00 EF"
b_stop_ = "7E FF 06 16 00 00 00 EF"

b_query = "7E FF 06 42 00 00 00 FE B9 EF"

_FEEDBACK = ['7e', 'ff', '06', '41', '00', '00', '00', 'fe', 'ba', 'ef']


class SerialHandler(Debugable):
    @staticmethod
    def cvt_str_to_hex_lst(string: str):
        result = []
        for hex_num in string.split(' '):
            hex_num = '0x' + hex_num
            result.append(eval(hex_num))
        return result

    @staticmethod
    def cvt_hex_lst(num_lst):
        return [hex(n) for n in num_lst]

    def __init__(self, timeout=0.1):
        Debugable.__init__(self)

        Log.info(f"Opening serial port ...")
        self.serial_port = serial.Serial(
            port="/dev/ttyUSB0",
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=timeout
        )
        while not self.serial_port.isOpen():
            time.sleep(1)
            Log.warning(f"Serial port not opened. Waiting for serial port...")
        Log.info(f"Serial port {self.serial_port.name} opened.")

    def send_cmd(self, cmd):
        msg = serial.to_bytes(self.cvt_str_to_hex_lst(cmd))
        self.serial_port.write(msg)

    def receive_data_hex_lst(self):
        data = []
        received = self.serial_port.read().hex()
        while received is not None and len(received) > 0:
            data.append(received)
            if int(data[-1], base=16) == 0xef:
                break
            received = self.serial_port.read().hex()
        return data

    def close_port(self):
        Log.info("Closing Serial Port...")
        self.serial_port.close()
        while self.serial_port.isOpen():
            time.sleep(1)
            self.serial_port.close()
            Log.warning(f"Serial port not closed. Waiting for serial port...")
        Log.info("Serial Port Closed!")


class AlarmHandler:
    """
    For backward compatibility
    """

    def __init__(self):
        # noinspection PyBroadException
        try:
            self.serial = SerialHandler(timeout=1)
        except Exception:
            self.serial = None

    def turn_on_alarm(self):
        if self.serial is not None:
            self.serial.send_cmd(b_play(3))

    def turn_off_alarm(self):
        if self.serial is not None:
            self.serial.send_cmd(b_stop_)

    def __del__(self):
        self.turn_off_alarm()
        self.serial.close_port()
