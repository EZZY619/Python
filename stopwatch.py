import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    
    input("Press Enter again to stop it.")
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {round(elapsed_time, 2)} seconds")

stopwatch()
