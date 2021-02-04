from rest_framework import pagination
class CLGAPIPagination(pagination.LimitOffsetPagination):
    default_limit = 5