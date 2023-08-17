class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author=author
        self.publication_year=publication_year

    def display_infor(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:",self.publication_year)

# Tao doi tuong
book1= Book("Gone with the Wind", "Margaret Mitchell", 1936)

# Hien thi thong tin
book1.display_infor()
