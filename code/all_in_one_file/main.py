def dangerous_sink(id: int):
    print(id)

def user_input():
    return {"id": "123"}

def do_something(id: int):
    # ruleid: user_input_to_dangerous_sink
    dangerous_sink(id)

def main():
    data = user_input()
    do_something(data.get("id"))

if __name__ == "__main__":
    main()
