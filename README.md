# Lab 5: Basic Tower Defense

## Intro
This week, we will be dealing with different tower types and writing functions to differentiate our different towers' attacks. 

Same as last week, there will be two types of monsters:
* fast monsters with low HP
* heavy monsters with high HP

This time, we will have two types of towers:
* A lightning tower with a fast cooldown (fast attack speed)
* A rock tower with a slow cooldown (slow attack speed)

For this lab we will be practicing writing and calling functions. You can copy your targeting functions from last week's lab and paste them into this week's. You will be using those functions to select a monster to damage when a tower's attack gets run. You'll need to check which type of tower is attacking though!

## Set Up
* Click the green 'Code' button on the top right of this section.
* Find 'Download ZIP' option and click it
* Unzip the file and move it over to your 'workspace' folder (or wherever you keep your files)

* Find the folder and open the entire folder in VSCode
    * You can find it in your Files and right click on it. Use the "Open with VSCode" option
    * You can also open VSCode, go to 'File' > 'Open' and then find the lab folder

* With VSCode open, go to the top of your window and find `Terminal`
* Click `Terminal`
* Click `New Terminal`

* In the new window that opens at the bottom of VSCode, type in
```
python run.py
```

* Hit enter
* You should see a game window open up
* You are done with set up!

## Game Explanation
This is a base version of tower defense with 2 tower types and 2 monster types. The objective is to take down the monsters before they reach the destination flag.

If a monster reaches your flag, then you will lose a life. Lose all 5 lives, and you lose the game.

We are starting off with 2 magic towers:
* Lightning
    * Cooldown: 2 seconds
    * Attack Radius: 300 pixels
    * Attack Damage: You decide!
* Rock
    * Cooldown: 4 seconds
    * Attack Radius: 200 pixels
    * Attack Damage: You decide!

You will be facing off against two monster types:
* Fast Monster
    * Total Health: 35HP
    * Speed: 90 pixels per second
* Heavy Monster
    * Total Health: 140HP
    * Speed: 35 pixels per second


Notice how Rock towers have a low rate of attack and lower attack radius. This is meant to be our heavy hitters, and we'll want to give them high damage! The lightning towers attack much more quickly and have a larger range. To make a balanced game, we want to make their individual attacks weak.

The idea here is to have the lightning towers powerful against fast enemies. Lightning towers can attack more enemies during the same time span, so deal well with quickly taking out weak targets.

Rock towers should have more damage output, but are slow. They will be suited for taking down heavy monsters one at a time. However, will struggle against a lot of fast monsters.

We want to have a game, where the best strategy is to have a mix of both! We'll get you started on balancing the game, but feel free to experiment!

## Lab Steps
* All the code you will need to edit is in `lab.py`
* You only need to use `run.py` to start the game, we will only have one map this week.
* Everything inside the `engine/` folder are the inner workings of the game. Feel free to take a look, but you won't need to change anything (unless you want to change your sprite speed)

### Selectors
* If you like your target selector functions from last week, feel free to copy / paste them over into this lab.
* If not, then feel free to use this basic solution:
```python
def selector_lightning(monsters):
    closest = None
    for monster in monsters:
        if closest == None:
            closest = monster
        elif get_distance_to_goal(monster) < get_distance_to_goal(closest):
            closest = monster
    return closest


def selector_rock(monsters):
    closest = None
    for monster in monsters:
        if closest == None:
            closest = monster
        elif get_distance_to_goal(monster) < get_distance_to_goal(closest):
            closest = monster
    return closest
```

* Notice that we have defined our own selector functions in this file. We can later use it in other functions, to help those functions do what they need to do.

### Attack Function
* Now let's take a look at the tower_attack function
* Notice the arguments it takes in:
    * monsters
    * tower
    * tower_type
* `monsters` is going to be a list of monsters that our game engine has determined to be in range of a specific tower
* `tower` is going to be the specific tower that we are focused on in this function
* `tower_type` is a string describing the type of tower (so we can tell the difference between rock and lightning)

* Understanding these arguments are important to correctly having the function do what you want it to do

* First let's set up two cases, one where our `tower_type == rock` and the other where our `tower_type == lightning`
```python
def tower_attack(monsters, tower, tower_type):
    if tower_type == 'lightning':
        pass
    elif tower_type == 'rock':
        pass
```

* `monsters` is the next argument we are interested in
* Notice how it's also the argument that we put into our selector function right?
* Also remember that our selector function returns a single monster for us to target
* So if we want to use our selector function inside this function, we need to call it with a list of monsters, and expect a single monster in return
* Let's just see what happens when we call a selector function with our `monsters` argument
```python
...
    if tower_type == 'lightning':
        monster = selector_lightning(monsters)
    elif tower_type == 'rock':
        monster = selector_rock(monsters)
    print(monster)
```
* Remember we split the case between selecting a monster for the rock to handle and for the lightning to handle

* Run the code and let's see what happens!
* PS: Click on the empty tower slots to spawn a tower. (Sometimes the click hanlder is finicky, so might require multi clicks)

If you checked the terminal output, you might notice a LOT of messages. That's because we are actually running this targeting function a LOT of times under the hood. If we choose to never attack an enemy, then the tower keeps looking for an enemy to attack.


* Now let's start making our towers attack.
* Here's an important part, we must determine how much damage our towers do.
* Update each conditional so you have a damage variable assigned
```python
...
    if tower_type == 'lightning':
        monster = selector_lightning(monsters)
        damage = 25
    elif tower_type == 'rock':
        monster = selector_rock(monsters)
        damage = 80
    print(monster)
```

* Now let's call the attack function, to actually have the tower attack our selected monster
```python
...
    if tower_type == 'lightning':
        monster = selector_lightning(monsters)
        damage = 25
    elif tower_type == 'rock':
        monster = selector_rock(monsters)
        damage = 80
    run_tower_attack_monster(tower, monster, damage)
```

* Notice how we use another helper function to help make this task simpler. Feel free to take a look inside that function, but we will get into these concepts next week.

* Save your file and run `run.py` and play the game!


### On Your Own
Alright now that you've got an interactive game going, let's set you off on your own to try and balance it.

You can change your target selector functions to more smartly select targets. Rock towers should target heavy monsters (with high HP). Lightning towers should target light monsters (with low HP). You should have all the tools in the lab file to allow your functions to select low vs high HP targets.

The next thing you can do is directly control the damage output that each tower type has. Obviously its easy to win if you set the damage to high, but that's not engaging to play. Instead, try and see what damage settings can make intense games. Where monsters barely make it or don't make it through. 

Play with these settings and see how this affects the game. Feel free to DM me with anything interesting!
