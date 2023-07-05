#!/usr/bin/env python3
import socket
import os
import sys
import psutil

def check_no_network():
    """Return True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUG: usage: {}".format(usage))
    return usage < percent

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    checklist = []

    if check_reboot():
        checklist.append("Pending Reboot")
    if not check_cpu_usage(75):
        checklist.append("CPU Overloaded")
    if check_no_network():
        checklist.append("No Network")

    if checklist:
        print("Issues found:")
        for item in checklist:
            print("- " + item)
        sys.exit(1)
    else:
        print("Everything is ok")

main()
print("Thanks")
