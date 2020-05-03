FROM {{ cookiecutter.docker_base_image }}

COPY docker/docker-entrypoint.sh /home/
COPY requirements.txt /home/requirements.txt
RUN rm -rf /home/jovyan/work

RUN pip install -r /home/requirements.txt

ENTRYPOINT ["sh", "/home/docker-entrypoint.sh"]