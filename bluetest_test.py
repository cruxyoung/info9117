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
        
    def register(self, username, password, password2):
        return self.app.post('/register', data=dict(
        username=username,
        password=password,
        password2=password2
        ),follow_redirects=True)
        
        
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
        
    def test_login_logout(self):
        rv=self.login('123','123')
        assert 'You were logged in' in rv.data
        rv=self.logout()
        assert 'You were logged out' in rv.data
        rv=self.login('yangyang', 'yang')
        assert 'Invalid username' in rv.data
        rv=self.login('yang', 'ya')
        assert 'Invalid password' in rv.data
        
    def test_register(self):
        
        rv=self.register('yan','pwyan', 'pwyan')
        assert 'You were successfully registered and can login now' in rv.data
        rv=self.register('yan','pwyan', 'pwyn')
        assert 'The two passwords do not match' in rv.data
        rv=self.register('yan','', '')
        assert 'You have to enter a password' in rv.data
        rv=self.register('iin','fsd', 'fafs')
        assert 'The two passwords do not match' in rv.data
        
        
        
        
if __name__=='__main__':
    unittest.main()