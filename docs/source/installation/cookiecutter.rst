Using cookiecutter
==================================================

The blueprint will be installed using a great tool called cookiecutter. When launching Cookiecutter, the
program will ask for some variables, whose values will configure the blueprint in order to make it **your** project.

Here is the list of the variables that will be set by Cookiecutter

+---------------------------+------------------------------------+----------------------------------------------------------------------+
| Variable                  | Default value                      | Definition                                                           |
+===========================+====================================+======================================================================+
| full_name                 | John Doe                           | Name of the author / maintainer                                      |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| email                     | john.doe@myemail.org               | Email of the author / maintainer                                     |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| project_name              | DS project                         | Name of the folder where the blueprint will be installed             |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| package_name              | Awesome project                    | Name of the project                                                  |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| package_slug              | awesome.project                    | Formatted name of the project that will be used with packages        |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| project_short_description | No description                     | Description of your project                                          |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| version                   | 1.0.0                              | Version of the project                                               |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| application-cli-name      | {project_slug}-cli                 | Unix command to use your packaged project as an app                  |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| open_source_licence       |                                    | Licence for your project                                             |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| docker_base_image         | jupyter/base-notebook:python-3.7.6 | Docker image used to build the environment                           |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| docker_image_name         | {project_slug}-env                 | Name of the built Docker image that will be used as your environment |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| docker_container_name     | {project_slug}-instance            | Name of the Docker container that will be instanciated               |
+---------------------------+------------------------------------+----------------------------------------------------------------------+
| docker_container_port     | 8888                               | Port exposed to access Jupyter notebooks                             |
+---------------------------+------------------------------------+----------------------------------------------------------------------+

