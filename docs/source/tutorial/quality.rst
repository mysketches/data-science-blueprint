Quality testing
==================================================

You can check that the your project meets the Python coding conventions::

        $ make lint

If you try this command with the fresh installation of the blueprint, nothing should output this command as the code
written in the blueprint respects the conventions.

Let's run unit tests now::

        $ make test

This is the output you should get::

        =================================== test session starts ==============================
        platform linux -- Python 3.7.6, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
        rootdir: /data
        collected 4 items

        awesome_project/tests/operator/test_data.py .                                   [ 25%]
        awesome_project/tests/operator/test_dataframe.py ..                             [ 75%]
        awesome_project/tests/operator/test_generator.py .                              [100%]

        =================================== 4 passed in 0.84s ================================

Finally, you can launch a coverage test over your project::

        $ make coverage

This is the output you should get::

        Name                                               Stmts   Miss  Cover   Missing
        --------------------------------------------------------------------------------
        awesome_project/__init__.py                            4      0   100%
        awesome_project/operator/data.py                       6      0   100%
        awesome_project/operator/dataframe.py                  6      0   100%
        awesome_project/operator/generator.py                  4      0   100%
        awesome_project/tests/operator/test_data.py            6      0   100%
        awesome_project/tests/operator/test_dataframe.py      11      0   100%
        awesome_project/tests/operator/test_generator.py       3      0   100%
        --------------------------------------------------------------------------------
        TOTAL                                                 40      0   100%