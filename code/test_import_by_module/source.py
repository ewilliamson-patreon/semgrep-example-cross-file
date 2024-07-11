from code.test_import_by_module import sink


def user_input():
    return {"id": "123"}


def doit():
    # this direct import is followed if uncommented
    # from code.test_import_by_module.sink import a_function
    # a_function(user_input())

    # BUG: this call is not followed in cross file
    sink.a_function(user_input())


if __name__ == "__main__":
    doit()
