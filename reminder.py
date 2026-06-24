import threading
import time

class TimerOfThread:
    def __init__(self, seconds=5, message="Process Start"):
        self.seconds = seconds
        self.message = message
        
        self.threadStop = threading.Event()
        self.thread = None

    def Times(self):
        while not self.threadStop.is_set():
            time.sleep(self.seconds)
            
            print(self.message)

    def Start(self):
        
        self.thread = threading.Thread(
            target=self.Times,
            
            name="TimerOfThread"
        )
        self.thread.start()

    def Stop(self):
        self.threadStop.set()

        if self.thread:
            self.thread.join()
            
    def __del__(self):
        print("Exit from timer")


def main():
    timer = TimerOfThread(2, "The thread is running")
    
    timer.Start()

    while True:
        value = input("The stop message (y/n): ")

        if value.lower() == "y":
            timer.Stop()
            
            print("Processing Stopped")
            break
        
    del timer


if __name__ == "__main__":
    main()