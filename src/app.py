import random
import requests
import autodynatrace
import time


@autodynatrace.trace
def call_ship():
    address = f"http://192.168.0.{random.randint(1, 30)}"
    try:
        print(requests.get(address))
    except Exception:
        pass


def main():
    while True:
        call_ship()
        time.sleep(5)


if __name__ == '__main__':
    main()
