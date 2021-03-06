
# timeouts
TIMEOUT = 30
WAIT_TIME = 0.0

MAX_TIMEOUT = 60.0
MAX_WAIT_TIME = 10.0

# png rendering options
VIEWPORT = '1024x768'
VIEWPORT_FALLBACK = VIEWPORT  # do not set it to 'full'
VIEWPORT_MAX_WIDTH = 20000
VIEWPORT_MAX_HEIGTH = 20000
VIEWPORT_MAX_AREA = 4000*4000

MAX_WIDTH = 1920
MAX_HEIGTH = 1080

AUTOLOAD_IMAGES = 1

# This value has the same meaning as "level" kwarg of :func:`zlib.compress`:
# - 0 means no compression at all
# - 1 means best speed, lowest compression ratio
# - 9 means best compression, lowest speed
#
# The default is 1, because it is twice as fast as 9 and produces only 15%
# larger files.
PNG_COMPRESSION_LEVEL = 1

# There's a bug in Qt that manifests itself when width or height of rendering
# surface (aka the png image) is more than 32768.  Usually, this is solved by
# rendering the image in tiled manner and obviously, TILE_MAXSIZE must not
# exceed that value.
#
# Other than that, the setting is a tradeoff between performance and memory
# usage, because QImage that acts as a rendering surface is quite a resource
# hog.  So, if you increase tile size you may end up using a lot more memory,
# but there is less image pasting and the rendering is faster.  As of now, 2048
# size is chosen to fit commonly used 1080p resolution in one tile.
TILE_MAXSIZE = 2048

# defaults for render.json endpoint
DO_HTML = 0
DO_IFRAMES = 0
DO_PNG = 0
SHOW_SCRIPT = 0
SHOW_CONSOLE = 0
SHOW_HISTORY = 0
SHOW_HAR = 0

# servers
SPLASH_PORT = 8050
PROXY_PORT = 8051
MANHOLE_PORT = 5023
MANHOLE_USERNAME = 'admin'
MANHOLE_PASSWORD = 'admin'

# pool options
SLOTS = 50

# disk cache options - don't enable it unless you know what you're doing
CACHE_ENABLED = False
CACHE_SIZE = 50  # MB
CACHE_PATH = '.splash-cache'

# security options
ALLOWED_SCHEMES = ['http', 'https', 'data', 'ftp', 'sftp', 'ws', 'wss']
JS_CROSS_DOMAIN_ENABLED = False

# logging
VERBOSITY = 1
