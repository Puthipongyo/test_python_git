import time
import pandas as pd

if __name__ == "__main__":
    print("Loading data...")
    running = True
    count = 0
    while running:
        print(count)
        count +=1
        time.sleep(1)
        if count==3 : running = False
        #eiei ayo
