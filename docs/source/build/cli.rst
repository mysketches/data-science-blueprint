Create your app
==================================================

After your project is deployed, the question of how you will interact with it remains. You can certainly open a Python shell
or call a Python command and call a module, but this is will require you to strictly interact with Python, which is not
very comfortable, in particular if you wish to deploy in production, and maybe interact with other programs.

This is why the blueprint also onboards command lines, so that you can call some specific modules with a dedicated command line
on your machine.

I guess this would be much more convenient to train a model by simply calling it in a shell::

        mymodel-cli train xgboost datafile.csv output

This is just an example to show you that working like will make your deployments and in-production executions much more
accessible.

Create you cli interfaces
##########################

You can declare your cli interfaces in the file ``setup.py``::

        entry_points={
                'console_scripts': [
                    'awesome-project-cli={}.commands.cmd:main'.format(config['application']['package'])
                ]
            }

For the sake of the blueprint, an example of entry point was written : ``awesome-project-cli``. You can access the source code of
this command line in the file ``commands/cmd.py``. You are free to update the entry points and add your owns as you wish.

In the blueprint's example, one sample call is defined like this::

        awesome-project-cli lorem 10 --text-size=50
