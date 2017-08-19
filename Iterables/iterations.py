def first(iterable):
    """This method will work for list collection but will throw ValueError
        Exception while passing set or dictionary collection as iterable object
        since only ValueError is handled"""
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")

# first(["1st", "2nd", "3rd"]) = > 1st, calling again = > 2nd, at the end it will return ValueError message,
# when Iterable reached end of the list"
# But will throw TypeError when other collection is passed to first() function.
