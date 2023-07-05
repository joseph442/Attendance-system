#!/usr/bin/env python3
import os
import sys
import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUG: usage: {}".format(usage))
    return usage < percent

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot in this system")
        sys.exit(1)
    else:
        if not check_cpu_usage(75):
            print("ERROR! CPU is overloaded")
        else:
            print("Everything is ok")

main()
print("thanks")
