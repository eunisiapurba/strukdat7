class Browser:
    def init(self):
        self.b_stack = []
        self.f_stack = []

    def go(self, url):
        self.b_stack.append(url)
        self.f_stack.clear()

    def back(self):
        if len(self.b_stack) > 1:
            self.f_stack.append(self.b_stack.pop())
            return self.b_stack[-1]

    def forward(self):
        if self.f_stack:
            self.b_stack.append(self.f_stack.pop())
            return self.b_stack[-1]

    def printAll(self):
        print(*self.b_stack)


browser = Browser()

browser.go("https://google.com")
browser.go("https://ukdw.ac.id")
browser.go("https://facebook.com")
browser.back() #output: https://ukdw.ac.id
browser.back() #output: https://google.com
browser.forward() #output: https://ukdw.ac.id
browser.go("https://twitter.com") 
browser.printAll() #output: https://google.com https://ukdw.ac.id https://twitter.com