import os


def run(**arg):
    print("[*] In environment module.")
    return str(os.environ)

