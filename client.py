import argparse
import csv

# Description of the code shown in help
welcome = '''Command line interface to interact with webserver for basic operations.\n
Pass val1, val2 and op, or csv file name to open. '''
parser = argparse.ArgumentParser(description=welcome)

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

print('''val1 = {}, val2 = {}, op = {}, csv = {}, output = {}.txt'''.format(val1, val2, op, file_csv, output_file))
