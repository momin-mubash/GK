from rest_framework.pagination import PageNumberPagination
class MyPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'#?page=1,2,3 wont work only ?p=1,2,3 will work
    page_size_query_param = 'records'#?p=1&records=10 will work..user will decide how many records to show in a page
    max_page_size = 10#user can not show more than 10 records in a page even if he wants to show more than 10 records in a page
    last_page_strings = 'end'#?p=end will take user to last page