def fibonacci():
    """generator for getting the next fibonacci num"""
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second

    
def reader(txt_file: str, num_of_lines: int):
    """generator for getting the next x lines at every iter"""
    result = []
    with open(txt_file, 'r') as f:
        for i, line in enumerate(f, 1):
            result.append(line.strip('\n'))
            if i % num_of_lines == 0:
                yield result
                result = []
    if result:
        yield result