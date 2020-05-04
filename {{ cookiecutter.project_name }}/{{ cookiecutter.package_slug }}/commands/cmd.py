"""{{ cookiecutter.package_name }} - machine-learning-production

Usage:
    {{ cookiecutter.application_cli_name }} lorem <iterations> [--text-size=<text_size>]
    {{ cookiecutter.application_cli_name }} data <data-url> <data-location>
    {{ cookiecutter.application_cli_name }} (-h | --help)

Arguments:
    <data-location>         Location to save the data file
    <data-url>              Location of the data file to download
    <iterations>            Number of times the text will be repeated

Options:
    --text-size=<text_size>    Lorem ipsum text size. [default: 50]
    -h --help                   Show this screen.
"""

from docopt import docopt

from {{ cookiecutter.package_slug }}.operator.data import get_data
from {{ cookiecutter.package_slug }}.operator.generator import generate


def main():
    arguments = docopt(__doc__)

    if arguments['lorem']:
        print(generate(arguments['<iterations>'], arguments['--text-size']))
    elif arguments['data']:
        get_data(arguments['<data-url>'], arguments['<data-location>'])


if __name__ == '__main__':
    main()
