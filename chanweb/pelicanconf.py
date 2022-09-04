AUTHOR = 'Winyee'
SITENAME = 'Winyee Art Page'
SITEURL = ''

PATH = 'content'
# STATIC_PATHS=['sounds']
PLUGINS=['pelican.plugins.photos']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# PHOTO SETTINGS
# Base settings where to find the galleries with images
PHOTO_LIBRARY="content/images/"
PHOTO_RESIZE_JOBS = -1
PHOTO_INLINE_GALLERY_ENABLED = True
# We use the default settings here
PHOTO_INLINE_GALLERY_TEMPLATE = "inline_gallery"

# Use the name of the site as watermark text
# PHOTO_WATERMARK = True
# PHOTO_WATERMARK_TEXT = SITENAME

PHOTO_INLINE_GALLERY_ENABLED = True 
PHOTO_INLINE_GALLERY_PATTERN = 'gallery_name'



# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True