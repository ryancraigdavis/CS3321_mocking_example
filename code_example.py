def simple_example(cond):
    """Simple example that runs an if/then statement with hello world print"""
    loop_count = number_of_runs(cond)
    print_hello_world(loop_count)


def number_of_runs(cond):
    """Take a conditional, and output how many print calls to make"""
    loop_count = 0
    if cond:
        print("This is true")
        loop_count = 3
    else:
        print("This is false")
        loop_count = 1
    return loop_count


def print_hello_world(loop_count):
    """Prints hello world a set number of times depending on the arg passed"""
    for prints_called in range(0, loop_count):
        print("Hello world")
