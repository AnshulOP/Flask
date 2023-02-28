                                                           make_response() function
In Flask, the make_response function is used to create a response object that can be returned to the client. It is often used in conjunction with cookies or when customizing the response headers.

What are response objects?

The response object is a crucial component in Flask web development as it is used to send a response back to the client once a request has been received by the server. The response object in Flask is an instance of the Response class which is used to generate the HTTP response returned to the client.

The response object can be customized to suit the needs of the application. For example, we can set cookies, headers, and the content type of the response using the make_response() function. This function allows us to create a response object from a string, tuple, or another response object.

Here are some use cases for make_response:

1. Setting Cookies: You can set cookies using the set_cookie method of the response object returned by make_response.
2. Customizing Response Headers: You can set custom headers using the headers attribute of the response object returned by make_response. For example, you could set the Content-Type header to "application/json" if you are returning JSON data.
3. Returning Complex Responses: You can return complex responses, such as streaming responses or responses that require custom encoding, by using make_response to create a response object and then customizing it as needed.

Overall, make_response is a useful function that provides flexibility in customizing Flask's response to a client.       

### cookies.set --> In Flask, cookies.set is used to set a cookie in the response. A cookie is a small piece of data that is stored on the client-side (i.e., the user's browser) by the web server.
### cookies.get --> In Flask, cookies.get() is a method used to retrieve the value of a cookie that was set in a previous request.
