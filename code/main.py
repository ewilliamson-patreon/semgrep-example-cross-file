
from code.folder.another_file import do_something


def user_input():
    return {"id": "123"}


def main():
    data = user_input()
    do_something(data.get("id"))

if __name__ == "__main__":
    main()
