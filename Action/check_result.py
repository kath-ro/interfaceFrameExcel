import re

class CheckResult(object):
    def __init__(self):
        pass

    @classmethod
    def check(self,responseObj,checkPoint):
        errorKey = {}

        for key,value in checkPoint.items():
            if isinstance(value,str):#说明是等值校验
                if key in responseObj:
                    if not responseObj[key] == value:
                        errorKey[key] = responseObj[key]
                else:
                    errorKey[key] = "not exists"
            elif isinstance(value,dict):#说明是需要通过正则校验或校验数据类型
                if "type" in value:#说明是整型
                    typeS = value["type"]
                    souceData = responseObj[key]
                    if typeS == "N":
                        if not isinstance(responseObj[key],int):
                            errorKey[key] = responseObj[key]
                    elif typeS == "S":
                        if not isinstance(responseObj[key],str):
                            errorKey[key] = souceData
                    elif typeS == "xxx":
                        pass
                elif "value" in value:#说明处理的是正则类型的
                    regStr = value["value"]
                    rg = re.match(regStr,"%s"%souceData)
                    if not rg:
                        errorKey[key] =souceData

        return errorKey


if __name__ == "__main__":
    r = {"code": "01", "userid": 12, "id": "12"}
    c = {"code": "00", "userid": {"type": "N"}, "id": {"value": "\d+"}}
    print(CheckResult.check(r, c))

