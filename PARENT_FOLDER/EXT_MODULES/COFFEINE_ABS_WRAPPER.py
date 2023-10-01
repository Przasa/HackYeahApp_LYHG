import random
import threading
import time
import queue

import SHARED_MODULES.shared_data as shared_data
from EXT_MODULES.CaffeineAbsorbers import main as caffeine_main

MAX_PULSE= 200
MIN_PULSE=50


class COFFEEInterface:

    def __init__(self) -> None:
        pass

    def StartMeasure(self):
        self.measure_thread = threading.Thread(target=caffeine_main.main_algo)
        self.measure_thread.start()





