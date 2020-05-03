Package your project
==================================================

Packaging your project should be the final step before deploying in your production environment. The purpose of this step
is to convert your project to a Python package, that will be installed on your machine.

Once your project is packaged, it can be imported by any Python code that would be running on your machine. This makes your project
portable, and exportable in a Docker image, on Pypi repository, or on a remote machine. At this stage of the blueprint,
the strategy to deploy on production is yours.

To package your project, just use this command::

        $ make package

It is also the very same command that is used in the blueprint's environment, and allows you to use your packaged project
with your notebooks.