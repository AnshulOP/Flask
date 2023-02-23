                                                           Dyanmic URLs
In Flask, dynamic or custom URLs can be defined by including variable sections in the URL pattern. These variable sections are indicated by enclosing them in <> brackets, with the name of the variable inside the brackets. When a user requests a URL that matches the pattern with the variable section, Flask captures the corresponding value from the URL and passes it as an argument to the corresponding view function.

Here's an example of how to define a dynamic URL in Flask:

    @app.route('/profile/<username>')
    def profile(username):
        return f"Hello, {username}!" #the f before the string indicates that it is an f-string, which allows you to embed expressions inside string literals, using curly braces {}.      
In this example, the URL pattern is /user/<username>, where username is a variable section. When a user requests a URL like /user/john, Flask captures the value john from the URL and passes it as an argument to the profile view function. The profile view function then uses the captured value to generate a personalized message for the user.

Multiple variable sections can also be included in a single URL pattern by separating them with slashes.
  
Dynamic URLs in Flask provide a powerful way to handle different types of requests from users with a single view function. By including variable sections in the URL pattern, Flask can capture and pass relevant information to the view function, making it easy to generate personalized responses for each user.
