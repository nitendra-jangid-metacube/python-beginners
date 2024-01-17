# abstract base class(ABC class)
from abc import ABC, abstractmethod
class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class Hp(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling on Hp laptop")
class Dell(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling on Dell laptop")
        
class HpNoteBook(Hp):
    def click(self):
        print("Clicking on Hp Notebook")
class DellNoteBook(Dell):
    def click(self):
        print("Clicking on Dell Notebook")

# creating object
hp_notebook = HpNoteBook()
dell_notebook = DellNoteBook()
# calling scroll method
hp_notebook.scroll()  # Output: Scrolling on Hp laptop
dell_notebook.scroll()  # Output: Scrolling on Dell laptop
# calling click method
hp_notebook.click()  # Output: Clicking on Hp Notebook
dell_notebook.click()  # Output: Clicking on Dell Notebook