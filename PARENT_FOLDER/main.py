import time
import queue
import numpy as np

import SHARED_MODULES.shared_data as shared_data
from TESTING import dummy
from EXT_MODULES.HRATE_WRAPPER import HrateInterface
from EXT_MODULES.FLAPPY_WRAPPER import FlappyInterface
from EXT_MODULES.COFFEINE_ABS_WRAPPER import COFFEEInterface

def main():
    flappy_iface = FlappyInterface()
    hrate_iface = HrateInterface()
    coffe_iface=  COFFEEInterface()
    
    flappy_iface.StartFlappy()
    
    coffe_iface.StartMeasure()

    # hrate_iface.StartMeasure_fake()
    # read_hrate(duration=10,frequency=5)
    # read_hrate(duration=np.inf)
    # hrate_iface.StopMeasure_fake()
 

def read_hrate(duration=5,frequency=1):

    if duration==np.inf:
        while True:
            try:
                data_from_thread = shared_data.data_queue.get(block=False)  # Non-blocking get
                print("Received HR: {:2f}".format(data_from_thread))
            except queue.Empty:
                print("No data in the queue.")
            time.sleep(1/frequency)
                


    else:

        for _ in range(duration*frequency):
            try:
                data_from_thread = shared_data.data_queue.get(block=False)  # Non-blocking get
                print("Received HR: {:2f} ".format(data_from_thread))

            except queue.Empty:
                print("No data in the queue.")
            time.sleep(1/frequency)  # Sleep for a while to avoid busy-waiting




if __name__ == "__main__":
    main()