Using the cli interface
==================================================

As the project is packaged in the environment, it is possible to use to run your project command lines. Open the environment shell::

        $make environment-shell

We will use a sample command written for the sake of the blueprint. It just generates a sequence of text. You can call it
like this::

        jovyan@awesome_project:~$ awesome-project-cli

As you didn't write any action to perform, here is the obvious output you'll get::

        Usage:
            mlp-cli lorem <iterations> [--text-size=<text_size>]
            mlp-cli data <data-url> <data-location>
            mlp-cli (-h | --help)

Let's use the lorem action. It generates a list of *lorem ipsum* text::

        jovyan@awesome_project:~$ awesome-project-cli lorem 10 --text-size=50

Here is the final output::

        ['Lorem ipsum dolor sit amet, consectetur adipiscing',
        'Lorem ipsum dolor sit amet, consectetur adipiscing',
        'Lorem ipsum dolor sit amet, consectetur adipiscing',
        'Lorem ipsum dolor sit amet, consectetur adipiscing',
        'Lorem ipsum dolor sit amet, consectetur adipiscing',
        'Lorem ipsum dolor sit amet, consectetur adipiscing',
        'Lorem ipsum dolor sit amet, consectetur adipiscing',
        'Lorem ipsum dolor sit amet, consectetur adipiscing',
        'Lorem ipsum dolor sit amet, consectetur adipiscing',
        'Lorem ipsum dolor sit amet, consectetur adipiscing']
