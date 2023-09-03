import argparse
from .TextFile import TextFile


def __main__():
    """
    The program's core logic.
    """
    # Parse command line arguments
    args = parse_arguments()
    # Create TextFile
    file = TextFile(args.file)
    # Compute metrics
    if args.metric == 0:
        print(file.get_char_count())
    elif args.metric == 1:
        print(file.get_word_count())
    elif args.scalar != None:
        print(file.get_file_vector(args.scalar))
    else:
        print(file.get_text_content())


def parse_arguments():
    """
    Parses the program's command line arguments.

    Returns:
        dict: The program's command line arguments.
    """
    parser = argparse.ArgumentParser(
        description='A small command line tool for parsing text files.'
    )
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--metric', type=int, required=False)
    parser.add_argument('--scalar', type=int, required=False)
    return parser.parse_args()


if __name__ == "__main__":
    __main__()
