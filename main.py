import re

emails = ['.denis.njima@gmail.com','denisnjima@gmail.com','23denisnjima@gmmail.com','-denis','@','samuel@', 'denis@gmail','denis@gmail123.org']

for email in emails:
     result = re.search(r'^[A-Za-z0-9.]+@[a-zA-Z0-9]+.[A-Za-z]{2,}$',email)
     if(result):
        print('Email: '+result.group()+' is correct.')
     else:
         print('Email: '+email+' is wrong')