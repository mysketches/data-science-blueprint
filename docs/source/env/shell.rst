Shell
==================================================

It is possible to open a shell to your environment. This can be useful if you want to manually install dependencies to
your environment, or test a python script. Please note though that the operations that you will apply to your environment
will not be persistent. This means that if you manually install dependencies and restart your Docker environment, you will
have to install your dependencies again. To make them persistent, you may update the ``requirements.txt`` file and persist
by rebuilding the environment.

To access your environment shell, just use this command::

        $ make environment-shell

This will behave a bit the same as if you were using SSH. Once in the shell, you can simply exit it with a ``exit`` command.

Working with your packaged project
########################################
Every time you start your environment, your project will be packaged and deployed in the environment. It is then made possible
to import your project in your notebooks, and work with as if you had installed a new dependency.

You can then add some code to your project, and live test it with Python scripts. As you update your code, its packaged version
in PYTHON_PATH will automatically be updated.

This can be very useful as for instance, it allows you to create some test scripts (you may store them in the script folder
in the environment, and they will be mapped with the scripts folder in your project), and test/challenge your code.

If you decide to test your code with Python command in interactive mode, you will need to reload the python cache in your
environment, to take into account the code updates. You can also exit the python interactive mode, and reload it again.