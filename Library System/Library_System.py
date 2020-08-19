__author__ = 'Trevor Banhart'
import json;
import os;
# This is a program that will run a command-based console application. The goal
# is to be able to add books and users to a library's json files and access them to
# check out and return books.

# Inputs: book, books, user, users, command, user_input
# Outputs: book, books, user, users, commands

# Modules

def main():
		command = "";
		initialize_commands();
		display_greeting();
		while command != "exit":
			command = get_valid_input("command", True);
			process_command(command);

def initialize_commands():
	commands = [
		"add user",
		"remove user",
		"list users",
		"add book",
		"remove book",
		"list books",
		"checkout",
		"checkin",
		"help",
		"?",
		"exit"
		];
	set_data("command", commands);

def display_greeting():
	print("Welcome to Demo City Library’s System Database! Enter help or ? for a list of commands.");

def process_command(command):
	if command == "checkout":
		book = get_valid_input("available book", True);
		set_data_move("available book", "unavailable book", book);

	elif command == "checkin":
		book = get_valid_input("unavailable book", True);
		set_data_move("unavailable book", "available book", book);

	elif command == "add user":
		user = get_valid_input("user", False);
		if user == "cancel":
			exit;
		set_data_add("user", user);

	elif command == "remove user":
		user = get_valid_input("user", True);
		set_data_remove("user", user);

	elif command == "list users":
		users = get_data("user");
		display_list(users);

	elif command == "add book":
		book = get_valid_input("book", False);
		if book == "cancel":
			exit;
		set_data_add("book", book);
		set_data_add("available book", book);

	elif command == "remove book":
		book = get_valid_input("book", True);
		set_data_remove("book", book);
		set_data_remove("available book", book);
		set_data_remove("unavailable book", book);

	elif command == "list books":
		books = get_data("book");
		display_list(books);

	elif command == "help" or "?":
		commands = get_data("command");
		display_list(commands);

	else: 
		print("Undefined command, try another command.");

def display_list(list):
	for item in list:
		print(item);

def set_data_add(type, value):
	data = [];
	if validate_input(type,value) == False:
		data = get_data(type);
		data.append(value);
		set_data(type, data);

def set_data_remove(type, value):
	data = [];
	if validate_input(type, value) == True:
		data = get_data(type);
		data.remove(value);
		set_data(type, data);


def set_data_move(type_from, type_to, value):
	set_data_remove(type_from, value);
	set_data_add(type_to, value);

def set_data(type, value):
	type += "s.json";
	with open(type,"w+") as file:
		json.dump(value, file);

def print_error_invalid():
	print("Invalid entry. Enter a valid selection or cancel to exit.");

def request_input(type):
	print("Please enter a " + str(type));

# Functions

def get_valid_input(type, exists):
	user_input = get_input(type);
	while validate_input(type, user_input) != exists:
		print_error_invalid();
		user_input = get_input(type);
		if user_input == "cancel":
			break;
	return user_input;

def get_input(type):
	user_input = "";
	request_input(type);
	user_input = input("");
	return user_input;

def validate_input(type, entry):
	data = [];
	data = get_data(type);
	if entry in data:
		return True;
	else:
		return False;

def get_data(type):
	data = [];
	type += "s.json";
	if os.path.exists(type) == True:
		with open(type, 'r') as file:
			data = json.load(file);
	return data;

main();
