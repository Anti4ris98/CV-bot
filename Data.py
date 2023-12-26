import os
import pickle
from pathlib import Path
from info import *

class Book:
    """Class for contacts and notes"""

    def __init__(self, filename=None) -> None:
        self.summary = Summary()
        self.academic = Academic()
        self.experience = Experience()
        self.contact = Contact()
        self.links = Links()
        self.filename = Path(__file__).parent / filename
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, "rb") as f:
                data = pickle.load(f)
                self.summary.data = data.get("sammary", Summary()) 
                self.academic.data = data.get("academic", Academic())
                self.experience.data = data.get("experience", Experience())
                self.contact.data = data.get("contact", Contact())
                self.links.data = data.get("links", Links())

        except:
            pass