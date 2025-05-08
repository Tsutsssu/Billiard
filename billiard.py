import time
startTime = time.time()

N=9
targetSum = N*(N-1)+1                   #要素の合計
sup = (targetSum-1)//2                  #要素の取りうる値の最大値
result = [0]*(N)
result[0] = 1

candidates = [0,tuple(range(2, sup+1))]     #要素の候補リスト

resultIndex = 1         #現在参照しているresultのindex
candidatesIndex = [0,0]       #candidatesに含まれるtupleの何番目までを参照したかまとめたもの

print(N,"角形")

def SupCheck():
    global resultIndex
    while resultIndex >= 1 and (len(candidates[resultIndex]) <= candidatesIndex[resultIndex]+1):
        #tmpの中の数字が全部ダメだったらresultIndexを1下げる
        del candidatesIndex[resultIndex]
        del candidates[resultIndex]

        resultIndex -= 1
        result[resultIndex] = 0

while result[0] != 0:
    result[resultIndex] = candidates[resultIndex][candidatesIndex[resultIndex]]
    tmpSet = set(candidates[resultIndex])
    valid = True    #うまく行ってますか


    #新しい数字に対して和を取る
    #result = [1,a,b,c,0,0,0] なら、c → c+b → c+b+a → c+b+a+1 の順で検証
    partialSum = 0  #部分和
    for j in range(resultIndex,-1,-1):
        partialSum += result[j]

        if min(partialSum,targetSum-partialSum) in tmpSet:       #partialSum,targetSum-partialSumのうち大きい方はsupを超えるので、tmpSetに含まれているはずがない
            #被ってないとき
            tmpSet.remove(min(partialSum,targetSum-partialSum))
        else:
            #被り時
            valid = False
            break
    
    if not valid:
        result[resultIndex] = 0
        SupCheck()
        candidatesIndex[resultIndex] += 1
        continue

    if resultIndex < N-2:
        #まだ最後まで埋まってないのでresultIndexを上げて次に行く
        candidates.append(tuple(tmpSet))
        candidatesIndex.append(0)
        resultIndex += 1 
    else:
        #tmpSetから数字がなくなったらプリント
        result[-1] = targetSum-partialSum  #最後の数字はN-1個の要素の和をtargetSumから引けばよい
        print(result)

        result[-1] = 0         #最後の数字削除  
        result[resultIndex] = 0
        SupCheck()
        candidatesIndex[resultIndex] += 1


print("実行時間 :", time.time() - startTime)