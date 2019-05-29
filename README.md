# WebServer
This is a python implementation of a client and a server to perform basic mathematical operations.
## server.py
This file contains a basic implementation of a flask server. The server runs in localhost, and serves POST http requests through port 5000.
In order to perform an operation it needs two numbers and an operator, corresponding to parameters val1, val2 and op.
It returns the result of the operation with two decimal places.

## client.py
This file performs http POST requests to the server in localhost port 5000. It consists on a Command Line Interface that allows the user to perform the desired operation through the server. The parameters it accepts when calling the function are `val1`, `val2`, `operator`, `ocsv` and `wfile`.
The simplest way to use this CLI is by passing two values and an operator, for example:
```
python client.py --val1 3 --val2 5 --operator '*'
```
Note: the operator is better if quoted, otherwise can lead to the error of not recognizing it.

Another way to use the CLI is by passing a csv file path to open it and perform the operations within it, for example:
```
python client.py --ocsv examples/sample.csv
```
Finally, the parameter `wfile` allows to specify a name for a txt file containing the operations, it can be used in combination with any of the other two examples:
```
python client.py --val1 3 --val2 5 --operator '*' --wfile results
python client.py --ocsv examples/sample.csv --wfile results
```
In both cases the results will be appended to the file results.txt.
In case all the parameters are passed, first the operation with `val1`, `val2` and `operator` will be sent to the server, followed by the operations from the csv file; all the operations will be added to output txt file.
## System requirements
The code has been tested in python 3.6.7, and all the required packages are in requirements.txt

## Testing examples of the server
The functioning of the server can be tested by using cURL commands. (cURL is a command line tool for transfering data with URLs)
Notice that curl by default does not encode the data using a UTF-8 charset. To be able to use it in the simplest the operators can be directly passed encoded in UTF-8. The only one not correctly encoded is the + operand that can be substituted by its UTF-8 encoded version ```%2B```.
Some examples:
To perform the operation 2 + 3: 
```
curl -d "val1=2&val2=3&op=%2B" http://127.0.0.1:5000/calculator
```
For the operation 12 - 7: 
```
curl -d "val1=12&val2=7&op=-" http://127.0.0.1:5000/calculator
```
For the operation 6 * 100: 
```
curl -d "val1=6&val2=100&op=*" http://127.0.0.1:5000/calculator
```
And the operation 7 / 5: 
```
curl -d "val1=7&val2=5&op=/" http://127.0.0.1:5000/calculator
```
