l_news=['news']
l_music=['music']
l_email=['email']
l_translate=['translate']
def news():
    print('Okay, here is the news of today: [INSERT NEWS HERE]')
def music():
    print('Okay, now playing music.')
def email():
    print('Okay, here is your most recent email: [INSERT EMAIL HERE]')
def translate():
    print('[INSERT TRANSLATED TEXT HERE]')
def search(list,string):
    n=len(list)-1
    while n>=0:
        if list[n] in string:
            return True
        n-=1
    return False
def listnames(list,string):
    n=0
    if search(list,string):
        while n<len(list):
            print(list[n])
            n+=1
def new(l,s,t):
    if search(l,t):
        l.append(s)
def metanew(l,s,t):
    n=0
    while n<len(l):
        new(l[n],s,t)
        n+=1
print('Welcome! I am your virtual assistant.\nAvailable commands: news | music | email | translate\nType "new command" to define a new name for a command.\nType "list commands" to list all the names for a certain command.')
list=[l_news,l_music,l_email,l_translate]
while True:
    inp=input('')
    if inp=='new command':
        s=input('What is the name of the command: ')
        t=input('What does the command do: ') #insert an already-existing name for the specified command
        metanew(list,s,t)
    elif inp=='list commands': #This lists all the names for a certain command
        s=input('What is the name of the command: ') #input a name for the command
        listnames(l_news,s)
        listnames(l_music,s)
        listnames(l_email,s)
        listnames(l_translate,s)
    elif search(l_news,inp):
        news()
    elif search(l_music,inp):
        music()
    elif search(l_email,inp):
        email()
    elif search(l_translate,inp):
        translate()
    else:
        print('That is not a valid input.')
# assistant
