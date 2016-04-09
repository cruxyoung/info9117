import os
import bluetest
import unittest
import tempfile


class BlueGardenTest(unittest.TestCase):
    def setUp (self):
        self.db_fd, bluetest.app.config['DATABASE'] = tempfile.mkstemp()
        bluetest.app.config['TESTING'] = True
        self.app = bluetest.app.test_client()
        bluetest.init_db()
        
    def login(self,username, password):
        return self.app.post('/login', data = dict(
        username=username,
        password=password,
        
        ), follow_redirects=True)
        
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
        
    def test_login_logout(self):
        rv=self.login('123','123')
        assert 'You were logged in' in rv.data
        
        
        
if __name__=='__main__':
    unittest.main()