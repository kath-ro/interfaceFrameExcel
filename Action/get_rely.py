from utils.md5_encrypt import md5_encrypt
from Config.public_data import REQUEST_DATA, RESPONSE_DATA

class GetRely(object):
    def __init__(self):
        pass

    @classmethod
    def get(cls, dataSource, relyData):
        dataS = dataSource.copy()
        for key, value in relyData.items():
            if key == "request":
                # 说明应该去REQUEST_DATA获取数据
                for k, v in value.items():
                    interfaceName, case_id = v.split("->")
                    try:
                        val = REQUEST_DATA[interfaceName][case_id][k]
                        if k == "password":
                            dataS[k] = md5_encrypt(val)
                        else:
                            dataS[k] = val
                    except Exception as err:
                        pass
            elif key == "response":
                # 说明需要去RESPONSE_DATA获取数据
                for k, v in value.items():
                    interfaceName, case_id = v.split("->")
                    try:
                        dataS[k] = RESPONSE_DATA[interfaceName][case_id][k]
                    except Exception as err:
                        pass
        return dataS

if __name__ == "__main__":
    {"request-用户注册->1" :{"username": "zhangsan008", "password": "zhangsan01"}}
    REQUEST_DATA = {"用户注册": {"1": {"username": "zhangsan008", "password": "zhangsan01"}}}  # request
    RESPONSE_DATA = {}  # response
    s = {"username": "", "password": ""}
    rely = {"request": {"username": "用户注册->1", "password": "用户注册->1"}}
    print(GetRely.get(s, rely))