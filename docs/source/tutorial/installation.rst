Installation
==================================================

Installation of the blueprint will proceed as follow::

        $ pip install cookiecutter
        $ cookiecutter https://github.com/mysketches/data-science-blueprint

This should output the following form::

        full_name [John Doe]:
        email [john.doe@myemail.org]:
        project_name [DS-blueprint]:
        package_name [Awesome project]:
        package_slug [awesome_project]:
        project_short_description [No description]:
        version [0.1.0]:
        Select python_interpreter:
        1 - python3
        2 - python
        Choose from 1, 2 [1]:
        application_cli_name [awesome-project-cli]:
        Select opensource_licence:
        1 - MIT
        2 - BSD
        3 - ISCL
        4 - Apache Software License 2.0
        5 - Not open source
        Choose from 1, 2, 3, 4, 5 [1]:
        docker_base_image [jupyter/base-notebook:python-3.7.6]:
        docker_image_name [awesome-project-env]:
        docker_container_name [awesome-project-env-instance]:
        docker_container_port [8888]: 8082

Leave the fields blank if you wish to use the default values.

That's it, your blueprint is installed, and ready to work !