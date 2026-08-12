# Импорт load_dotenv.
from dotenv import load_dotenv

# Импорт библиотеки для работы с окружением.
import os

def print_author():

        load_dotenv(dotenv_path='/Users/yana/pract/proj_git/a.env')
        author = os.getenv('AUTHOR')
        print(f"Автор проекта: {author}")
print_author()
