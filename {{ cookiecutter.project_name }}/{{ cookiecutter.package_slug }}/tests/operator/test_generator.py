import {{ cookiecutter.package_slug }} as pack


def test_generator():
    assert(isinstance(pack.generate(10, 10), list))
