Code coverage
==================================================
After running unit tests, you can display the code coverage of your project. To show the code coverage, simply use the command::

        $ make coverage

The output of the coverage report should look like this::

        Name                                              Stmts   Miss  Cover   Missing
        -------------------------------------------------------------------------------
        awesome_project/__init__.py                            4      0   100%
        awesome_project/operator/data.py                       6      0   100%
        awesome_project/operator/dataframe.py                  6      0   100%
        awesome_project/operator/generator.py                  4      0   100%
        awesome_project/tests/operator/test_data.py            6      0   100%
        awesome_project/tests/operator/test_dataframe.py      11      0   100%
        awesome_project/tests/operator/test_generator.py       3      0   100%
        -------------------------------------------------------------------------------
        TOTAL                                                40      0   100%
