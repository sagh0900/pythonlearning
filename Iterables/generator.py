from genlist import take
from genset import distinct


def run_pipeline():  # lazy pipeline
    items = [3, 6, 6, 2, 1, 1, 4]
    for item in take(4, distinct(items)):
        print(item)


if __name__ == '__main__':
    run_pipeline()