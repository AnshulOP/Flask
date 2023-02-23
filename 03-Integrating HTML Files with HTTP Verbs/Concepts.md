                                                        render_tempelate() function
render_template is a function in Flask that allows you to render HTML templates. It is used to display dynamic content in web applications built with Flask.

When a Flask application receives a request, it needs to return a response to the client. This response typically includes some HTML content that will be displayed in the user's web browser. However, the HTML content often needs to be customized with data from the Flask application.

This is where render_template comes in handy. It allows Flask to use a template engine to generate dynamic HTML pages. With render_template, you can create an HTML template that includes placeholders for dynamic data. You can then pass the dynamic data to render_template, and Flask will replace the placeholders in the HTML template with the actual data.                

                                                               request object
In Flask, the request object is a global object that represents the incoming HTTP request sent by the client (i.e., web browser). It contains all the data associated with the request, such as the form data, query parameters, cookies, headers, and files uploaded through the request.

When working with HTML forms, Flask uses the request object to retrieve the form data submitted by the user through the HTTP POST method. For example, suppose you have an HTML form with an input field named username and a submit button. When the user submits the form by clicking the button, Flask retrieves the value of the username input field using the request.form dictionary
