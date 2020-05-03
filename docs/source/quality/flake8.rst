Flake8
==================================================

I have chosen flake8 package to test coding conventions. Indeed, you are free to use your own, but flake8 is installed by default,
and it is working just fine.

Installation and usage
########################
To work it, you don't have to integrate anything in your code.

Here are the few steps to follow to use flake8 :

Installation (once)::

        $ make install

Use::

        $ make lint

Configure flake8
################
Flake8 configuration is stored in the file ``setup.cfg``. In the ``[flake8]`` section, you can update a few parameters::

        [flake8]
        max-line-length = 79
        max-complexity = 10
        filename = ./awesome_project/*.py

If you need to get some information about flake8 parameters, you can check these links:

- `flake8 options <https://flake8.pycqa.org/en/2.5.5/config.html>`_
- `flake8 error codes <https://flake8.pycqa.org/en/2.5.5/warnings.html#error-codes>`_
