# Manual

This document shows how to use Gades Siege. For the installation instructions, check [here](installation.html).

## Launching ##

Once Gades Siege has been built, you can launch it through its main script, located in the root folder:
```
./gsiege.py
```

This also works:
```
python gsiege.py
```

## Log files ##

Gades Siege has two types of log files:

* Developer logs: the `log_gsiege` file created in the main folder will contain the various debugging, warning and error messages produced during execution.
* Match logs: they record all the actions during a match. These are located in the `data/games` folder, and are classified by the type of match.

# Main menu options #

The main menu of Gades Siege lists several options, which we describe below.

## Quick game ##

This is for a single match between two expert systems. The configuration dialog allows us to pick the teams that will face off and change various options:
* We can change the length of the game with **Number of turns**.
* If we check **Don't save the game**, no match log will be produced.
* If we check **Only result**, we will only see the final result of the match instead of all the actions taken.
* If we check **Hide piece values**, the value of each piece will be hidden until it is uncovered by another piece.

Once we click **Apply**, the match will start with the specified options.

## Competitions ##

The competition mode is the most commonly used in Gades Siege. It runs various types of competitions among many teams, following one of three formats:

* **League**: all teams play against each other. Teams are given points for ties and wins, and a ranking is generated showing the winners of the competition.
* **Cup**: teams are matched against each other randomly. Defeated teams are automatically removed from the competition, and winners advance to the next round. Matches are organised in a tree, and the number of teams in each round is always a power of two. Gades Siege is implemented so that all the [byes](https://en.wikipedia.org/wiki/Bye_(sports)) happen in the first round.
* **Mixed**: this is a hybrid between a league and a cup. First, a league is run with all the participants, and then a cup is held using the teams in the top half of the league ranking.

This window offers the following options:

* **Two legs**: this option is only valid for leagues. Ensures that all pairs of teams play against each other twice, swapping their turn order.
* **Only results**: same as for _quick games_, it will only show the results from each game, and not the full game.
* **Number of turns**: same as for _quick games_, it changes the length of the game.

The **Players** tab is for entering the various teams into the competition. There is a checkbox for adding all installed teams into the system at once.

## Play against an expert system ##

This is the most interactive mode in Gades Siege. We will be able to manually control one of the teams in the game and face off an expert system controlled by the computer.

We can choose our formation within the **Human team** section, and either pick the formation and rules for the **Computer team** or leave it as random. The other configuration options are the same as in the previous modes.

Once we start a match, during our turns we can click the piece we want to move. The available target positions will be highlighted in cyan. We will not see the values of the enemy pieces until they are uncovered by another piece. The goal of the game is the same as usual: to find and capture the enemy king. The match will end once one of the kings is captured.

## Laboratory ##

This mode allows us to have our expert system play many matches automatically. After choosing the expert system to evaluate in the **Main expert system** section, we will be able to choose various options:
* The **number of repetitions** for each match.
* The **number of turns** that each match will take.

We will then choose which teams will be the opponents, or **use all teams installed**. Clicking **Forward** will start the evaluation process, which may take a while.

Afterwards, we will be shown a table of statistics and a collection of graphs, with the following information:

* Number of matches played, won, lost and tied.
* Number of turns in which the system is winning or losing.
* Turn in which the highest valued piece is lost.

## Previous games ##

This mode is for browsing previously played games. We need to pick the desired match log, and then the usual match replay window will appear.

## Settings ##

The configuration options in this window are:

* Path to the folder with the match logs.
* Path to the folder with the expert systems. Valid expert system folders must have two subfolders:: **rules** and **formations**. We will explain [later](teamdesign.html) the meaning of these folders.
* Enabling or disabling music during matches.
* Time interval between turns in the autoplay mode.

## About ##

This panel shows the credits for the game and other miscellaneous information.

# Folder structure #

Gades Siege is organised into these folders:
  * **data** : includes all resource files,
    * **fonts** : typographies.
    * **games** : match logs.
    * **glade** : user interface definitions.
    * **images** : images and other graphical assets.
    * **music** : music assets.
    * **teams** : <font color='#ff0000'><b>important</b></font>, this is where teams are stored. [Here](teamdesign.html) we explain how to add your own teams to Gades Siege. It has two subfolders:
      * **formations** : team formations - the way in which pieces are initially placed.
      * **rules** : team rules - the way in which the expert system plays the game.
  * **notes** : miscelleaneous developer documentation.
  * **guadaborad** : Python files with the guadaboard module, which presents the matches on the screen.
  * **libguadalete** : Python files with the game engine module, which generates the match results and processes Clips files.
  * **po** : translation files.
  * **resistencia** : Python file with the main game module, which coordinates the others, provides the user interface and manages the various configuration options.

## Team files ##

For more information on how to create teams, check [here](teamdesign.html).

## Obstacles ##

Obstacles are defined in the **obstaculos** file inside the **data** folder. The syntax is quite simple: each obstacle is a single line of the form `(x,y)`, where `x` is the column where the obstacle should be placed, and `y` is the row. This would be a valid file:
```
(1,4)
(2,4)
(3,4)
(4,4)
```

As explained in [the article on designing teams](teamdesign.html), a rule can find out if there is an obstacle in the board by using `(obstaculo (pos-x) (pos-y))`.
