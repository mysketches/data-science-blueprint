Unit tests
==================================================

I 've decided to use pytest package to run unit tests.

To run unit tests over your project, you can use the command::

        $ make test

The unit tests are located in the package's test folder. I recommend you follow the folder structure of the files that
are tested. For instance in the blueprint, the python code that is covered with unit tests is located in the ``operators``
folder. This is why unit tests are located in the folder ``tests/operators``.

The output of the unit test will look like this::

        platform darwin -- Python 3.7.2, pytest-5.4.1, py-1.8.0, pluggy-0.13.1
        collected 4 items

        awesome_project/tests/operator/test_data.py .               [ 25%]
        awesome_project/tests/operator/test_dataframe.py ..         [ 75%]
        awesome_project/tests/operator/test_generator.py .          [100%]

        ======================== 4 passed in 0.82s =============================
➜