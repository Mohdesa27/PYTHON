# import Flask from flask module
from flask import Flask

# Creating an instance of flask app
app = Flask(__name__)

# Defining a route
@app.route('/home')
def home():
	return "Hello, Flask!"

# Run the application
if __name__ == '__main__':
	app.run()
