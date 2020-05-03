Project operations
==================================================

The Makefile will help you work on the structure of your project. Data science projects are about coding of course,
but it is also about all that is going around, such as working on a Jupyter notebooks interface, running unit tests, and
even deploying your project.

To work your project beyond coding, all you will need is the ``make`` command installed on your machine. Depending on
your operating system, there are many ways to install ``make``.

Install dependencies
########
The blueprint comes with a ``requirements.txt`` file, whose purpose is to list the packages that will be required to
work your project.

Here is the list of the requirements that come with the blueprint::

        coverage
        flake8
        numpy
        pandas
        scikit-learn
        matplotlib
        docopt
        configparser
        pytest

You are indeed encouraged to update this file and make it fit your needs.

To install the dependencies on your machine, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make install

Update dependencies
########
In order to update the version of your dependencies (because you have specified a specific version of a dependency in
the ``requirements.txt`` file, or because there is a newer latest version of the dependency on pypi), you can open a
terminal, move to the folder where the blueprint is installed, and type in the following command::

        $ make upgrade

Install your project as a package on your machine
########
You can package your project, and install it as a python package on your machine. Once packaged, your project is part
of the Python path, and can be called in another project or anywhere else on your machine.

In particular, you could also imagine packaging your project in a Docker image, and deploy it in the Cloud. You could then
spawn resources and call entry points to run your data science project.

To package your project on your machine, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make package

After this command is complete, you can import your project in any python script that would be running on your machine.

Build your environment
########
Your work environment will be built with Docker. Therefore, in order to create this environment, you will have to build
a Docker image.

To build your environment, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-build

Start your environment
########
Starting your environment will allow you to access your shell, and Jupyter notebooks. Once the environment is started,
you can immediately use your browser to connect to Jupyter notebooks on your localhost.

To start your environment, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-start

Stop your environment
########
To stop your environment, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-stop

Restart your environment
########
To restart your environment, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-restart

Get your environment status
########
To check whether your environment is running, and where you can access your Notebooks interface, just open a terminal,
move to the folder where the blueprint is installed, and type in the following command::

        $ make environment-status

Access your environment shell
########
You can load a shell in your environment. This will allow you call your project package through command lines, and also
test your code. To enter your shell, just open a terminal, move to the folder where the blueprint is installed,
and type in the following command::

        $ make environment-shell

Load the sample data
########
The blueprint comes with some sample data to load into your project. This command will only be useful for the sake of
the tutorial. You may update this command according to your needs.

The data that will be loaded into your project is a repartition of the population across regions in New Zealand. To load this data, just open a
terminal, move to the folder where the blueprint is installed, and type in the following command::

        $ make environment-data

Clean your project
########
This command will remove from your project all the temporary files, in particular those that shall never be pushed on Github.
If you identify other temp files to add, feel free to update the Makefile.

To clean your project, just open a terminal, move to the folder where the blueprint is installed, and type in the following command::

        $ make clean

Test your project
########
To run unit tests to your project, just open a terminal, move to the folder where the blueprint is installed, and type in the following command::

        $ make test

Visualize the tests coverage for your project
########
After running your unit tests, you can use visualization of the tests coverage. To do so, just open a terminal, move to the folder where the blueprint is installed, and type in the following command::

        $ make coverage

Check the code quality of your project
########
The Data Science blueprint uses Flake8 to test the code quality of the project. To output the coding styles tests that
wouldn't pass, just open a terminal, move to the folder where the blueprint is installed, and type in the following command::

        $ make lint
