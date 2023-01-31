def test():
    s="alo"
    def testsub():
        global s
        s="blo"
    testsub()
    print(s)
test()