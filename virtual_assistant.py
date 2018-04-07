l_news=['news']
l_music=['music']
l_email=['email']
def news():
    print('Okay, here is the news of today: [INSERT NEWS HERE]')
def music():
    print('Okay, now playing music.')
def email():
    print('Okay, here is your most recent email: [INSERT EMAIL HERE]')
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
print('Welcome! I am your virtual assistant.\nType "new command" to define a new name for a command.\nType "list commands" to list all the names for a certain command.')
list=[l_news,l_music,l_email]
while True:
    inp=input('')
    if inp=='new command':
        s=input('What is the name of the command: ')
        t=input('What does the command do: ') #insert an already-existing name for the specified command
        if search(l_news,t):
            l_news.append(s)
        elif search(l_music,t):
            l_music.append(s)
        elif search(l_email,t):
            l_email.append(s)
    elif inp=='list commands': #This lists all the names for a certain command
        s=input('What is the name of the command: ') #input a name for the command
        listnames(l_news,s)
        listnames(l_music,s)
        listnames(l_email,s)
    elif search(l_news,inp):
        news()
    elif search(l_music,inp):
        music()
    elif search(l_email,inp):
        email()
    else:
        print('That is not a valid input.')
# assistant
