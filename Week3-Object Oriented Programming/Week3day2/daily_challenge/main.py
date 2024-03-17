# Daily Challenge : Pagination
class Pagination:
    def __init__(self, items=None, pageSize=10):
        if items is None:
            items = []
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = -(-(len(items)) // self.pageSize) 
        self.currentPage = 1

    def getVisibleItems(self):
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = min(start_index + self.pageSize, len(self.items))
        return self.items[start_index:end_index]

    def prevPage(self):
        self.currentPage = max(self.currentPage - 1, 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.currentPage + 1, self.totalPages)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        self.currentPage = max(min(pageNum, self.totalPages), 1)
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())
p.nextPage().getVisibleItems()
print(p.getVisibleItems()) 
p.lastPage().getVisibleItems()
print(p.getVisibleItems()) 

p.goToPage(10)
print(p.currentPage)


