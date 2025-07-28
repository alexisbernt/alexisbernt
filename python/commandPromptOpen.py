import os
import subprocess

def open_cmd():
    try:
        # subprocess is a library that lets your Python script run
        # system-level commands, just like if you typed them into the terminal or command prompt.
        subprocess.Popen("start", shell=True)
        print("Command Prompt opened.")
    except Exception as e:
        print(f"Error opening Command Prompt: {e}")

if __name__ == "__main__":
    open_cmd()
