import requests
import alldatadb
import db
all=[]
all= alldatadb.boxlistlist()
#print(all)
#all=['13o1','1o2','1o3','2o1','2o2','2o3','2o4','3o1','3o2','3o3','3o4','4o1','4o2','4o3']
#all=['13o1','1o2','1o3','2o1','2o2','2o3','2o4','3o1','3o2','3o3','3o4','4o1','4o2','4o3']
server='192.168.1.60:8080'
#roomkey='h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz'
#response=requests.get('http://82.146.54.116:8080/lOZID_NzdLlF1oSx99GznhAr_I6eBuR3/get/V0')
##http://blynk-cloud.com/auth_token/update/pin?value=value
# roomkey={'13o1': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '1o2': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '1o3': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '2o1': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '2o2': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '2o3': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '2o4': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '3o1': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '3o2': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '3o3': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '3o4': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '4o1': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '4o2': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         # '4o3': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz'}
roomkey=alldatadb.boxkeyall() 
#print(roomkey.keys())  
#      tuple_as_dictionary = dict((letter, number) for (number, letter) in a_tuple)

#print(roomkey.get('2o4'))         
selectbox=''
selectbox=alldatadb.selectboxbox()
#print(selectbox)
alldatadb.selectboxbox('1.3')
selectbox=alldatadb.selectboxbox()
#print(selectbox)



select_room=alldatadb.selectboxbox()
#resptext='http://'+server+'/'+roomkey.get(select_room)+'/'
def zeropoint(select_room):
    zeropoint = select_room.replace('o', '.', 1)
    return zeropoint
    
# def door_check(select_room):
    # block_resp='http://'+server+'/'+roomkey.get(select_room)+'/get/V0'
    # response_block=requests.get(block_resp)

    # check_block=response_block.text[2]
# #   print(response.text)
    
    # if check_block=='1':
        # checkmessage1='?????????? ??????????????????????????.'
    # else:
        # checkmessage1='?????????? ????????????????????????.'
    
    # open_resp='http://'+server+'/'+roomkey.get(select_room)+'/get/V1'
    # response_open=requests.get(open_resp)
    # check_open=response_open.text[2]
    
    # if check_open=='0':
        # checkmessage2='?????????? ??????????????'
    # else:
        # checkmessage2='?????????? ??????????????'
    
    # checkmessage="???????? "+zeropoint(select_room)+", "+checkmessage2+", "+checkmessage1
    # print(checkmessage)
    # return checkmessage
def door_check(select_room):  
    checkmessage='?????????? ??????????????. ?????????? ????????????????????????.'
    return checkmessage
    
# def door_block(select_room):
     # t_resp='http://'+server+'/'+roomkey.get(select_room)+'/update/V9?value="1"'
     # print(t_resp)
     # response=requests.get(t_resp)
     # checkmessage=door_check(select_room)
     # return checkmessage
     
def door_block(select_room):
    checkmessage='?????????? ??????????????. ?????????? ????????????????????????.'
    return checkmessage

# def door_unblock(select_room):
     # t_resp='http://'+server+'/'+roomkey.get(select_room)+'/update/V8?value=1'
     # print(t_resp)
     # response=requests.get(t_resp)
     # checkmessage=door_check(select_room)
     # return checkmessage

def door_unblock(select_room):
    checkmessage='?????????? ??????????????. ?????????? ??????????????????????????.'
    return checkmessage