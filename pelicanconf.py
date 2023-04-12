from os import environ as env


AUTHOR = env.get('AUTHOR')
SITENAME = env.get('SITENAME') or 'ag•photos'
TIMEZONE = env.get('TIMEZONE', 'Europe/Belgrade')
DEFAULT_DATE = 'fs'
STATS_SCRIPTS_URL = 'https://stat.arsgab.io/stonks.js'
STATS_WEBSITE_ID = env.get('STATS_WEBSITE_ID')

# Disable category/author/feeds pages build
CATEGORY_SAVE_AS = AUTHOR_SAVE_AS = ''
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = DISPLAY_CATEGORIES_ON_MENU = False

# Build setup
DIRECT_TEMPLATES = ['index']
PATH = 'articles'
ARTICLE_SAVE_AS = PAGE_SAVE_AS = '{slug}.html'
ARTICLE_URL = PAGE_URL = '/{slug}'
OUTPUT_PATH = 'dist/'
THEME = 'assets'
THEME_STATIC_DIR = 'static'
PLUGIN_PATHS = ['markup']
PLUGINS = ['renderers']
STATIC_PATHS = []

# Processors/renderers setup
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.meta': {},
        'markup.processors.picture': {},
    },
    'output_format': 'html5',
}

# Media processing setup
IMGPROXY_KEY = env.get('IMGPROXY_KEY')
IMGPROXY_SALT = env.get('IMGPROXY_SALT')
IMGPROXY_FQDN = env.get('IMGPROXY_FQDN', 'img.arsgab.io')
