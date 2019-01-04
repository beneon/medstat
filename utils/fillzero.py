import os
import re
from os import path
inputFile = path.join('utils','input.txt')
rst = []
with open(inputFile,'r',encoding='utf-8') as fhdlr:
    txt = fhdlr.read()
    txtlines = txt.split('\n')
    for l in txtlines:
        entry = [e.strip() for e in l.split('|')]
        rst.append(entry)
    
tpDate,tpTime,tpContent = zip(*rst)

def zeroFill(txt,splitter,template):
    reTemp = re.compile(template)
    # 原先采用splitter的形式, 但是只要复杂一点马上傻叉
    # 看来还是必须要用regex才行
    lTxt = txt.split(splitter)
    lTemplate = template.split(splitter)
    lPlaceHolder = [len(e) for e in lTemplate]
    lTxt = [('0'*lPlaceHolder[i]+e)[-lPlaceHolder[i]:] for (i, e) in enumerate(lTxt)]
    return splitter.join(lTxt)

tpDate = [zeroFill(e,"-",r"\d{4}-\d{1,2}-\d{1,2}") for e in tpDate]
tpTime = [zeroFill(e,":")]

        


