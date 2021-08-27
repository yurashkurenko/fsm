from redis import Redis
import configfsm
# Пытаемся узнать из базы «состояние» пользователя
def get_current_state(user_id):
    with Redis() as db:
        try:
            return db[user_id].decode() # Если используете Vedis версии ниже, чем 0.7.1, то .decode() НЕ НУЖЕН
        except KeyError:  # Если такого ключа почему-то не оказалось
            return configfsm.States.S_START.value  # значение по умолчанию - начало диалога
# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    with Redis() as db:
        try:
            db[user_id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False
            
def get_reg(user_id):
    with Redis() as db:
        try:
            return db[user_id+'.reg'].decode() # Если используете Vedis версии ниже, чем 0.7.1, то .decode() НЕ НУЖЕН
        except KeyError:  # Если такого ключа почему-то не оказалось
            return configfsm.States.S_START.value  # значение по умолчанию - начало диалога
            
def set_reg(user_id, value):
    with Redis() as db:
        try:
            db[user_id+'.reg'] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False          