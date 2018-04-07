l_news=['news']
l_music=['play music']
def news():
    print('Okay, here is the news of today: [INSERT NEWS HERE]')
def music():
    print('Okay, now playing music.')
def search(list,string):
    n=len(list)-1
    while n>=0:
        if list[n]==string:
            return True
        n-=1
    return False
print('Welcome! I am your virtual assistant.\nType "new command" to define a new name for a command.\nType "list commands" to list all the names for a certain command.')
list=[l_news,l_music]
while True:
    inp=input('')
    if inp=='new command':
        s=input('What is the name of the command: ')
        t=input('What does the command do: ') #insert an already-existing name for the specified command
        if search(l_news,t):
            l_news.append(s)
        elif search(l_music,t):
            l_music.append(s)
    elif inp=='list commands': #This lists all the names for a certain command
        s=input('What is the name of the command: ') #input a name for the command
        n=0
        if search(l_news,s):
            while n<len(l_news):
                print(l_news[n])
                n+=1
        if search(l_music,s):
            while n<len(l_music):
                print(l_music[n])
                n+=1
    elif search(l_news,inp):
        news()
    elif search(l_music,inp):
        music()
    else:
        print('That is not a valid input.')
# assistant
