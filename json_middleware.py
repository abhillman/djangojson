"""
Simple, but helpful and powerful Django middleware to automatically
parse incoming HTTP POST requests for JSON content. Makes JSON
available as request.JSON within each method on the server. Effectively
gets rid of redundant parse/try-catch blocks for POST'd JSON.
"""
__author__ = 'Aryeh Hillman'

import simplejson
class JSONMiddleware(object):
    """Class for processing incoming POST for JSON. Places
    JSON (if successfully parsed) under request.JSON as
    a python dictionary."""
    def process_request(self, request):
        """Django-expected method. Does the work for processing
        incoming POST for JSON."""
        request.JSON = None
        #if request.is_ajax():
        if request.META.get('CONTENT_TYPE'):
            if request.META.get('CONTENT_TYPE').count('application/json'):
                try:
                    request.JSON = simplejson.loads(request.body)
                except simplejson.JSONDecodeError:
                    pass

