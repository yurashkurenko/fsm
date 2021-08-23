import airtable
import airdata
import alldatadb
from dbworkerredis import get_current_state, set_state,get_reg,set_reg

messagelist=airdata.getairdata()
def answer():
    print('вопрос')
def question():
    print('ответ')
    
def dialog(text,user_id):
    messagelist=airdata.getairdata()
#    print(messagelist)
    state=get_current_state(user_id)
    debugmsg="\n"+text+"\n"+user_id+"\n"+' состояние '+state
    #debugmsg=''
    dialog=[]
    dialog.append(messagelist[0][0])
    dialog.append(messagelist[0][1]+debugmsg)
    dialog.append(messagelist[0][2])
    dialog.append(messagelist[0][3])
    dialog.append(messagelist[0][4])
    dialog.append(messagelist[0][5])
#    print(dialog)    

    for i in range(len(messagelist)):
        if (text==messagelist[i][0] and state==messagelist[i][5]):
            dialog=[]
            dialog.append(messagelist[i][0])
            dialog.append(messagelist[i][1]+debugmsg)
            dialog.append(messagelist[i][2])
            dialog.append(messagelist[i][3])
            dialog.append(messagelist[i][4])
            dialog.append(messagelist[i][5])
            # print(text,dialog)
#   print(dialog)
# Сохраняем ФИО
    if state=='10':
        print(user_id,text)
        regfamily=text
        #reg=[]
        reg={'user_id':user_id, 'family':regfamily}
        #reg.append(user_id)
        #reg.append(regfamily)
        print(reg)
        #string_reg=reg[0]+","+reg[1]
        string_reg=str(reg)
        print(string_reg)
        set_reg(user_id, string_reg)
        saveinfo=get_reg(user_id)
        print(saveinfo)
        state='0'
        # Сохраняем телефон
    if state=='11':
        print(user_id,text)
        regphone=text
        reg=eval(get_reg(user_id))
        reg['phone']=regphone
        #reg=[]
        #reg={'user_id':user_id, 'phone':regfamily}
        #reg.append(user_id)
        #reg.append(regfamily)
        print(reg)
        #string_reg=reg[0]+","+reg[1]
        string_reg=str(reg)
        print(string_reg)
        set_reg(user_id, string_reg)
        saveinfo=get_reg(user_id)
        print(saveinfo)
        state='0'
    return dialog