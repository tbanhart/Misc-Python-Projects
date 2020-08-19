__author__ = "Trevor Banhart";

# This is a program that generates mazes and outputs the values to a json file to be 
# read by a GUI program. The values in the maze JSON file use bit directions to 
# calculate which tiles they connect to. Included is a Unity Project, unzipping this
# will allow viewing of the maze. The maze.json file generated in this file will need
# to be placed in your My Documents folder before running the Unity project.
# It is not recommended to generate mazes with sizes over 50 due to a high performance
# demand.

# Input List: size
# Output List: grid

# import enum
# import random
# import json

import enum;
import random;
import json;

# Class Directions(enum.Enum)
#	Declare border = -1
#	Declare empty = 0
#	Declare left = 1
#	Declare up = 2
#	Declare right = 4
#	Declare down = 8 
# End Class

class Directions(enum.Enum):
	corner = -2
	border = -1;
	empty = 0;
	left = 1;
	up = 2;
	right = 4;
	down = 8;

# Module main()
#	Declare Int size = get_input(int, "size")							input - size
#	Declare List[[Int]] grid()	
#	grid.generate_grid(size)
#	output_grid(grid, size)
# End Module

def main():
	size = get_input(int, "size");
	grid = [];
	grid = grid_initialize(grid, size);
	grid = generate_grid(grid, size);
	output_grid(grid);
	grid_to_json(grid);

# Module output_grid(Grid grid)
#	Declare String line
#	For each x_value in grid.grid
#		Set line = ""
#		For each y_value in grid.grid[x_value]
#			line += y_value + " " As String
#		Display line
# End Module

def output_grid(grid):
	line = "";
	for x_value in grid:
		line = ""
		for y_value in x_value:
			line += str(y_value);
			for digits in range(3 - len(str(y_value))):
				line += " ";
		print(line);

# Module grid_to_json(Grid grid)
#	With open("maze.json", "w+") as file	
#		json.dump(grid, file);
# End Modules

def grid_to_json(grid):
	with open("maze.json", "w+") as file:
		json.dump(grid, file);

# Function Grid grid_initialize(Grid grid, Int size)
# 	Set grid = []
# 	For Each x_value in range(size)
# 		Declare [Int] y_values
# 		For y_value in range(size)
# 			If x_value or y_value Is 0 Or
# 				x_value or y_value Is size
# 				Set y_values += Directions.border.value
# 			Else
# 				Set y_values += Directions.empty.value
#		Set grid += y_values
#	return grid
# End Module

def grid_initialize(grid, size):
	grid = [];
	for x_value in range(size+1):
		y_values = [];
		for y_value in range(size+1):
			value = Directions.empty.value;
			if x_value == 0 or x_value == size:
				value += Directions.border.value;
			if y_value == 0 or y_value == size:
				value += Directions.border.value;				
			y_values.append(value);
		grid.append(y_values);
	return grid;

# Function Int get_grid_cell(Grid, Int x_value, Int y_value)
# 	 return grid[x_value][y_value]
# End Function

def get_grid_cell(grid, x_value, y_value):
	return grid[x_value][y_value];

# Function Grid set_grid_cell(Grid grid, Int x_value, Int y_value, Int i_value)
# 	Set grid[x_value][y_value] = i_value
#	Return grid
# End Function	

def set_grid_cell(grid, x_value, y_value, i_value):
	grid[x_value][y_value] = i_value;
	return grid;

# Module update_grid_cell(Grid grid, Int x_value, Int y_value, Int i_value)
# 	set_grid_cell(grid, x_value, y_value, get_grid_cell(grid, x_value, y_value) + i_value)
# End Module

def update_grid_cell(grid, x_value, y_value, i_value):
	grid = set_grid_cell(grid, x_value, y_value, get_grid_cell(grid, x_value, y_value) + i_value);
	return grid;

# Function Grid generate_grid(Grid grid, Int size) 
# 	Declare Tuple[Int, Int] start_point = get_random_point(size, Directions.border.value)
# 	set_grid_cell(start_point[0],start_point[1],Directions.empty.value)
# 	Declare Tuple[Int, Int] end_point = get_random_point(size, Directions.border.value)
# 	set_grid_cell(start_point[0],start_point[1],Directions.empty.value)
# 	Declare Tuple[Int, Int] current_point = start_point
# 	Declare Tuple[Int, Int] previous_point
# 	Declare Int adjacent_value
# 	Declare Bool is_complete = False
# 	Declare List[Tuple[Int, Int]] adjacent_cells
# 	Declare Int bit_count
# 	While is_complete is False
# 		Set adjacent_cells = []
# 		If current_point[0] != 0										
# 			Set adjacent_value = get_grid_cell(current_point[0]-1, current_point[1]) 
# 			If adjacent_value == Directions.empty.value
# 				Set adjacent_cells += (current_point[0]-1,current_point[1])		
# 		If current_point[0] != size										
# 			Set adjacent_value = get_grid_cell(current_point[0]+1, current_point[1]) 
# 			If adjacent_value == Directions.empty.value
# 				Set adjacent_cells += (current_point[0]+1, current_point[1])				
# 		If current_point[1] != 0											
# 			Set adjacent_value = get_grid_cell(current_point[0], current_point[1]-1) 
# 			If adjacent_value == Directions.empty.value
# 				Set adjacent_cells += (current_point[0], current_point[1]-1
# 		If current_point[1] != size	
# 			Set adjacent_value = get_grid_cell(current_point[0], current_point[1]+1) 
# 			If adjacent_value == Directions.empty.value
# 				Set adjacent_cells += (current_point[0], current_point[1]+1
# 		If adjacent_cells.size != 0
# 			Set previous_point = current_point
# 			Set current_point = adjacent_cells[random_range(0,adjacent_cells.size-1)]
# 			Set bit_count = get_direction(previous_point, current_point)
# 			update_grid_cell(previous_point[0], previous_point[1], get_direction(previous_point, current_point)
# 			update_grid_cell(current_point[0], current_point[1], get_direction(current_point, previous_point)
# 		Else
# 			If is_spaces_available() == True
# 				Set current_point = get_random_point(size, 1)		
# 			Else
# 				Set is_complete = True
# End Function

def generate_grid(grid, size):
	start_point = get_random_point(grid, size, Directions.border.value);
	grid = set_grid_cell(grid, start_point[0], start_point[1], Directions.empty.value);
	end_point = get_random_point(grid, size, Directions.border.value);
	grid = set_grid_cell(grid, end_point[0], end_point[1], Directions.empty.value);
	current_point = start_point; 
	previous_point = start_point;

	adjacent_value = 0;
	is_complete = False;
	adjacent_cells = [];
	bit_count = 0;

	while is_complete == False:
		adjacent_cells = [];
		if current_point[0] != 0:										
			adjacent_value = get_grid_cell(grid, current_point[0]-1, current_point[1]);
			if adjacent_value == Directions.empty.value:
				adjacent_cells.append((current_point[0]-1,current_point[1]));		
		
		if current_point[0] != size:										
			adjacent_value = get_grid_cell(grid, current_point[0]+1, current_point[1]);
			if adjacent_value == Directions.empty.value:
				adjacent_cells.append((current_point[0]+1, current_point[1]));	
				
		if current_point[1] != 0:											
			adjacent_value = get_grid_cell(grid, current_point[0], current_point[1]-1); 
			if adjacent_value == Directions.empty.value:
				adjacent_cells.append((current_point[0], current_point[1]-1));

		if current_point[1] != size:
			adjacent_value = get_grid_cell(grid, current_point[0], current_point[1]+1);
			if adjacent_value == Directions.empty.value:
				adjacent_cells.append((current_point[0], current_point[1]+1));

		if len(adjacent_cells) != 0:
			previous_point = current_point;
			current_point = adjacent_cells[random.randint(0, len(adjacent_cells)-1)];
			bit_count = get_direction(previous_point, current_point);
			grid = update_grid_cell(grid, previous_point[0], previous_point[1], get_direction(previous_point, current_point));
			grid = update_grid_cell(grid, current_point[0], current_point[1], get_direction(current_point, previous_point));
		
		else:
			if is_spaces_available(grid) == True:
				current_point = get_random_point(grid, size, 1);	
			else:
				is_complete = True;

	return grid;

# Function Tuple<Int, Int> get_random_point(Grid grid, Int size, Int value)	
# 	Declare Bool is_valid = False
# 	Declare Tuple<Int, Int> point
# 	Declare Int cell_value
# 	While is_valid == False
# 		Set point = (random(size), random(size))
# 		Set cell_value = get_grid_cell(grid, point[0], point[1])
# 		If value == 1
# 			If cell_value >= value
# 				is_valid = True
# 		Else If cell_value == value
# 			If cell_value == value
# 				is_valid = True
# 	return point
# End Function

def get_random_point(grid, size, value):
	point = ();
	cell_value = 0;
	is_valid = False;
	while is_valid == False:
		point = (random.randint(0, size), random.randint(0, size));
		cell_value = get_grid_cell(grid, point[0], point[1]);
		if value == 1:
			if cell_value >= value:
				is_valid = True;
		elif cell_value == value:
			if cell_value == value:
				is_valid = True;
	return point

# Function Int get_direction(Tuple[int, int] previous_point, Tuple[Int, Int] current_point) 
# 	Declare x_distance = previous_point[0] - current_point[0]
# 	Declare y_distance = previous_point[1] - current_point[1]
# 	If x_distance < 0 
# 		return Directions.right
# 	Else If x_distance > 0
# 		return Direction.left
# 	Else If y_distance < 0
# 		return Directions.up
# 	Else If y_distance > 0
# 		return Directions.down
# 	else return 0 
# End Function

def get_direction(previous_point, current_point):
	y_distance = previous_point[0] - current_point[0];
	x_distance = previous_point[1] - current_point[1];
	if x_distance < 0:
		return Directions.right.value;
	elif x_distance > 0:
		return Directions.left.value;
	elif y_distance > 0:
		return Directions.up.value;
	elif y_distance < 0:
		return Directions.down.value;
	else:
		return 0;

# Function Bool is_spaces_available()
# 	For each x_value in grid
# 		For each y_value in grid[x_value]
# 			If y_value == Directions.empty.value
# 				return True
# 	return False	
# End Function

def is_spaces_available(grid):
	for x_value in grid:
		for y_value in x_value:
			if y_value == Directions.empty.value:
				return True
	return False	

# Get input from user in a the specified type
# Function Type get_input(Type input_type, String requested_input)
#	Declare string input
#	Display "Please enter a value for " + requested_input
#	Input user_input
#	While validate_input(user_input, input_type) == False
#		Display "Input invalid, please enter a value for " + requested_input 
#		Input user_input
#	Return input As input_type
# End Function

def get_input(input_type, requested_input):
	user_input = input("Please enter a value for " + requested_input + ": ");
	while validate_input(user_input, input_type) == False:
		user_input = input("Input invalid, please enter a value for " + requested_input + ": ");
	return input_type(user_input);

# Validate the input can be cast as type
# Function Bool validate_input(String input, Type input_type)
#	Try input As input Type 
#		Return True
#	Catch
#		Return False
# End Function
	
def validate_input(input, input_type):
	try:
	    input_type(input);
	except:
		return False;
	return True;

main();
