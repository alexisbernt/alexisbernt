import os
import subprocess

def open_cmd():
    try:
        # This works on Windows to open a new command prompt window
        subprocess.Popen("start", shell=True)
        print("Command Prompt opened.")
    except Exception as e:
        print(f"Error opening Command Prompt: {e}")

if __name__ == "__main__":
    open_cmd()
