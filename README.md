Simple, but helpful and powerful Django middleware to automatically
parse incoming HTTP POST requests for JSON content. Makes JSON
available as request.JSON within each method on the server. Effectively
gets rid of redundant parse/try-catch blocks for POST'd JSON.

Usage:

One good option is to rename json_middleware.py as __init__.py. Place
it within a directory at the base of your Django project path (call it
middleware). Finally, add 'middleware.json_middleware' to your 
MIDDLEWARE_CLASSES variable within your projects settings.py file.
