# Conway-s-game-of-life
This is my python implementation of John Horton Conway's game of life, I hope you find it useful.

The program needs optimization, due it makes a lot of operations with arrays that can be unecessary at all, at the moment it seems work as is expected, but any bug or error that you found please, let me know. 

Tested in python 3.12.9 and pygame 2.6.1

## How to use:

### To prepare the environment

1. Open a new Terminal/CMD
2. Create a new virtual enviroment in the project folder "python3 -m venv path"
3. Activate the new venv:
   - Windows "venv_path/Scripts/activate.bat or venv_path/Scripts/activate"
   - Linux "source venv_path/bin/activate"
4. Install the dependencies "pip3 install -r requirements.txt"
5. Open the main.py file "python3 main.py"
6. Enjoy!

### In the program

#### GUI

Into the program you can select the cells (squares) that you want to put, all the black cells are dead, the white are alive.

To start the simulation press the <kbd>SPACE</kbd> key, also it's toggle the state of the simulation, between pause and play.

The <kbd>BACKWARD</kbd> key resets the world and stops the simulation.

Also making click in one cell while the simulation is running will pause it.

On the program title will be a counter of the days(steps) that has been passed since the start of the simulation, they will reset if you clear the world.

##### Test Mode

You can start test mode by pressing the <kbd>T</kbd> key and then <kbd>1</kbd> or <kbd>2</kbd>.  
Pressing <kbd>1</kbd> will load a simple cyclic structure (I wasn’t able to find its name, if you know it, let me know).  
The <kbd>2</kbd> key will load a **Pulsar**:

![Pulsar, Conway's Game of Life](https://upload.wikimedia.org/wikipedia/commons/0/07/Game_of_life_pulsar.gif)

After the world loads, you can use the game normally.

##### FPS Control

<kbd>↑</kbd> doubles the FPS, up to a maximum of 144 FPS (120 might be enough, due to current frame rate multiples).  
<kbd>↓</kbd> halves the FPS, down to a minimum of 1 FPS.

#### Console

The console mode it's different from the GUI mode, it puts randomly the alive cells and starts the simulation.

By the moment just can be stopped by killing the procces, and don't have all the funtionalities of the GUI mode.

This model it's planned for improvement over time.

## Modules and Libraries

This program uses the modules sys, copy, time and random from python.

For the GUI module it makes use of pygame 2.6.1.

## Suggestions
Any suggestion or commentary about the program it's appreciated.