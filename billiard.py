import time
startTime = time.time()

N=10
targetSum = N*(N-1)+1       #要素の合計
sup = (targetSum-1)//2 +1   #要素の取りうる値の最大値
result = [0]*(N)
result[0] = 1

candidates = [0,tuple(range(2, sup+1))]     #要素の候補リスト

depth = 1             #現在参照しているresultのindex
candidatesIndex = [0,0]     #candidatesに含まれるtupleの何番目までを参照したかまとめたもの

print(N,"角形")

def SupCheck():
    global depth
    while depth >= 1 and (len(candidates[depth]) <= candidatesIndex[depth]+1):
        #tmpの中の数字が全部ダメだったらdepthを1下げる
        del candidatesIndex[depth]
        del candidates[depth]

        depth -= 1
        result[depth] = 0


while result[0] != 0:
    result[depth] = candidates[depth][candidatesIndex[depth]]
    tmpSet = set(candidates[depth])
    valid = True    #うまく行ってますか


    #新しい数字に対して和を取る
    #result = [1,a,b,c,0,0,0] なら、c → c+b → c+b+a → c+b+a+1 の順で検証
    partialSum = 0  #部分和
    for j in range(depth,-1,-1):
        partialSum += result[j]

        if min(partialSum,targetSum-partialSum) in tmpSet:  #partialSum,targetSum-partialSumのうち大きい方は、"大抵"supを超える。sup-1 と sup のみ例外(sup-1 + sup == targetSum)で、このときsup-1の方がtmpSumに含まれるかどうかの判定が行われる。よって最終的にはtmpSetにsupのみが残る。
            #被ってないとき
            tmpSet.remove(min(partialSum,targetSum-partialSum))
        else:
            #被り時
            valid = False
            break
    
    if not valid:
        result[depth] = 0
        SupCheck()
        candidatesIndex[depth] += 1
        continue

    if depth < N-2:
        #まだ最後まで埋まってないのでdepthを上げて次に行く
        if depth+1 == N//2 and 2 in tmpSet:
            candidates.append([2])
        else:
            candidates.append(tuple(tmpSet))
        candidatesIndex.append(0)
        depth += 1 
    else:
        #tmpSetから数字がなくなったらプリント
        result[-1] = targetSum-partialSum  #最後の数字はN-1個の要素の和をtargetSumから引けばよい
        print(result)

        result[-1] = 0         #最後の数字削除  
        result[depth] = 0
        SupCheck()
        candidatesIndex[depth] += 1


print("python  実行時間:", time.time() - startTime)