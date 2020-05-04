Commands
==================================================

Your work environment will be built with Docker. Therefore, in order to create this environment, you will have to build
a Docker image.

To build your environment, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-build

Start your environment
########################
Starting your environment will allow you to access your shell, and Jupyter notebooks. Once the environment is started,
you can immediately use your browser to connect to Jupyter notebooks on your localhost.

To start your environment, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-start

Stop your environment
########################
To stop your environment, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-stop

Restart your environment
########################
To restart your environment, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-restart

Get your environment status
################################
To check whether your environment is running, and where you can access your Notebooks interface, just open a terminal,
move to the folder where the blueprint is installed, and type in the following command::

        $ make environment-status

Access your environment shell
################################
You can load a shell in your environment. This will allow you call your project package through command lines, and also
test your code. To enter your shell, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-shell

Load the sample data
########################
The blueprint comes with some sample data to load into your project. This command will only be useful for the sake of
the tutorial. You may update this command according to your needs.

The data that will be loaded into your project is a data sample of the visitors and travellers arriving in New Zealand from June 2014 to June 2019. To load this data, just open a
terminal, move to the folder where the blueprint is installed, and type in the following command::

        $ make environment-data

Clean your project
########################
This command will remove from your project all the temporary files, in particular those that shall never be pushed on Github.
If you identify other temp files to add, feel free to update the Makefile.

To clean your project, just open a terminal, move to the folder where the blueprint is installed, and type in the following command::
