from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculator', methods=['POST'])
def calculator():
	if request.method == 'POST':
		
		# Store the values and operator passed
		val1 = float(request.form.get('val1'))
		val2 = float(request.form.get('val2'))
		operator = request.form.get('op')
		
		# Perform the corresponding operation
		if operator == '+':
			result = 1.0 * val1 + val2
		elif operator == '-':
			result = 1.0 * val1 - val2
		elif operator == '*':
			result = 1.0 * val1 * val2
		elif operator == '/':
			result = 1.0 * val1 / val2
		
		# Return the result with two decimal places
		return '''{:.2f}'''.format(result)

if __name__ == '__main__':
    app.run()
