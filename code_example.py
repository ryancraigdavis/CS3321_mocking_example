def simple_example(cond):
    """Simple Hello world Example"""
    conditional_var = cond
    run_loop = 0
    if conditional_var:
        print("This is true")
        run_loop = 3
    else:
        print("This is false")
        run_loop = 1
    for prints_called in run_loop:
        print("Hello world")
