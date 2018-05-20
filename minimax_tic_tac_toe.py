import random
import os
import time
import requests
import json
import textwrap

# def main_experiment(iterations):
# 	wins = 0
# 	draws = 0
# 	for i in range(iterations):
# 		result = tic_tac_toe()
# 		if result == "win":
# 			wins += 1
# 		if result == "draw":
# 			draws += 1
# 	print("\t\t\t\t{0} Wins; {1} Draws\n".format(wins, draws))


def tic_tac_toe():
	FIRST_PLAYER = random.choice(("x", "o"))
	DESCRIPTION = "This is an implementation of a Minimax Algorithm to minimize one's own maximum loss, and to maximize one's own minimum gain in the zero-sum game of tic-tac-toe. This program was created in an effort to prove that a 'perfect player' in competition with a 'random' or 'novice' player of tic-tac-toe will always win or draw in a given game. API calls are made to the \"Tic-Tac-Toe\" github repository of Jason Fox in order to simulate a 'perfect player', while implementation of Brian Bristol's \"Wager\" code is utilized to simulate a 'random'/'novice' player. For the purposes of this algorithm, the 'perfect player' will always be 'X' while the 'random'/'novice' player will always be 'O'. Gameplay is executed in a Terminal or Command Prompt shell compatible with a Python 3 environment."
	board_status = [{"id": "top-left", "value": " "}, 
	{"id": "top-center", "value": " "}, 
	{"id": "top-right", "value": " "}, 
	{"id": "middle-left", "value": " "}, 
	{"id": "middle-center", "value": " "}, 
	{"id": "middle-right", "value": " "}, 
	{"id": "bottom-left", "value": " "}, 
	{"id": "bottom-center", "value": " "}, 
	{"id": "bottom-right", "value": " "}]
	board_json = {"player_piece" : "x",
	"opponent_piece": "o",
	"board" : [
	{"id": "top-left", "value": ""}, 
	{"id": "top-center", "value": ""}, 
	{"id": "top-right", "value": ""}, 
	{"id": "middle-left", "value": ""}, 
	{"id": "middle-center", "value": ""}, 
	{"id": "middle-right", "value": ""}, 
	{"id": "bottom-left", "value": ""}, 
	{"id": "bottom-center", "value": ""}, 
	{"id": "bottom-right", "value": ""}
	]}
	url = "http://perfecttictactoe.herokuapp.com/api/v2/play"
	turn = FIRST_PLAYER
	placement = None
	iterations = 1
	potential_winner = None

	os.system('clear')
	print()
	print(textwrap.fill(DESCRIPTION, 125))
	print("\n\t\t\t\t'{0}' will make the first move. Please wait for the game to start.".format(FIRST_PLAYER.upper()))
	time.sleep(20)
	draw_board(board_status)
	while potential_winner == None and iterations < 9:
		if turn == "x": # perfect player
			# API Call to perfect player
			response = requests.post(url, json=board_json)
			decoded_response = response.json()
			for j in range(9):
				if decoded_response["data"]["board"][j]["value"] != board_json["board"][j]["value"]:
					placement = (j, "x")
			turn = "o"
		else: # random/novice player 
			placement = randomize(board_status, "o")
			turn = "x"
		board_json["board"][placement[0]]["value"] = placement[1]		
		board_status[placement[0]]["value"] = placement[1].upper() # assign value to board place dictionary
		draw_board(board_status)
		potential_winner = determine_winner(board_json) # check for winner
		iterations += 1
		time.sleep(3)
	if potential_winner:
		print("\n\t\t\t\t\t   '{0}' is the winner. Game over.\n\n".format(potential_winner.upper()))
		#return "win"
	else:
		print("\n\t\t\t\t\t   Tie. Game over.\n\n")
		#return "draw"


def determine_winner(board):
	'''Looks for consecutive player moves in each of the possible winning combinations.'''
	win_combos = ["012", "345", "678", "036", "147", "258", "246", "840"]
	for combo in win_combos:
		if board["board"][int(combo[0])]["value"] == "x":
			if board["board"][int(combo[1])]["value"] == "x":
				if board["board"][int(combo[2])]["value"] == "x":
					return "X" # winning player
		if board["board"][int(combo[0])]["value"] == "o":
			if board["board"][int(combo[1])]["value"] == "o":
				if board["board"][int(combo[2])]["value"] == "o":
					return "X" # winning player
	return None

def randomize(spaces_taken, letter):
	'''Randomizes the move of novice player 'O' on tic-tac-toe board.'''
	space_names = ["top-left", "top-center", "top-right", "middle-left", "middle-center", "middle-right", "bottom-left", "bottom-center", "bottom-right"]
	move = random.randint(0,8)
	if spaces_taken[move]["value"] != " ": # if move has already been made in a space
		return randomize(spaces_taken, letter)
	else:
		return (move, letter) # tuple of board position and "o" symbol

def draw_board(board):
	'''Creates graphical representation of Wager game.'''
	os.system('clear')
	print()
	print("\n\t\t\t\t\t\t     ",board[0]["value"],"|",board[1]["value"],"|",board[2]["value"])
	print("\t\t\t\t\t\t     ", "----------")
	print("\n\t\t\t\t\t\t     ",board[3]["value"],"|",board[4]["value"],"|",board[5]["value"])
	print("\t\t\t\t\t\t     ", "----------")
	print("\n\t\t\t\t\t\t     ",board[6]["value"],"|",board[7]["value"],"|",board[8]["value"], "\n")

#main_experiment(100)
tic_tac_toe()