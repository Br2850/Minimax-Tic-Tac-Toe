# Minimax-Tic-Tac-Toe

## Study
_In order to replicate the results presented in the paper, "The Perfect Tic-Tac-Toe Player: Minimax Algorithm" certain changes to the code file <minimax_tic_tac_toe.py> need to be made first. The program in its current state is only meant to simulate one game of Tic-Tac-Toe and it prioritzes visuale display over information gathering. In order to process many games, code has already been provided within the structure of the program. In your favorite text editor, open the file <minimax_tic_tac_toe.py>. Please comment out lines: 117, 79, 76, 74, 71, and 52 - 56. Please reinstate/uncomment lines 8 - 17, 77, 80, 116. On line 116, please insert the number of Tic-Tac-Toe games you would like to run as a numerical value within the parenthesis of the function call "main_experiment". After the completition of these steps, running this program will no longer output any text until the program has terminated. After the successful termination of the program, one line will be printed to the standard output which will describe the number of games that resulted in wins and the number of the games that resulted in draws. Note, the amount of time it will take to run this program will be dependent on the number of Tic-Tac-Toe games desired to be run. For example, 1000 instances takes significantly longer to run than 100 instances._

## System Requirements
* Terminal/Command Prompt
* Python 3 Environment
* 'Requests' Python Module
* 'JSON' Python Module
* A Stable Internet Connection

## To Run
1. Download the zip file or clone the necessary files from Github
2. Extract the zip file, if applicable, into a desired folder
3. In the appropriate source folder, open a Terminal/Command Prompt
4. Set the Terminal/Command Prompt screen size to be at least 125 pixels wide
5. Type in the command <python3 minimax_tic_tac_toe.py> to run
6. If running non-Study version, a Tic-Tac-Toe game with details describing the gameplay will be displayed
7. If running the Study version, no output will be displayed until termination of the program

## Troubleshoot:
* The Python modules listed in the System Requirements are paramount to running this program. Failure to acquire these modules will result in the appearance of errors. To download any missing modules, 'pip install' the necessary modules. Other methods of installing these modules are out of the scope of this documentation, please Google search your specific problem if module errors occur.
* The length of time required to run a large number of Study version Tic-Tac-Toe games is significant. Calls are being made to an outside API which require time, therefore please be patient if you attempt to run a study on a large number of Tic-Tac-Toe games.
* Internet connection is an essential part of this program. The program will not function without this system requirement. 
