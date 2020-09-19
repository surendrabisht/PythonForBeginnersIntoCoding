json = {"key1":1,\
"Details": { "Name": "Surendra" , "LastName": "bisht"},\
"Interests": [  {"ComputerScience": {"topics": ["Algo","Data Structures","Design Patterns","Distributed systems"],\
"Languages":["C#","Java","Python"]\
}}\
,{"Maths":["coordinate geometry","Trignometry","calculus","Algebra"]}\
,"Engineering Drawing","Physics"]}


# def flatter_It(parent,jsonText):
#     text= {}
#     for key in jsonText:
#         if key is dict:
#             flatter_It(parent+"_"+key,jsonText[key])
#         elif key is list:
#             i=0
#             for value in key:
#                 flatter_It(parent+"_"+key+"_"+i,value)
#                 i=i+1
#         else:
#             text[parent]=jsonText

def flatter_It(parent,jsonText):
    text= {}
    newDic={}
    if type(jsonText) is dict:
        for key in jsonText:
            newDic=flatter_It(parent+"_"+str(key),jsonText[key])
            text.update(newDic)
    elif type(jsonText) is list:
        i=0
        for value in jsonText:
            newDic=flatter_It(parent+"_"+str(i),value)
            text.update(newDic)
            i=i+1
    else:
        text[parent]=jsonText
        #print(text)
    return text


flattenedJson=flatter_It("Root",json)
flattenedJSOText=str(flattenedJson)
flattenedJSOText=flattenedJSOText.replace("'","\"")
print(flattenedJSOText)




