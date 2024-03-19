from pynput.keyboard import Key, Listener, Controller
import sys

class KeyListener():
    def on_press(self, key):
        print(f"{key} is pressed")
        if key == Key.esc:
            sys.exit()

if __name__ == "__main__":
    kl = KeyListener()
    
    with Listener(on_press=kl.on_press) as listener:
        listener.join() 