from pynput.keyboard import Key, Listener

class KeyListener():
    def onKeyPressListener(self, key, target_key):
        if key == target_key:
            print("Enter has been pressed")
            return False
    
    def start_listener(self, target_key):
        with Listener(on_release=lambda key: self.onKeyPressListener(key, target_key)) as listener:
            listener.join()

if __name__ == "__main__":
    kl = KeyListener()
    target_key = Key.enter

    kl.start_listener(target_key)



        