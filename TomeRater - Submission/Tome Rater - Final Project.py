#Capstone Project - TomeRater
#Programmed by Connor Emory Waxberg
#March 17, 2019

#User class - Identifies and stores the information of the User 
class User():
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        #Maps a book to a users rating e.g. {1984 : 3, etc.}
        self.books = {}
        
    def get_email(self):
        return self.email
        
    def change_email(self, address):
        self.email = address
        return "{name}'s email has been updated.\n".format(name = self.name)

    def __repr__(self):
        return "User: {name} \nEmail: {email} \nBooks read: {books}.".format(name = self.name, email = self.email, books = len(self.books)) 

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating
        return self.books

    def get_average_rating(self):
        average = 0
        if self.books.values is not None and self.books.values is not 0:
            for i in self.books.values():
                if i is None:
                    continue
                average += i
            return average/len(self.books)
        else:
            return ("No ratings found")


#Book Class
class Book():

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self):
        return self.title
        
    def get_isbn(self):
        return self.isbn
       
    def set_isbn(self, updated_isbn):
        self.isbn = updated_isbn
        return "The isbn for \"{}\" has been updated.\n".format(self.title)

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid rating. Enter an acceptable rating.\n")

    def get_average_rating(self):
        average_score = 0
        if len(self.ratings) > 0:
            for i in self.ratings:
                average_score += i
            return average_score/len(self.ratings)
        else:
            average_score = 0
            return "There are no ratings currently for \"{}\"".format(self.title)
    
    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__ (self, other_value):
        return self.title == other_value.title and self.isbn == other_value.isbn

    def __repr__(self):
        return "{title}.\n".format(title = self.title)


#Fiction Class
class Fiction(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}.\n".format(title = self.title, author = self.author)
    

#Non-Fiction Class
class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a(n) {level} manual on {subject}.\n".format(title = self.title, level = self.level, subject = self.subject)


#TomeRater Application Class
class TomeRater():

    def __init__(self):
        #self.users stores the email with a value of the user data e.g. {email : user_data}
        self.users = {}
        #Maps a book to the number of users who have read that book {book_name : num_of_reads}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating = None):
       if email in self.users:
           assign_book_to_user = self.users.get(email, "No email in key found!")
           assign_book_to_user.read_book(book, rating)
           if book not in self.books:
               self.books[book] = 1
               if rating is not None:
                   book.add_rating(rating)
           else:
               self.books[book] += 1
               book.add_rating(rating)
       if email not in self.users:
           return "No user with email \"{email}\" found!".format(email = email)
                    
    def __repr__(self):
        return "User: {name} \nEmail: {email} \nBooks read: {books}.".format(name = self.name, email = self.email, books = len(self.books)) 

    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for i in user_books:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        for book_info in self.books.keys():
            print(book_info)
        
    def print_users(self):
        for user_info in self.users.values():
            print(user_info)

    def most_read_book(self):
        most_read = ""
        most_read_amount = 0
        for key, value in self.books.items():
            if value > most_read_amount:
                most_read_amount = value
                most_read = key
        return most_read

    def highest_rated_book(self):
        highest_rating = 0
        book_highest_rated = ""
        for key in self.books.keys():
            i = key.get_average_rating()
            if i > highest_rating:
                highest_rating = i
                book_highest_rated = key
        return book_highest_rated

    def most_positive_user(self):
        most_positive = ""
        most_positive_rating = 0
        for key, value in self.users.items():
            i = value.get_average_rating()
            if i > most_positive_rating:
                most_positive_rating = i
                most_positive = key
        return most_positive

