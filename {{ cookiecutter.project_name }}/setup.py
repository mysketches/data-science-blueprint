from setuptools import setup
import configparser

config = configparser.ConfigParser()
config.read('setup.cfg')

setup(
    name=config['application']['package'],
    packages=[config['application']['package']],
    version=config['application']['version'],
    description='{{ cookiecutter.project_short_description }}',
    python_requires=config['application']['python'],
    author=config['application']['author'],
    author_email=config['application']['email'],
    maintainer=config['application']['author'],
    maintainer_email=config['application']['email'],
    license='{{ cookiecutter.opensource_licence }}',
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.application_cli_name }}={}.commands.cmd:main'.format(config['application']['package'])
        ]
    }
)
