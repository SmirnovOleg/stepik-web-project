def app(environ, start_response):
	query = environ['QUERY_STRING']
        data = [bytes(item + '\n', 'ascii') for item in query.split('&')]
	status = '200 OK'
	headers = [('Content-type', 'text/plain')]
	start_response(status, headers)
	return data
