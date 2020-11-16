FROM numbers_api_django_base:latest

ADD DOCKER/django_api/start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT ["/bin/bash", "/start.sh"]