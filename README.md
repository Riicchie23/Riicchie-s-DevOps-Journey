<div>
# Riicchie's DevOps Journey
This will be my somewhat of a journal on the things that I've been doing. </br>
(or atleast I'll "try" to be consistent on logging my works //note to self!)

### **Things I need to learn:**
I will be using this [site](https://roadmap.sh/devops) as a reference on what I need to learn first
I ditch the whole "following step by step" since I realize that will only make things slower </br>


### **Certificates I need to get:**

As of today (3/16/24), I do not know what certificated I need to get for I am only starting
</div>

<div>

## Day 1 (March 16, 2024)

- I'm doing the first part of the course, Python.
- Currently learning on how to manuever with Git

<details>
  <summary> Usage of Git </summary>

## Setting up

```
  git config --global user.name "[name]" 
  git config --global user.email "[email]"
  git clone [url]
```

## Staging

```
  git status
  git commit -m "[message]"
```

## Branching

```
  git branch
  git branch [branch-name]
  git checkout [branch-name]
  git merge [branch-name]
```

## Inspect

```
  git log
```

## Updating

```
  git remote add [nickname] [url]
  git merge [nickname]/[branch-name]
  git push [nickname] [branch-name]
  git pull
```

</details>

## Day 2 (March 17, 2024)

- Currently reading about Python basics
- Planning to make a simple Python game

<details>
  <summary>Details of the game</summary>

```
  # Create a RPG-like game, where there's a boss and the player needs to defeat it
  # Player can choose what class they want
  # It will have a fixed set of skills
  # Player can know how many hp the boss still has
  # It will be a turn-based type of game
```

</details>

- You know, I really should start learning how to use flowcharts
  its kind of hard to constantly remember how a flow supposed to work
- As of late, probably I'll focus first on the "RPG game" project as a way to limit test
  myself with Python
- I forgot to mention, I somewhat have the basic grasp of Git. I'm just worried that since I found *Source Control* here in VSCode, I might lose that knowledge but I'll try not too.

## Day 3 (March 18, 2024)

- Since its the weekdays, probably I'll have a shorter time to do this (around an hour) but I think that's enough to do something productive
- I think I'll continue on that game or probably research some other stuff
- I searced some DevOps scripting that uses Python, I think that's too advance ^^;
- So, I decided to continue on the game first.
- I learned how to use Python's [pynput](https://pythonhosted.org/pynput/keyboard.html#) (just a little bit)

<details>
  <summary>pynput</summary>

```python
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
```

</details>

## Day 4 (March 19, 2024)

- Probably I'll continue the game first, I'll try to implement some advance coding and good practice
- I have only 1 week before, I change language in this case, I'll learn golang

## Day 5 (March 20, 2024)

- Didn't got to do anything, took a break

## Day 6 (March 21, 2024)

- Tries to figure out how to correctly use imports on Python.
- Still can't understand how that works, I'll probably stick with using ``sys`` module

```python
import sys
sys.path.append('[filepath]')
```

## Day 7 (March 22, 2024)
  - Learned that alias in github is not for website aliasing. oops

## Day 8 (March 23, 2024)
  - Break

## Day 9 (March 24, 2024)
  - Started with Ubuntu, manage to get a course on udemy

## Day 10 (March 25, 2024)
</div>
