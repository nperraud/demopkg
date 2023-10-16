import sys
from time import sleep

sleep_secs = 300

print(f"Hello from script.py, I was passed arguments {sys.argv[1:]}")
print(f"Sleeping for {sleep_secs} seconds")
sleep(sleep_secs)
