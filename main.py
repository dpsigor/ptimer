import os
import sys
import time


def figlet(notification, countdown):
    os.system(
        f"""
        height=$(tput lines);
        half=$((height/2-10));
        for x in $(seq 1 1 $half); do
            echo '';
        done
        """
    )
    os.system(f"figlet -w $(tput cols) -c {notification} | lolcat")
    os.system(f"figlet -w $(tput cols) -c {countdown} | lolcat")


def clear():
    os.system("clear")


def main(notification, seconds):
    while seconds:
        countdown = time.strftime("%M:%S", time.gmtime(seconds))
        clear()
        figlet(notification, countdown)
        seconds -= 1
        time.sleep(1)


if __name__ == "__main__":
    seconds = 90
    notification = "BRB"
    if sys.argv[1:]:
        seconds = int(sys.argv[1])
    if seconds < 0:
        raise ValueError("Seconds should be a positive integer.")
    if seconds > 3600:
        raise ValueError("Seconds should be less than 3600.")
    if sys.argv[2:]:
        notification = " ".join(sys.argv[2:])
    main(notification, seconds)
