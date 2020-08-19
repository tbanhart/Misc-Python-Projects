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

class Directions(enum.Enum):
	corner = -2
	border = -1;
	empty = 0;
	left = 1;
	up = 2;
	right = 4;
	down = 8;

def main():
	size = get_input(int, "size");
	grid = [];
	grid = grid_initialize(grid, size);
	grid = generate_grid(grid, size);
	output_grid(grid);
	grid_to_json(grid);

def output_grid(grid):
	line = "";
	for x_value in grid:
		line = ""
		for y_value in x_value:
			line += str(y_value);
			for digits in range(3 - len(str(y_value))):
				line += " ";
		print(line);

def grid_to_json(grid):
	with open("maze.json", "w+") as file:
		json.dump(grid, file);

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

def get_grid_cell(grid, x_value, y_value):
	return grid[x_value][y_value];

def set_grid_cell(grid, x_value, y_value, i_value):
	grid[x_value][y_value] = i_value;
	return grid;

def update_grid_cell(grid, x_value, y_value, i_value):
	grid = set_grid_cell(grid, x_value, y_value, get_grid_cell(grid, x_value, y_value) + i_value);
	return grid;

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

def is_spaces_available(grid):
	for x_value in grid:
		for y_value in x_value:
			if y_value == Directions.empty.value:
				return True
	return False	

def get_input(input_type, requested_input):
	user_input = input("Please enter a value for " + requested_input + ": ");
	while validate_input(user_input, input_type) == False:
		user_input = input("Input invalid, please enter a value for " + requested_input + ": ");
	return input_type(user_input);
	
def validate_input(input, input_type):
	try:
	    input_type(input);
	except:
		return False;
	return True;

main();
