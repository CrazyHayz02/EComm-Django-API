from rest_framework.throttling import UserRateThrottle

class ProductWriteThrottle(UserRateThrottle):
    scope = "product_write"