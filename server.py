from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculator', methods=['POST'])
def calculator():
	if request.method == 'POST':
		
		# Store the values and operator passed
		# Check if val1 and val2 are numbers
		try:
			val1 = float(request.form.get('val1'))
			val2 = float(request.form.get('val2'))
		except ValueError:
			return '''NaN'''.format()
			
		operator = request.form.get('op')
		
		#Check if all the needed arguments are present
		if val1 == None or val2 == None or operator == None:
			return '''Not enough input parameters. Try again.\n'''.format()
		
		# Perform the corresponding operation
		if operator == '+':
			result = 1.0 * val1 + val2
		elif operator == '-':
			result = 1.0 * val1 - val2
		elif operator == '*':
			result = 1.0 * val1 * val2
		elif operator == '/':
			try:
				result = 1.0 * val1 / val2
			except ZeroDivisionError:
				return '''NaN'''.format()
		else:
			return '''Invalid operator or missing, try again.\n'''.format()
			
		# Return the result with two decimal places
		return '''{:.2f}'''.format(result)

if __name__ == '__main__':
    app.run()
