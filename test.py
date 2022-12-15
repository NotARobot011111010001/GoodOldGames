from main import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index (self):
        tester=app.test_client(self)
        response=tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code,200)

    # Ensure that the about page loads correctly
    def test_about_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertTrue(response.status_code, 200)

    # Ensure that the games page loads correctly
    def test_games_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/games', content_type='html/text')
        self.assertTrue(response.status_code, 200)

    # Ensure that the gamesInfo page loads correctly
    def test_games_info_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/games_info', content_type='html/text')
        self.assertTrue(response.status_code, 200)

    # Ensure that the home page loads correctly
    def test_home_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(response.status_code, 200)

    # Ensure that the index page loads correctly
    def test_index_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(response.status_code, 200)

    # Ensure that the reviews page loads correctly
    def test_reviews_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/reviews', content_type='html/text')
        self.assertTrue(response.status_code, 200)

    # Ensure that the reviews(mongodb) page loads correctly
    def test_reviews_mongodb_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/mongo', content_type='html/text')
        self.assertTrue(response.status_code, 200)    

    # Ensure that the reviews(googlebucket) page loads correctly
    def test_reviews_google_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/google', content_type='html/text')
        self.assertTrue(response.status_code, 200) 

if __name__=='__main__':
    unittest.main()