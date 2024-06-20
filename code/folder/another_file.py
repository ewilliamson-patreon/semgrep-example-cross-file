
from code.another_folder.dangerous_sink import dangerous_sink

def do_something(id: int):
    # ruleid: user_input_to_dangerous_sink
    dangerous_sink(id)
