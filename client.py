import argparse
import requests
import csv

# Description of the code shown in help
welcome = '''Command line interface to interact with webserver for basic operations.\n
Pass val1, val2 and op, or csv file name to open. '''
parser = argparse.ArgumentParser(description=welcome)


# Function to perform the http request to the server
def operation (val1, val2, operator):
	# Send http POST request
	data = {'val1' : val1, 'val2' : val2, 'op' : operator}
	r = requests.post('http://127.0.0.1:5000/calculator', data = data)
	return r.text



# Available parameters when executing the code
parser.add_argument('--val1', '-v1', help = 'Set first number of the operation')
parser.add_argument('--val2', '-v2', help = 'Set second number of the operation')
parser.add_argument('--operator', '-op', help = 'Set operator of the operation. Quote it for robustness')
parser.add_argument('--ocsv', '-csv', help = 'Load data from csv file')
parser.add_argument('--wfile', '-w', help = 'Write the operations in a .txt file')

args = parser.parse_args()

# Assign input to variables for further use
val1 = args.val1
val2 = args.val2
op = args.operator
file_csv = args.ocsv
output_file = args.wfile

# Check what arguments are passed
# Case with not enough arguments
if (val1 == None or val2 == None or op == None) and file_csv == None:
	print("Not enough arguments. Either pass val1, val2 and op, or csv file path to open.")

# Case where there's two values and an operator
elif (val1 != None and val2 != None and op != None):
	result = operation(val1, val2, op)
	print('''{} {} {} = {}'''.format(val1, op, val2, result))
	
# In case the user passes csv file name to open, proceed to reading it
# and storing it in table
if file_csv != None:
	table = []
	# Check if the path to file is correct, if not, notice the user
	try:
		with open(file_csv, newline='') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				table.append(row)
				
	except FileNotFoundError:
		print('File not found. Check path') 

	# For each row in the table, that is a pair of values and an operand, call operation function
	for row in table:
		result = operation(row[0], row[2], row[1])
		print('''{} {} {} = {}'''.format(row[0], row[1], row[2], result))


