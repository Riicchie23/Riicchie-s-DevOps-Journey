from pynput.keyboard import Key, Listener

class KeyListener():
    def __init__(self, target_key):
        self.target_key = target_key
    
    def onKeyPressListener(self, key):
        if key == self.target_key:
            return False
    
    def start_listener(self):
        with Listener(on_release=self.onKeyPressListener) as listener:
            listener.join()

if __name__ == "__main__":
    target_key = Key.enter
    kl = KeyListener(target_key)

    kl.start_listener()

