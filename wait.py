import time
import sys

def progress_bar(iteration, total, start_time, length=60):
    percent = iteration / total
    filled_length = int(length * percent)
    bar = '█' * filled_length + '-' * (length - filled_length)
    
    elapsed = time.time() - start_time
    remaining = max(0, total - iteration - 1)
    eta = int(remaining)  # 1 second per step

    sys.stdout.write(f'\r|{bar}| {percent:.1%} ETA: {eta//60:02d}:{eta%60:02d}')
    sys.stdout.flush()

def run_1_hour_bar():
    total_seconds = 3600
    start_time = time.time()
    for i in range(total_seconds):
        progress_bar(i, total_seconds, start_time)
        time.sleep(1)
    progress_bar(total_seconds - 1, total_seconds, start_time)
    print()  # newline after completion

# Run it
run_1_hour_bar()
