from flask import Flask

# Create a new Flask application instance
basics = Flask(__name__)

# Create a route that handles requests to the root URL
@basics.route('/')
def welcome():
    # Return a message to the user
    return "Welcome to my Github, you will learn more about Flask here"

# Create a route that handles requests to the "/information" URL
@basics.route('/information')
def myself():
    # Return a message to the user
    return "My name is Anshul and I have a very keen interest in Data Science"

# This statement ensures that the server is only started when the script is run directly, not when it is imported as a module.
if __name__ == '__main__':
    # Run the application in debug mode, which allows for more detailed error messages to be displayed
    basics.run(debug=True)
