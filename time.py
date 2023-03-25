# import time
# print(time.asctime())

# import sys 
# print(sys.stdin.readline())

def battling_ninja(ninja):
    if ninja < 10:
        print('Oh. I can defeat them!')
    elif ninja <30:
        print('emm... It\'s a little difficult, but I can try!')
    elif ninja <50:
        print('My god! Too much!')
    else:
        print('What?!')
battling_ninja(5)