import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = Book(2311, 'East of Eden by John Steinbeck', 'Ali')
        self.book2 = Book(2532, 'The House of Mirth by Edith Wharton','Omar')

    def test_add_and_list(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.assertEqual(self.manager.list_books(), [self.book1, self.book2])

    def test_remove_book(self):
        self.manager.add_book(self.book2)
        self.manager.remove_book(2532)
        self.assertEqual(self.manager.list_books(), [])
        
    def test_remove_none_existent_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book(24214)
        self.assertEqual(self.manager.list_books(), [self.book1])
    
if __name__ == '__main__':
    unittest.main()
