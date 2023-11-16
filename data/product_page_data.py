"""
Global variables related to any product page.
"""

# Different product pages types
PRODUCT_PAGE_URL_LIST = [
    # Woman>Top>Jackets: without review, "As low" tag, Sizes US, Related products
    "https://magento.softwaretestingboard.com/juno-jacket.html",
    # Men>Bottom>Pants> with review, "As low" tag, Sizes EU, Liked products
    "https://magento.softwaretestingboard.com/kratos-gym-pant.html",
    # Gear>Bags: with review, no tag, no sizes, no colors, Liked products
    # "https://magento.softwaretestingboard.com/overnight-duffle.html"
    ]

# Watches doesn't have bottom block with related or liked products. For me, it's a bug but just in case:
WATCHES_URL_LIST = [
    "https://magento.softwaretestingboard.com/didi-sport-watch.html",
    "https://magento.softwaretestingboard.com/clamber-watch.html",
    "https://magento.softwaretestingboard.com/bolo-sport-watch.html",
    "https://magento.softwaretestingboard.com/luma-analog-watch.html",
    "https://magento.softwaretestingboard.com/dash-digital-watch.html",
    "https://magento.softwaretestingboard.com/cruise-dual-analog-watch.html",
    "https://magento.softwaretestingboard.com/summit-watch.html",
    "https://magento.softwaretestingboard.com/endurance-watch.html",
    "https://magento.softwaretestingboard.com/aim-analog-watch.html",
]

# Exclusion for US_002.005
EXCLUDED_URL_LIST = [
    "https://magento.softwaretestingboard.com/sprite-yoga-companion-kit.html",
    "https://magento.softwaretestingboard.com/set-of-sprite-yoga-straps.html"
]

MIN_TIMEOUT = 1
TIMEOUT = 10
MAX_TIMEOUT = 30

PRODUCT_PAGE_EXAMPLE = "https://magento.softwaretestingboard.com/breathe-easy-tank.html"