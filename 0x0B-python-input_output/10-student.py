
#!/usr/bin/python3
"""
Module 10-student.

Contains class Student
that initializes public instance attributes first_name, last_name, and age,
and has public method to_json that retrieves its dictionary representation
of requested attributes or all if none were requested
"""


class Student:
    """
    Public Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with name & age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data struct
        (list, dictionary, dictionary, string)
        for JSON serialization of obj

        Return:
            Only return dict of attrs specified
            Or entire dict if not specified
        """
        if attrs is None:
            return self.__dict__
        else:
            dicto = {}
            for attr in self.__dict__.keys():
                dicto[attr] = self.__dict__[attr]
            return dicto
