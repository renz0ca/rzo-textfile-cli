import re
import numpy


class TextFile:

    def __init__(self, file):
        """
        Creates a new TextFile.

        Args:
            file (str): The path to the text file.
        """
        self.file = file

    def get_text_content(self):
        """
        Returns the text file's text content.

        Returns:
            str: The text file's text content.
        """
        with open(self.file, 'r') as file:
            txt = file.read()
        return txt

    def get_char_count(self):
        """
        Returns the text file's character count.

        Returns:
            int: The text file's character count.
        """
        txt = self.get_text_content()
        return len(txt)

    def get_word_count(self):
        """
        Returns the text file's word count.

        Returns:
            int: The text file's word count.
        """
        txt = self.get_text_content()
        return len(re.split(r"\s+", txt))

    def get_file_vector(self, scalar):
        """
        Returns a vector containing the text file's char and word count.

        Args:
            scalar (int): A scalar to apply to the vector.

        Returns:
            array: A vector containing the text file's char and word count.
        """
        return numpy.array([self.get_char_count(), self.get_word_count()]) * scalar
