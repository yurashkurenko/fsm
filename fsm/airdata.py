import airtable
from configfsm import ATOKEN,ABASE,ATABLE
def getairdata():
#    aird=airtable.Airtable('appTrXBmiYXmKyLLj','bota','keybPU0bpOGwuAwRA')
    aird=airtable.Airtable(ATOKEN,ATABLE,ABASE)
    at1=aird.get_all(view='anstable', maxRecords=20)
    airo2=list(at1)
    airlist=[]
    for i in range(len(airo2)):
        l0=airo2[i].get('fields').get('вопрос')
        l1=airo2[i].get('fields').get('ответ')
        l2=airo2[i].get('fields').get('клавиатура')
        l3=airo2[i].get('fields').get('подсказка')
        l4=airo2[i].get('fields').get('команда')
        l5=airo2[i].get('fields').get('состояние')
        l6=airo2[i].get('fields').get('установитьсостояние')
        airlist.append([l0,l1,l2,l3,l4,l5,l6])
#    print(airlist)
    return airlist
    #return at1

# airo2=list(airdata.getairdata())
# >>> airo2[0].get('fields').get('ответ')
# 'Здравствуйте!'
# >>> airo2[0].get('fields').get('вопрос')
# 'привет'