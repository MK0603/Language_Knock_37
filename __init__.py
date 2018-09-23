# coding: UTF-8
from LanguageKnock_30 import makeMecabPattern
import numpy as np
import matplotlib.pyplot as plt
#matplotlib用日本語フォントのセット
from matplotlib.font_manager import FontProperties
font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

class extractVersMethods:
    def checkNovel(self, novelListS):
        wordCounter={}
        for sentenseList in novelListS:
            for word in sentenseList:
                if word["surface"]!="。" and word["surface"]!="、" and word["surface"]!="「" and word["surface"]!="」" and word["surface"]!="…":
                    if word["surface"] in wordCounter.keys():
                        wordCounter[word["surface"]] = wordCounter[word["surface"]]+1
                    else:
                        wordCounter.setdefault(word["surface"],1)
        sortedWordCounter=sorted(wordCounter.items(),key=lambda x:x[1],reverse=True)
        
        return sortedWordCounter
    


                

if __name__ == '__main__':
    labelx=[]
    x=[]
    y=[]
    cal = extractVersMethods()
    novelListS = makeMecabPattern()
    ans = cal.checkNovel(novelListS)
    for i in range(0,10):
        labelx.append(ans[i][0])
        x.append(i)
        y.append(ans[i][1])
    plt.bar(x,y,tick_label=labelx,align="center")
    plt.show()
    
