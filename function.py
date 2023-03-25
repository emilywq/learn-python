def testfunc(myname):
    print('hello %s' % myname)
testfunc('emily')

def testfunc(firstname, secondname):
    print('Hello %s %s' % (firstname, secondname))
testfunc('Emily', 'Wan')

def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending
print('You\'re savings is %s.' % savings(10, 10, 5))