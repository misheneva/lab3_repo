from main import BaseClient


class UserGet(BaseClient):
    method = "users.get"

    def __init__(self, username):
        self.username = username

    def get_params(self):
        return{

            'user_ids': self.username
        }
    def response_handler(self, response):
            b = response.json()
            print(b['response'][0]['uid'])
            return b['response'][0]['uid']


class FriendsGet(BaseClient):
    BASE_URL = "https://api.vk.com/method"
    method = "friends.get"

    def __init__(self, user_id):
        self.user_id = user_id

    def get_param(self):
        return{

            'user_id': self.user_id
        }
    def response_handler(self, response):  #обработчик результата
          data = response.json()
          c = {}
          for i in data['response']:
              try:
               if i["bdate"].split('.')[2] in c:
                   c[i["bdate"].split('.')[2]] +=1
               else:
                   c[i["bdate"].split('.')[2]] = 1
              except:
                    pass
          return c