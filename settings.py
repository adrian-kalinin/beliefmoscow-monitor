import dotenv
import os


dotenv.load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

KEYWORDS = ['jordan', 'dunk', 'sacai']

BASE_URL = 'https://beliefmoscow.com/'
CART_PATH = '/cart_items'
COLLECTION_PATH = '/collection/frontpage.json?page_size={page_size}&page={page}'
PAGE_SIZE = 100

SQLITE_PATH = 'db.sqlite3'

DELAY = 1
