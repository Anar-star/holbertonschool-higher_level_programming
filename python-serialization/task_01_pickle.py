#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """Serialize the current instance to a file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            # Handle file write or pickle errors gracefully
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """Deserialize an instance from a pickle file."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                else:
                    return None
        except (OSError, pickle.PickleError, EOFError):
            # Handle missing file, corrupted file, or invalid pickle
            return None
