# class Book():
#     def read(self):
#         print("Чтение интересной истории")
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()

# принцип инверсии зависимостей (Dependency Inversion Principle)

from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Чтение интересной истории")

class AudioBook(StorySource):
    def get_story(self):
        print("Чтение интересной истории вслух")

class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

book = Book()
audiobook = AudioBook()

readerBook = StoryReader(book)

readerAudioBook = StoryReader(audiobook)

readerBook.tell_story()
readerAudioBook.tell_story()