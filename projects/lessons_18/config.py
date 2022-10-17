from decouple import config
host = '127.0.0.1'
user = config('user', default='')
password = config('password', default='')
db_name = 'animal_world'
port = '5432'