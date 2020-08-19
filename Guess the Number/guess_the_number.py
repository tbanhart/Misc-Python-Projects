
__author__ = 'Trevor Banhart'
import random;
import numbers;
# This is a program meant for the computer to guess the number the user is thinking of.

# The computer will start by asking the player for the minimum and the maximum number 
# their number is between.

# The way the computer decides the number to pick is by splitting the range of possible
# numbers in half and randomly adding or subtracting up to 10% of the possible range.
# Ex:If the range is 1-50, the computer will guess a number between 20 and 30.

# Once the computer has given a response, the player can tell the computer if the
# number is higher, lower, or correct.

# The computer receives two guesses plus one guess for every 10 numbers in the total 
# range. If the computer runs out of guesses it will ask what the number was 
# (to satisfy its curiosity, of course).
# Note: balance is a bit off, could use a sloped curve for gaining guesses so 
# it doesn't guess it EVERY time.

# Input List: number, requested_low, requested_high, high_or_low, correct_guess
# Ouput List: guessed_number, number, has_guessed_correctly

# Task: calulate current guess
def get_number(low, high):
	guess_range = abs(high - low);
	guess_middle = round(guess_range / 2);
	guess_offset = round(guess_range * .1);
	guessed_number = guess_middle + low;

	if guess_range == 0:
		print("It looks like I've guessed your number...");
		guessed_number = low;
	elif guess_range == 1:
		guessed_number = low + 1;
	elif guess_offset != 0:
		guessed_number += random.randrange(0 - guess_offset, guess_offset);
	
	return guessed_number;

# Task: request user for a number
def request_number(request):
	number = "";

	while validate_input(number, int) == False:
		number = input("Please enter a number for the " + str(request) + " number.");

	return int(number);

# Task: make guesses until correct or out of guesses
# Note: would make code more solid adherent to have input options taken from json or xml,
# do not know which package to use to achieve this
def make_guesses(low, high):
	low = low;
	high = high;
	guesses = round(((high-low) * .1) + 2);
	has_guessed_correctly = False;
	#Is there a way to express an empty string similar to string.empty?
	high_or_low = "";
	current_guess = 0;

	while guesses > 0:
		print("I currently have " + str(guesses) + " guesses remaining.");
		current_guess = get_number(low, high);
		high_or_low = get_guess_feedback(current_guess, "high", "low", "correct")
		if high_or_low == "high":
			high = current_guess;
			guesses -= 1;
		elif high_or_low == "low":
			low = current_guess;
			guesses -= 1;
		elif high_or_low == "correct":
			has_guessed_correctly = True;
			break;
		else:
			print("I don't understand that. Please enter high, low, or correct.");
			
	return has_guessed_correctly;

# Task: ensure correct input type is received
def validate_input(input_value, cast_type):
	try:
		cast_type(input_value);
		return True;
	except:
		return False;

# Task: Display rules for the player
def display_rules():
	print("Welcome to Guess the Number!");
	print("I will ask you for a high number and a low number in just a moment. After " + 
	"that, you will guess a number between the high and low numbers and I will try to " +  
	"guess it.");
	print("I will get two guesses plus one for each ten numbers in the range.");

# Task: get input from player on that matches accepted inputs
def get_guess_feedback(guess, *args):
	input_valid = False;
	high_or_low = "";
	while input_valid != True:
		high_or_low = str(input("My guess is " + str(guess) + ", is this number" + 
			" high, low, or correct?"));
		for arg in args:
			if high_or_low == arg:
				input_valid = True;
				break;
	return high_or_low;

# Task: get the correct guess from the player
def get_correct_guess():
	correct_guess = "";
	correct_guess = input("Out of curiosity, what was your number?");
	return correct_guess;

#Task: display closing notes dependent on whether computer was correct or not
def end_game(guessed_correctly):
	correct_guess = "";
	if guessed_correctly == True:
		print("I knew it!");
	else:
		print("Looks like I couldn't guess it...");
		correct_guess = get_correct_guess();
		print("My next guess was " + correct_guess + "!");
	print("Feel free to challenge me again any time.");

# Task: run through main loop of game
def main():
	guessed_correctly = False;
	low = 0;
	high = 0;
	requested_low = 0;
	requested_high = 0;

	random.seed();

	display_rules();
	
	requested_low = request_number("low");
	requested_high = request_number("high");
	low = min(requested_low, requested_high);
	high = max(requested_low, requested_high);
	guessed_correctly = make_guesses(low, high);
	end_game(guessed_correctly);

main();
