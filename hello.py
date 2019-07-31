def app(environ, start_response):
	query = environ['QUERY_STRING']
	data = b''
	for item in query.split('&'):
		data += item + b'\n'
	status = '200 OK'
	headers = [
		('Content-type', 'text/plain'),
		('Content-length', str(len(data)))
	]
	start_response(status, headers)
	return data
