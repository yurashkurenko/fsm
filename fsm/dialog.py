import airtable
import airdata
import alldatadb
from dbworkerredis import get_current_state, set_state

messagelist=airdata.getairdata()
def answer():
    print('вопрос')
def question():
    print('ответ')
    
def dialog(text,user_id):
    messagelist=airdata.getairdata()
#    print(messagelist)
    state=get_current_state(user_id)
    dialog=[]
    state=get_current_state(user_id)
    dialog.append(text)
    dialog.append(text+"\n"+user_id+"\n"+" состояние "+state+"\n"+" Ок")
    dialog.append("Что-то вводим")
    dialog.append("[['ОК']]")
    dialog.append("")
    dialog.append("")
    
    
#    print(dialog)
    # dialog=[]
    # dialog.append(text+messagelist[0][1])
    # dialog.append(messagelist[0][2])
    # dialog.append(messagelist[0][3])
    #state=alldatadb.getstate()
    #state=get_current_state(user_id)
    # for i in range(len(messagelist)):
        # #print(messagelist[i][0],messagelist[i][1])
        # if i==0:
            # dialog=[]
            # dialog.append(text+"\n"+messagelist[0][1]+"\n"+user_id+"\n"+' состояние-'+state)
            # dialog.append(messagelist[0][2])
            # dialog.append(messagelist[0][3])
        # if text==messagelist[i][0]:
            # dialog=[]
            # dialog.append(messagelist[i][1]+"\n"+user_id+"\n"+' состояние '+state)
            # dialog.append(messagelist[i][2])
            # dialog.append(messagelist[i][3])
            # print(text,dialog)
    # return dialog
    
    for i in range(len(messagelist)):
        # print("\n")
        # print(messagelist[i][0])
        # print(messagelist[i][1])
        # print(messagelist[i][2])
        # print(messagelist[i][3])
        # print(messagelist[i][4])
        # print(messagelist[i][5])
        # print(state)
        if (text==messagelist[i][0] and state==messagelist[i][4]):
            dialog=[]
            dialog.append(messagelist[i][0])
            dialog.append(messagelist[i][1]+"\n"+user_id+"\n"+' состояние '+state)
            dialog.append(messagelist[i][2])
            dialog.append(messagelist[i][3])
            dialog.append(messagelist[i][4])
            dialog.append(messagelist[i][5])
            # print(text,dialog)
    return dialog