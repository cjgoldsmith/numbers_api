FROM numbers_api_django_base:latest

ADD DOCKER/django_test/start.sh /start.sh
RUN chmod +x /start.sh

ADD requirements-test.txt /code/requirements-test.txt
RUN pip install -r /code/requirements-test.txt

ENTRYPOINT ["/bin/bash", "/start.sh"]