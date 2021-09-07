import airtable
import airdata
import alldatadb
import registration
from dbworkerredis import get_current_state, set_state,get_reg,set_reg

messagelist=airdata.getairdata()
def answer():
    print('вопрос')
def question():
    print('ответ')
    
def dialog(text,user_id):
    messagelist=airdata.getairdata()
    print(messagelist)
    state=get_current_state(user_id)
    print(user_id+" "+state)
#    debugmsg="\n"+text+"\n"+user_id+"\n"+' состояние '+state
    debugmsg=''
    #regmsg=str(eval(get_reg(user_id)))
#    print(user_id)
    print(get_reg(user_id))
    #print(str(eval(get_reg(user_id))))
    userreg={}
    print(get_reg(user_id))
    userreg=eval(get_reg(user_id))
    print(userreg)
    regmsg="\n"+"Телеграм ИД"+userreg['user_id']+"\n"
    regmsg=regmsg+"ФИО - "+userreg['family']+"\n"
    regmsg=regmsg+"Телефон - "+userreg['phone']+"\n"
    regmsg=regmsg+"Организация - "+userreg['organ']
    dialog=[]
    dialog.append(messagelist[0][0])
    dialog.append(messagelist[0][1]+debugmsg)
    dialog.append(messagelist[0][2])
    dialog.append(messagelist[0][3])
    dialog.append(messagelist[0][4])
    dialog.append(messagelist[0][5])
    dialog.append(messagelist[0][6])
#    print(dialog)    

    for i in range(len(messagelist)):
#        if (text==messagelist[i][0] and state==messagelist[i][5]):
        if (text==messagelist[i][0] and state==messagelist[i][5]):
            print(state)
            print(messagelist[i][5])
            dialog=[]
            dialog.append(messagelist[i][0])
            dialog.append(messagelist[i][1]+debugmsg)
            dialog.append(messagelist[i][2])
            dialog.append(messagelist[i][3])
            dialog.append(messagelist[i][4])
            dialog.append(messagelist[i][5])
            dialog.append(messagelist[i][6])
        if text=="Информация о регистрации":
            dialog[1]="Информация о регистрации"+"\n"+regmsg
            
            # print(text,dialog)
#   print(dialog)
# Сохраняем ФИО
    if state=='10':
        print(user_id,text)
        regfamily=text
        #reg=[]
        reg={'user_id':user_id, 'family':regfamily, 'phone':"+78888888888", 'organ':"Организация"}
        # reg.append(user_id)
        # reg.append(regfamily)
        # reg.append(regfamily)
        # reg.append(regfamily)
        print(reg)
        #string_reg=reg[0]+","+reg[1]
        string_reg=str(reg)
        print(string_reg)
        set_reg(user_id, string_reg)
        saveinfo=get_reg(user_id)
        print(saveinfo)
        #state='1'
        # Сохраняем телефон
    if state=='11':
        print(user_id,text)
        regphone=text
        reg=eval(get_reg(user_id))
        reg['phone']=regphone
        string_reg=str(reg)
        set_reg(user_id, string_reg)
        saveinfo=get_reg(user_id)
        #state='1'
        # Сохраняем Организацию
    if state=='12':
        print(user_id,text)
        regorg=text
        reg=eval(get_reg(user_id))
        reg['organ']=regorg
        string_reg=str(reg)
        set_reg(user_id, string_reg)
        saveinfo=get_reg(user_id)
        state='1'
    return dialog