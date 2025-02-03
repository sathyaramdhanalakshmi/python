from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass
    
    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self, username, password):
        print(f"Google login successful for {username}")
    
    def logout(self):
        print("Google logout successful")

class FacebookAuth(UserAuthentication):
    def login(self, username, password):
        print(f"Facebook login successful for {username}")
    
    def logout(self):
        print("Facebook logout successful")

google_auth = GoogleAuth()
google_auth.login("user1", "password123")
google_auth.logout()

facebook_Auth= FacebookAuth()
facebook_Auth.login("user1", "123456789")
facebook_Auth.logout()
