content_array = []
def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line)

file_read('20ng-sports.txt')
# print(len(content_array))
import math
# scikit-learn k-fold cross-validation
from numpy import array
from sklearn.model_selection import KFold
# data sample
data = array(range(0,1993))
# prepare cross validation
kfold = KFold(5, True)
# enumerate splits
baseball_article=0
hockey_article=0
p_good=0
for train, test in kfold.split(data):
    # print('train: %s, test: %s' % (data[train], data[test]))
    baseball_article=0 ## stores no of baseball article
    hockey_article=0  ## stores no of hockey article
    distinct = {}    ## stores no of distinct words##
    for lineno in data[train]:
        sentence = content_array[lineno].split()
        dis_in_sent=[]
        for word in sentence:
            if distinct.get(word)==None:
                if word!="rec.sport.hockey" and word!="rec.sport.baseball":
                    distinct.update({word:[0, 0]})
                    if sentence[0]=="rec.sport.baseball":
                        distinct[word][0]=1
                    else:
                        distinct[word][1]=1
            elif word!="rec.sport.hockey" and word!="rec.sport.baseball":
                if word not in dis_in_sent:
                    if sentence[0]=="rec.sport.baseball":
                        distinct[word][0]=distinct[word][0]+1
                    else:
                        distinct[word][1]=distinct[word][1]+1
            dis_in_sent.append(word)

        
        if sentence[0]=="rec.sport.baseball":
            baseball_article=baseball_article+1
        else:
            hockey_article=hockey_article+1

    ##conversion in probability##
    for word in distinct:
        distinct[word][0]=distinct[word][0]/baseball_article
        distinct[word][1]=distinct[word][1]/hockey_article    
    # print(len(distinct))
    ##testing##
    p1=1  ##Probability of P(X/Y=0)
    p2=1  ##Probability of P(X/Y=1)
    ph=hockey_article/(hockey_article+baseball_article)
    pb=baseball_article/(hockey_article+baseball_article)
    p_right=0
    count=0
    for lineno in data[test]:
        p1=0
        p2=0
        sentence = content_array[lineno].split()
        for word in sentence:
            if word in distinct:
                if distinct[word][0]!=0:
                    p1=p1+math.log(distinct[word][0])
                else:
                    p1=p1+math.log(1/(baseball_article+len(sentence)))
                # print(p1)
                if distinct[word][1]!=0:
                    p2=p2+math.log(distinct[word][1])
                else:
                    p2=p2+math.log(1/(hockey_article+len(sentence)))
            else:
                p1=p1+math.log(1/(baseball_article+len(sentence)))
                p2=p2+math.log(1/(hockey_article+len(sentence)))
        # print(p1)
        # p_x = p1*pb + p2*ph
        p_b = p1 + math.log(pb)
        p_h = p2 + math.log(ph)
        if p_b>p_h :
            if sentence[0]=="rec.sport.baseball":
                p_right=p_right+1
        else:
            if sentence[0]=="rec.sport.hockey":
                p_right=p_right+1
        count=count+1
    print(p_right/count)
    p_good=p_good+ p_right/count

print("average probability over 5 sets of k folding is: "+ str(p_good/5))