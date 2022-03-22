def chunks(seq: list, size: int):
    return (seq[i::size] for i in range(size))
