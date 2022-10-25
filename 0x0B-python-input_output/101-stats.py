#!/usr/bin/python3
"""Log parsing."""
import sys
import signal

statuses = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def exit_program(signo, frame):
    """Handle the SIGINT signal."""
    for stat in statuses:
        if statuses[stat] == 0:
            continue
        sys.stdout.write(f"{stat}: {statuses[stat]}\n")
    sys.stdout.flush()


def main():
    """Parse logs passed in as stdin."""
    count = 0
    signal.signal(signal.SIGINT, exit_program)
    for line in sys.stdin:
        statuses[line.split()[-2]] += 1
        count += 1
        if count == 10:
            count = 0
            for stat in statuses:
                if statuses[stat] == 0:
                    continue
                sys.stdout.write(f"{stat}: {statuses[stat]}\n")
            sys.stdout.flush()


if __name__ == '__main__':
    main()
