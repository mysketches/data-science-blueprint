Installation
==================================================

Installing the blueprint will be quite easy.

First, you need to install cookiecutter, with this command::

        pip install cookiecutter

Now Cookiecutter is installed, you can install the Data Science blueprint::

        cookiecutter https://github.com/mysketches/data-science-blueprint

The blueprint should now be installed in the folder matching the value you set for the cookiecutter variable ``project_name``.

After testing the blueprint, I found situations where the cookiecutter would not be recognized. If this happens,
you can call it with this alternate command::

        python -m cookiecutter https://github.com/mysketches/data-science-blueprint
