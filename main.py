print('Hello from Zhalgas Zhaksylyk')

from dotenv import load_dotenv
import os

def print_author():
    load_dotenv(dotenv_path=r'C:\Users\Zhalgas\Desktop\Новая папка\Яндекс Практикум\Git\1_learn\.env')
    author = os.getenv('AUTHOR')
    print(f'Author of project is :{author}')

print(print_author())
