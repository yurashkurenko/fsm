from enum import Enum

db_file = "database.vdb"
ATOKEN = 'appTrXBmiYXmKyLLj'
ABASE = 'keybPU0bpOGwuAwRA'
ATABLE = 'bota'
TOKEN = "720456901:AAHKxg2WHPqaaIemulTkO3x7IXGD-IZSd-w"

class States(Enum):
    """
    Мы используем БД Redis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_NAME = "1"
    S_ENTER_AGE = "2"
    S_SEND_PIC = "3"