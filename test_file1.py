# class Test_A:
#     def test_add(self):
#         a=3
#         b=6
#         c=a+b
#
#         if c<0:
#             print('test case passed')
#         else:
#             print('test case failed')

# class Test_A:
#     def test_add(self):
#         a=3
#         b=6
#         c=a+b
#
#         if c<0:
#             assert True
#         else:
#             assert False

class Test_A:
    def test_add(self):
        a=3
        b=6
        c=a+b
        print(c)
        if c>0:
            assert True
        else:
            assert False

# class Test_B:
#     def __init__(self):
#         p,q=10,20
#         r=p*q
#         print(r)
#         if r==30:
#             assert False
#         else:
#             assert True

class Test_B:
    def test_mul(self):
        p,q=10,20
        r=p*q
        print(r)
        if r==200:
            assert False
        else:
            assert True