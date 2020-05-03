Make the environment your own
==================================================

The blueprint's environment is entirely managed with Docker. Therefore, if you wish to customize the environment, you may
update the following files

Updating Dockerfile
########################
The Dockerfile's content is pretty straightforward::

        FROM jupyter/base-notebook:python-3.7.6

        COPY docker/docker-entrypoint.sh /home/
        COPY requirements.txt /home/requirements.txt
        RUN rm -rf /home/jovyan/work

        RUN pip install -r /home/requirements.txt

        ENTRYPOINT ["sh", "/home/docker-entrypoint.sh"]

The installation process is explained as follow:

- Load the base docker image for jupyter notebooks
- Copy the starting script
- Copy the python dependencies list
- Install the dependencies
- Map the image starting script with the one we have just added

Updating docker-entrypoint
##########################
The purpose of the docker-entrypoint script is just to prepend the jupyter workspace launch with a package build of your project.
Thanks to this docker-entrypoint script, you can use your project as a python package, in your working environment.

The docker-entrypoint file is located here : ``docker/docker-entrypoint.sh``
