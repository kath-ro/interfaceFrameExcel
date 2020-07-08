#数据存储文件
from Config.public_data import REQUEST_DATA,RESPONSE_DATA

class RelyDataStore(object):
    def __init__(self):
        pass
    @classmethod
    def do(self, storePoint, apiName, caseId, request_source, response_source):
        for key,value in storePoint.items():
            if key=="request":
                #说明依赖的存储数据是来自于请求参数
                for i in value:
                    if i in request_source:
                        if apiName not in REQUEST_DATA:
                            #说明存储数据的结构还未生成，需要指明数据存储结构
                            REQUEST_DATA[apiName]={str(caseId):{i:request_source[i]}}
                        else:
                            #说明存储数据结构中最外层结构是存在的
                            if str(caseId) in REQUEST_DATA[apiName]:
                                REQUEST_DATA[apiName][str(caseId)][i] = request_source[i]
                            else:
                                REQUEST_DATA[apiName][str(caseId)] = {i: request_source[i]}

                    else:
                        print("请求参数中不存在字段" + i )
            elif key=="response":
                #说明依赖的存储数据是来自于响应参数
                for j in value:
                    if j in response_source:
                        if not apiName in RESPONSE_DATA:
                            #说明存储数据结构还未生成，需要指明数据存储结构
                            RESPONSE_DATA[apiName] = {str(caseId):{j:response_source[j]}}
                        else:
                            #说明存储数据结构中最外层结构存在
                            if str(caseId) in RESPONSE_DATA[apiName]:
                                RESPONSE_DATA[apiName][str(caseId)][j] = response_source[j]
                            else:
                                RESPONSE_DATA[apiName][str(caseId)] = {j: response_source[j]}

                    else:
                        print("响应body中不存在字段" + j)
        #print("RESPONSE_DATA = ", RESPONSE_DATA)
        #print("REQUEST_DATA = ", REQUEST_DATA)


if __name__ == "__main__":
    r = {"username": "qcjl001", "password": "12qwe", "email": "wsddw@qq.com"}
    s = {"request": ["username", "password"], "response": ["userid"]}
    res = {"userid": 12, "code": "00"}
    RelyDataStore.do(s, "register", 1, r, res)
    #print(REQUEST_DATA)
    #print(RESPONSE_DATA)