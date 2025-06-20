import sys
import time

def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

total_iterations = 100

for i in range(total_iterations + 1):
    time.sleep(0.01)  # Simulate some work
    progress_bar(i, total_iterations, prefix='Cleaning up:', suffix='Complete', length=50)




print("\nCleanup complete, Entering wait sate for 1 hour...")