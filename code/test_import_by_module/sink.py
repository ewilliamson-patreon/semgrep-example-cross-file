def a_function(a: str) -> None:
    # ruleid: user_input_to_dangerous_sink
    return dangerous_sink(a)


def dangerous_sink(a: str) -> None:
    return None
