import urllib.request


def get_data(url, location):
    """Download the remote file, and store it on local disk

    Args:
        url (string): Url of the file to download
        location(string): File path of the downloaded file

    Raises:
        URLError: URL not found
    """
    try:
        urllib.request.urlretrieve(url, location)
    except ValueError as e:
        raise urllib.error.URLError(e)
