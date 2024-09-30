import os
import pandas as pd
import random
import vdf
from glob import glob

random_message = pd.read_csv(os.path.join(os.getcwd(), "uwu_word_list"))["0"]
def uwuficate(sentence) -> str:
    word_list = sentence.split()
    for number, word in enumerate(word_list):
        if word=="my":
            word_list[number]="mwy"
        elif word=="to":
            word_list[number]="tuwu"
        elif word=="had":
            word_list[number]="hawd"
        elif word=="you":
            word_list[number]="yuw"
        elif word=="go":
            word_list[number]="gow"
        elif word=="and":
            word_list[number]="awnd"
        elif word=="have":
            word_list[number]="haw"
            
        
        else:
            word = word.replace("ll", "w").replace("r", "w").replace("l", "w").replace("th", "d").replace("fu", "fwu")
            word_list[number]=word
            
        if random.randrange(0,11)==1:
            word_list[number] = word[0]+"-"+word
            
        if "." in word:
            word_list[number] = word_list[number] + " " + random_message[random.randrange(0,len(random_message))]
        if "!" in word:
            word_list[number] = word_list[number] + " " + random_message[random.randrange(0,len(random_message))] 
        if "?" in word:
            word_list[number] = word_list[number] + " " + random_message[random.randrange(0,len(random_message))]
            
        
    final = " ".join(word_list)
    return final

def work_file(file:str):
    d:vdf.VDFDict
    text = ""
    try:
        text = open(file, encoding="utf-8-sig").read()
    except:
        return

    d = vdf.loads(text)
    try:
        actual_dict:vdf.VDFDict = d["lang"]["Tokens"]
    except:
        return

    for k, v in actual_dict.items():
        uwu = uwuficate(v)
        actual_dict[k] = uwu
    with open(file, "w", encoding="utf-8-sig") as f:
        new_text = vdf.dumps(d)
        f.write(new_text)
    

result = [y for x in os.walk(os.getcwd()) for y in glob(os.path.join(x[0], '*english.txt'))]
for f in result:
    work_file(f)



    
        

        