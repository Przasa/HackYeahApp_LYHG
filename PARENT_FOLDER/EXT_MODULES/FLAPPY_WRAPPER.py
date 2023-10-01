import sys, os
import threading

from EXT_MODULES.Flappy_bird_python import flappy

class FlappyInterface:

    def __init__(self) -> None:
        pass

    def StartFlappy(self):
        flappy_thread = threading.Thread(target=flappy.lauch_game)
        flappy_thread.start()


if __name__ == "__main__":
    flappy_iface = FlappyInterface()
    flappy_iface.StartFlappy()
