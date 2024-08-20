import json

profanityFilePathCSV="./profanityList.csv"
wordListFilePathJSON="./words.json"

profanityList=[]
newWordList=[]


def containsProfanity(word):
    for profanity in profanityList:
        if profanity in word:
            return True
    return False


with open(profanityFilePathCSV, "r", encoding='utf-8') as pf:
    for ln in pf.read().split("\n"):
        profanityList.append(ln.split(",")[0])


with open(wordListFilePathJSON, "r", encoding='utf-8') as j:
    jsonData=json.loads(j.read())
    for word in jsonData["data"]:
        if word in profanityList: continue
        if containsProfanity(word): continue
        
        newWordList.append(word)


jsonData["data"] = newWordList


with open("./words2.json", "w", encoding='utf-8') as j:
    json.dump(jsonData, j)