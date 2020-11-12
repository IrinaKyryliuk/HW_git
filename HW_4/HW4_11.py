#HW_4 Level 1 1.Зчитати дані з вхідного файлу Car_Model_List.jsonта вивести на екран.
#Level 2 
# 1. Вивести список доступних брендів авто
# 2. Вивести список моделей вказаного бренду користувачем
# 3. Пошук моделі по імені
# 4. Знайти усі моделі виробника за вказаний проміжок часу
# Level3
# 1. Додати можливість пошуку по частковій назві авто або бренду
# 2. Додати можливість виводуавтівок вказаного виробника з пагінацією (5 автівок на сторінку)
# 3. Додати можливість сортування за роком/назвою/виробником. Порядок сортування може бути як asc, так і desc.
# Результат має бути відображений у формі таблички.
# parsing json
def getFile(fileName):
    file = open(fileName)
    return file.read()

def getObjects(jsonString):
    specSymbols = ('[',']','{','}',':',',')

    parts = []
    value = ""
    for symbol in jsonString:
        tmpValue = value.strip()
        if len(tmpValue) < 1 and symbol in specSymbols:
            parts.append(symbol)
        else:
            value += symbol
        if len(tmpValue) > 0:
            if symbol =="\"":
                parts.append(tmpValue[1:])
                value = ""
            elif symbol in (',', '}', ']') and "\"" not in value:
                parts.append(float(value[:-1]))
                parts.append(symbol)
                value = ""
    return parts
def parseArray(data):
    jsonArray = []
    data = data[1:]
    if data[0] == ']':
        return jsonArray, data[1:]
    while True:
        value, data = tryParseObject(data)
        jsonArray.append(value)
        if data[0] == ']':
            return jsonArray, data[1:]
        elif data[0] != ',':
            raise Exception('Expected comma after value')
        data = data[1:]

def parseObject(data):
    jsonObject = {}
    data = data[1:]

    if data[0] =='}':
        return jsonObject, data[1:]
    while True:
        key = data[0]
        if data[1] != ':':
            raise Exception('Expected colon after key')
        value, data = tryParseObject(data[2:])
        jsonObject[key] = value

        if data[0] == '}':
            return jsonObject, data[1:]
        elif data[0] != ',':
            raise Exception('Expected coma after value')
        data = data[1:]

def tryParseObject(data, root = False ):
    if root and data[0] not in ('{', '['):
        raise Exception('incorrect structure')

    result = (data[0], data[1:])
    if data[0] == '{':
        result = parseObject(data)
    elif data[0] == '[':
        result = parseArray(data)
    return result[0] if root else result
    
jsonString = getFile('D:/HW_git/HW_4/Car_Model_List_Full.json')
data = getObjects(jsonString)
data = tryParseObject(data, True)
print(type(data))
print()
print(data)
#Level 2 
# 1. Вивести список доступних брендів авто
print()
print("car's number = ", len(data))
make =[]
for make_list in data:
    make.append(make_list['Make'])
print('---list of brands---')
print(*make)
# 2. Вивести список моделей вказаного бренду користувачем
brand = input('--- enter brand ---')
model = []
for make_list in data:
    if brand == make_list['Make']:
        model.append(make_list['Model'])
if(len(model)==0):
    print('enter correct name of brand')
elif(len(model)>0):   
    print('brand', brand, 'model :', model)
# 3. Пошук моделі по імені
model_input = input('--- enter model ---')

for model_list in data:
    if model_list['Model'] == model_input:
        print(model_list)
    
# 4. Знайти усі моделі виробника за вказаний проміжок часу'''
interval_start = input('--- enter  time interval start in format "yyyy-MM-ddTHH:mm:ss.SSSZ" ---')
interval_end = input('--- enter time interval end in format "yyyy-MM-ddTHH:mm:ss.SSSZ"---')
interval = []
interval_s = []
for interval_list in data:
    if interval_start <= interval_list['createdAt'] and interval_list['createdAt'] <= interval_end:
        interval.append(interval_list['Model'])
interval_s = list(set(interval)&set(model))
if(len(interval_s)==0):
    print('enter correct time interval')
elif(len(interval_s)>0):   
    print('brand : ', brand,'; interval time with: ', interval_start,'to: ', interval_end , '; model :', interval_s)
