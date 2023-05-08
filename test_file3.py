import pytest

@pytest.mark.xfail
class Test_E:
    def test_assert(self):
        a=10
        b=30
        addition=a+b
        if addition==True:
           print('not matter')
        else:
           print('not matter')

class Test_F:
    def test_assert2(self):
        a=10
        b=30
        addition=a+b
        if addition==False:
           print('not matter')
        else:
           print('not matter')

@pytest.mark.skip
class Test_G:
    def test_assert3(self):
        a=10
        b=30
        addition=a+b
        if addition==False:
           assert True
        else:
           assert False