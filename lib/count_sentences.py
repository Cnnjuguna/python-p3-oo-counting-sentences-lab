#!/usr/bin/env python3
import re


class MyString:
    def __init__(self, value):
        """
        Purpose: value
        """
        self._value = value if isinstance(value, str) else ""
        # self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")  # Raise ValueError instead of printing

    def is_sentence(self):
        trimmed = self._value.strip()  # Remove leading and trailing whitespace
        # trimmed = trimmed.rstrip(string.punctuation)  # Remove trailing punctuation

        if trimmed.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        """
        if the value ends
        with a '?' mark and False if it does not.
        """
        trimmed = self._value.strip()  # Remove leading and trailing whitespace
        if trimmed.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        """
        if the value ends with
        an exclamation mark and False if it does not.
        """
        trimmed = self._value.strip()  # Remove leading and trailing whitespace
        if trimmed.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        sentences = re.split(r"[.!?]", self._value)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        num_of_sentences = len(sentences)
        return num_of_sentences


some_sentence = MyString(456)
some_sentence.value = 456
# some_sentence = MyString("MyString has something!Or nah? i will check?")
# some_sentence.value = "MyString has something!Or nah? i will check?"
print(some_sentence.is_question())
print(some_sentence.count_sentences())
