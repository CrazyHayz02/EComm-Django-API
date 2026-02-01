from rest_framework.throttling import UserRateThrottle

# Custom throttle for product write operations
class ProductWriteThrottle(UserRateThrottle):
    scope = "product_write"