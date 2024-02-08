user_answers = ["Yes", "", "No", "", "Maybe", "", "Yes"]

filtered_answers = list(filter(lambda x: len(x) > 0, user_answers))
print(filtered_answers)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Ebook(Book):
    def __init__(self, title, author, file_size):
        self.title = title
        self.author = author
        self.file_size = file_size


# complete the child class definition


my_ebook = Ebook("1984", "George Orwell", 10)
print(my_ebook.title)
print(my_ebook.author)
print(my_ebook.file_size, 'MB')
