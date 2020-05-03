Build & Start
==================================================

The blueprint's environment runs with Docker. Therefore, before using it, you must build it. All is done thanks to the
``Dockerfile`` file that is located at the root of the project.

The content of the Dockerfile is pretty straightforward::

        FROM jupyter/base-notebook:python-3.7.6

        COPY docker/docker-entrypoint.sh /home/
        COPY requirements.txt /home/requirements.txt
        RUN rm -rf /home/jovyan/work

        RUN pip install -r /home/requirements.txt

        ENTRYPOINT ["sh", "/home/docker-entrypoint.sh"]

The base image used (base-notebook here) can be configured in the ``cookiecutter.json``. In this file, you can set the
default value for the ``docker_base_image`` parameter, and you will also be prompted the parameter when installing the blueprint
with the ``cookiecutter`` command.

When the blueprint's environment is built, you can start it with this command::

        $ make environment-start

The output of this command should be::

        8c512b6e09c1b5551075fb8921b24f08044dad876e102cd0e7f1813943c1816a
        Environment is running!
        Notebooks interface is available at http://localhost:8888

The Jupyter notebook interface is then accessible through port 8888 (by default). It is also possible to configure the default port
value in the ``cookiecutter.json`` file.

All the dependencies listed in the file ``requirements.txt`` will be loaded in the environment during its build. This means that if you
update the file requirements.txt and you want to add those new dependencies to the environment, you will need to build it again.

To do so, just launch a new build thanks to the following command::

        $ make environment-build
