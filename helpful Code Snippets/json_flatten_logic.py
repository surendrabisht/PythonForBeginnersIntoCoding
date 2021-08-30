json = {"key1": 1,
        "Details": {"Name": "Surendra", "LastName": "bisht"},
        "Interests": [{"ComputerScience": {"topics": ["Algo", "Data Structures", "Design Patterns", "Distributed systems"],
                                           "Languages":["C#", "Java", "Python"]
                                           }}, {"Maths": ["coordinate geometry", "Trignometry", "calculus", "Algebra"]}, "Engineering Drawing", "Physics"]}


def flatten_it(parent, jsonText):
    text = {}
    newDic = {}
    if type(jsonText) is dict:
        for key in jsonText:
            newDic = flatten_it(parent+"_"+str(key), jsonText[key])
            text.update(newDic)
    elif type(jsonText) is list:
        i = 0
        for value in jsonText:
            newDic = flatten_it(parent+"_"+str(i), value)
            text.update(newDic)
            i = i+1
    else:
        text[parent] = jsonText
        # print(text)
    return text


flattenedJson = flatten_it("Root", json)
flattenedJSOText = str(flattenedJson)
flattenedJSOText = flattenedJSOText.replace("'", "\"")
print(flattenedJSOText)
