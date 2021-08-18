import db
levelbuffer=[]
# def insertuser(user):
    # db.insert('users',{'user':user})
    # return
def setstate(state):
    db.updatestate(state)
    return
    
def getstate():
    state=db.getstate()
    return state
def userregistration(userreg):
    user=userreg[0]
    telegram_id=userreg[1]
    registration='registered'
    db.insert('users',{'user':user,'telegram_id':telegram_id,'registered':registration,'boxes':' '})   
# Для проверки пользователя и соответствия телеграм id в базе

def isuserregistered(userreg):
    reg='не зарегистрирован'
    userfromuserreg=userreg[0]
    users=db.fetchall('users',['user','telegram_id','registered'])
    for j in range(len(users)):
        userfromtable=list(users[j].values())
        if userfromtable[0]==userfromuserreg:
            if userfromtable[2]=='registered':
                reg='зарегистрирован'
#            userslist=list(users)
#    print(userreg)
#    print(users)
    return reg
    
def iduserregistered(userreg):
    reg='не зарегистрирован'
    print(userreg)
    users=db.fetchall('users',['user','telegram_id'])
    for j in range(len(users)):
        print(j)
        print(users[j])
        print(users[j].keys())
        print(users[j].values())
        userfromtable=list(users[j].values())
        print(userfromtable)
        a = set(userreg)
        b = set(userfromtable)
        if a==b:
            
            reg='зарегистрирован'  
        # print(userfromtable.values(0))
        # print(userfromtable.values(1))
        #s = sorted(userfromtable, reverse=True)
        #print(s)
#        userlist1=userlist1+' /'+list(users[j].values())[0]
#        
#    print(users)
    return reg

def userlist():
    userlist1=''
    users=[]
    users=db.fetchall('users',['user'])
    for j in range(len(users)):
        userlist1=userlist1+' /'+list(users[j].values())[0]
    return userlist1
    
def boxlist():
    boxlist1=''
    boxes=[]
    boxes=db.fetchall('boxes',['box'])
    for j in range(len(boxes)):
        boxlist1=boxlist1+' /'+list(boxes[j].values())[0]
    return boxlist1
    
def boxlistlist():
    boxes=[]
    boxes=db.fetchall('boxes',['box'])
    return boxes    

def menulevel(state=''):
    if state!="":
        db.updateml(state)
    ml=[]
    ml=db.fetchall('menulevel',['ml'])
    menulevel=(list(ml[0].values())[0])
    return menulevel
    
def messagestringbuffer(message=''):
    if message!='':
        db.updatemsb(message)
    msb=[]
    msb=db.fetchall('messagestringbuffer',['message'])
    message1=(list(msb[0].values())[0])
    return message1

def inputtext(text):
    return text
    
def buttonlist(state):
    buttontoople=db.fetchcelltext('botstate','keyboard',state)
    buttonstring=buttontoople[0]
    buttonlist=[]
    buttonlist=buttonstring.split(' ')
    return buttonlist
    
def message(state):
    messagetoople=db.fetchcelltext('botstate','message',state)
    messagestring=messagetoople[0]
    return messagestring 

def command(state):
    commandtoople1=db.fetchcelltext('botstate','level1',state)
    commandtoople2=db.fetchcelltext('botstate','level2',state)
    commandstring=commandtoople1[0]+' '+commandtoople2[0]
    return commandstring
    
def commandlv1(state):
    commandtoople1=db.fetchcelltext('botstate','level1',state)
    commandstring=commandtoople1[0]
    return commandstring
    
def commandlv2(state):
    commandtoople2=db.fetchcelltext('botstate','level2',state)
    commandstring=commandtoople2[0]
    return commandstring

def commandlv3(state):
    commandtoople3=db.fetchcelltext('botstate','level3',state)
    commandstring=commandtoople3[0]
    return commandstring
    
def commandlv4(state):
    commandtoople4=db.fetchcelltext('botstate','level4',state)
    commandstring=commandtoople4[0]
    return commandstring

def insertuser(user):
    db.insert('users',{'user':user})
    return
    
def deleteuser(user):
    iddelete=db.fetchidforusers(user)
    for i in range(len(iddelete)):
        db.delete('users',iddelete[i])
    return
    
def insertbox(box):
    api=''
    users=''
    db.insert('boxes',{'box':box,'api':api,'users':users})
    return
    
def deletebox(box):
    iddelete=db.fetchidforboxes(box)
    for i in range(len(iddelete)):
        db.delete('boxes',iddelete[i])
    return
    
def insertboxuser(box,user):
    listusers=db.getlistuserforbox(box)
    listusers=listusers+' '+user
    db.setlistuserforbox(box,listusers)
    return
    
def deleteboxuser(box,user):
    strusers=db.getlistuserforbox(box)
    listusers=[]
    listusers=strusers.split(' ')
    for i in range(len(listusers)):
        if listusers.count(user)>0:
            listusers.remove(user)
    strusers=' '.join(listusers)
    db.setlistuserforbox(box,strusers)
    return
    
def listboxusers(box):
    listusers=db.getlistuserforbox(box)
    return listusers
    
def selectbox(box=''):
    if box!='':
        db.updateselectedbox(box)
    box=[]
    box=db.fetchall('selectedboxusers',['box'])
    box=(list(box[0].values())[0])
    return box
   
def selectuser(user=''):
    if user!='':
        db.updateselecteduser(user)
    user=[]
    user=db.fetchall('selectedboxusers',['user'])
    user=(list(user[0].values())[0])
    return user
    
def selectboxbox(box=''):
    if box!='':
        db.updateselectedboxbox(box)
    box=[]
    box=db.fetchall('selectbox',['box'])
    box=(list(box[0].values())[0])
    return box
    
def boxkeyall():
    boxboxkey=db.fetchall('boxes',['box','api'])
    boxbox={}
    for i in range(len(boxboxkey)):
        boxbox[list(boxboxkey[i].values())[0]]=list(boxboxkey[i].values())[1]
    #print(boxbox.keys())
    #print(boxbox.values())
    return boxbox
    
def userboxlist(user):
    boxes=db.getlistboxforuser(user)
    return boxes[0]
    
def userlistusers():
    users=db.getlistusersuser()
    return users
    
def allboxes():
    boxes=db.getallboxes()
    listboxes=[]
    for i in range(len(boxes)):
        listboxes.append(boxes[i][0])
    return listboxes