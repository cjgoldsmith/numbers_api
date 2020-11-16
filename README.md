# numbers_api
Small Sample API for converting numbers to speech

# Directions to start
* Go into base dir and type `docker-compose up`
* Hit the convert api eg: http://localhost:8000/ntos/api/v1/convert/1223

# Directions for running tests
* `docker-compose run --rm django_test`

# Divergence from assignment
* API endpoint is in the wrong location on the server.
* As written if there are non-digit character presented to the end point it will 404 instead of possibly using the 'status' field in the response.
* GET API endpoint uses url params instead of GET body. Did not want to use the GET body value. Honestly not sure if rest framework supports that use case.