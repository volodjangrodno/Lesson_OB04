# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f"Сформирован отчёт - {self.title} - {self.content}")



# принцип открытости/закрытости (Open closed Principle)

from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HTMLFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)

report = Report("заголовок отчёта", "Это текст отчёта, его тут много", TextFormatted())
report = Report("заголовок отчёта", "Это текст отчёта, его тут много", HTMLFormatted())

report.docPrinter()
