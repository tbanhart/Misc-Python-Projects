__author__ = 'Trevor Banhart'
import json;
import os;
# This is a program that will run a command-based console application. The goal
# is to be able to add books and users to a library's json files and access them to
# check out and return books.

# Inputs: book, books, user, users, command, user_input
# Outputs: book, books, user, users, commands

# Modules

# Module main()
#	Declare String command
#	display_greeting()
#	while command != "exit"
#		Set command = get_valid_input("command", True)
#		process_command(command)
# End Module

def main():
		command = "";
		initialize_commands();
		display_greeting();
		while command != "exit":
			command = get_valid_input("command", True);
			process_command(command);

# Module initialize_commands()
#	Declare List<String> commands
#	Set commands = [
#		"add user",
#		"remove user",
#		"list users",
#		"add book",
#		"remove book",
#		"list books",
#		"checkout",
#		"checkin",
#		"help",
#		"?",
#		"exit"
#		]
#	set_data(command, commands)
# End Module 

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

# Module display_greeting()
#	Display "Welcome to Demo City Library’s System Database! Enter help or ? for a list of commands."
# End Module

def display_greeting():
	print("Welcome to Demo City Library’s System Database! Enter help or ? for a list of commands.");

# Module process_command(String command)
#	If command == "checkout"
#		Declare String book = get_valid_input("available book", True)
#		set_data_move("available book", "unavailable book", book)
#	Else If command == "checkin"
#		Declare String book = get_valid_input("unavailable book", True)
#		set_data_move("unavailable book", "available book", book)
#	Else If command == "add user"
#		Declare String user = get_valid_input("user", False)
#		if user == "cancel"
#			break 
#		set_data_add("user", user)
#	Else If command == "remove user"
#		Declare String user = get_valid_input("user", True)
#		set_data_remove("user", user)
#	Else If command == "list users"
#		Declare List<string> users = get_data("user")
#		display_list(users)
#	Else If command == "add book"
#		Declare String book = get_valid_input("book", False)
#		if book == "cancel"
#			break; 
#		set_data_add("book", book)
#		set_data_add("available book", book)
#	Else If command == "remove book"
#		Declare String book = get_valid_input("book", True)
#		set_data_remove("book", book)
#		set_data_remove("available book", book)
#		set_data_remove("unavailable book", book)
#	Else If command == "list books"
#		Declare List<string> books = get_data("book")
#		display_list(books)
#	Else If command == "help" || "?"
#		Declare List<string> commands = get_data("command")
#		display_list(commands)
#	Else 
#		Display "Undefined command, try another command."
# End Module

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

# Module display_list(List<string> list)
#	For each item in list
#		Display item
# End Module

def display_list(list):
	for item in list:
		print(item);

# Module set_data_add(String type, String value)
#	Declare List<String> data
#	If validate_input(type, value) == False
#		Set data = get_data(type)
#		Set data += value
#		set_data(type, data)
# End Module 

def set_data_add(type, value):
	data = [];
	if validate_input(type,value) == False:
		data = get_data(type);
		data.append(value);
		set_data(type, data);

# Module set_data_remove(String type, String value)
#	Declare List<String> data
#	If validate_input(type, value) == True
#		Set data = get_data(type)
#		Set data -= value
#		set_data(type, data)
# End Module 

def set_data_remove(type, value):
	data = [];
	if validate_input(type, value) == True:
		data = get_data(type);
		data.remove(value);
		set_data(type, data);

# Module set_data_move(String type_from, String type_to, value)
#	set_data_remove(type_from, value)
#	set_data_add(type_to, value)
# End Module

def set_data_move(type_from, type_to, value):
	set_data_remove(type_from, value);
	set_data_add(type_to, value);

# Module set_data(String type, List<String> value)
#	Set type += "s.json"
#	With open(type, "w") as file
#		json.dump(value, file)
# End Module

def set_data(type, value):
	type += "s.json";
	with open(type,"w+") as file:
		json.dump(value, file);

# Module print_error_invalid()
#	Display "Invalid entry. Enter a valid selection or cancel to exit."
# End Module

def print_error_invalid():
	print("Invalid entry. Enter a valid selection or cancel to exit.");

# Module request_input(String type)
#	Display "Please enter a " + type
# End Module  

def request_input(type):
	print("Please enter a " + str(type));

# Functions

# Function String get_valid_input(String type, Bool exists)
#	Declare String user_input
#	Set user_input = get_input(type)
#	While validate_input(type, user_input) == exists
#		Display "Invalid entry. Enter a valid selection or cancel to exit."
#		Set user_input = get_input(type)
#		If user_input == "cancel"
#			Break
#	Return user_input
# End Function

def get_valid_input(type, exists):
	user_input = get_input(type);
	while validate_input(type, user_input) != exists:
		print_error_invalid();
		user_input = get_input(type);
		if user_input == "cancel":
			break;
	return user_input;

# Function String get_input(String type)
#	Declare String user_input
#	request_input(type)
#	Input user_input
#	return user_input
# End Function 

def get_input(type):
	user_input = "";
	request_input(type);
	user_input = input("");
	return user_input;

# Function Bool validate_input(String type, String entry)
#	Declare List<String> data
#	Set data = get_data(type)
#	If data contains entry
#		Return True
#	Else
#		Return False
# End Function 

def validate_input(type, entry):
	data = [];
	data = get_data(type);
	if entry in data:
		return True;
	else:
		return False;

# Function List<String> get_data(String type)
#	Declare List<String> data
#	Set type += "s.json"
#	With open(type) as file
#		If file exists
#			Set data = json.load(file)
#		Except data = data 
#	Return data
# End Function  

def get_data(type):
	data = [];
	type += "s.json";
	if os.path.exists(type) == True:
		with open(type, 'r') as file:
			data = json.load(file);
	return data;

main();
