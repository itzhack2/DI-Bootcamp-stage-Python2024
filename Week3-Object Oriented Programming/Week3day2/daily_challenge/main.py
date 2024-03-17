# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

class Paginator:
    def __init__(self, content, items_per_page):
        self.content = content
        self.items_per_page = items_per_page
        self.total_items = len(content)
        self.total_pages = (self.total_items + items_per_page - 1) // items_per_page
        self.current_page = 1

    def get_current_page_content(self):
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        return self.content[start_index:end_index]

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            return True
        return False

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            return True
        return False

    def goto_page(self, page_number):
        if 1 <= page_number <= self.total_pages:
            self.current_page = page_number
            return True
        return False
    
content_list = [f"Item {i}" for i in range(1, 101)]  
items_per_page = 10
paginator = Paginator(content_list, items_per_page)
print("Current Page Content:", paginator.get_current_page_content())
paginator.next_page()

print("Current Page Content:", paginator.get_current_page_content())
paginator.goto_page(3)

print("Current Page Content:", paginator.get_current_page_content())


# The Pagination class will accept 2 parameters:
class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items or []
        self.pageSize = pageSize
        self.totalItems = len(self.items)
        self.totalPages = (self.totalItems + self.pageSize - 1) // self.pageSize
        self.currentPage = 1

    def get_current_page_items(self):
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        return self.items[start_index:end_index]

    def next_page(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
            return True
        return False

    def prev_page(self):
        if self.currentPage > 1:
            self.currentPage -= 1
            return True
        return False

    def goto_page(self, page_number):
        if 1 <= page_number <= self.totalPages:
            self.currentPage = page_number
            return True
        return False


alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
pagination = Pagination(alphabet_list, 4)

print("Current Page Items:", pagination.get_current_page_items())

pagination.next_page()
print("Current Page Items:", pagination.get_current_page_items())

pagination.goto_page(3)
print("Current Page Items:", pagination.get_current_page_items())
