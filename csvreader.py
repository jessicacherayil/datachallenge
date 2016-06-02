'''Authors: Jasmine Jones, Jess Cherayil'''

import csv

def maxVotes(postfile):
    '''Task from workshop'''
    maxVal = 0
    maxProduct = ()
    with open(postfile,'rb') as csvfile:
        postreader = csv.reader(csvfile)
        firstline = True
        for row in postreader:
            if firstline:    #skip first line
                firstline = False
                continue
            if row[6] != ' ' and row[6] != '': 
                if int(row[6]) > maxVal:
                    maxVal = int(row[6])
                    maxProduct = (row[2],row[3])
                
    return maxProduct, maxVal

#####################################################################################################
    
def getPopularUsers(userfile):
    '''Given filename containing user IDs and their
    numbers of followers, calculate top 10000 most 
    popular users (i.e. the top 10000 users with 
    the most followers.) and the 10000 least popular users (i.e.
    the ones with the least followers) Returns two lists of user IDs'''

    userDict = {} #Format is user: followerCount
    with open(userfile,'rb') as csvfile:
        userReader = csv.reader(csvfile)
        firstline = True 
        for row in userReader:
            if firstline:    #skip first line
                firstline = False
                continue
                
            if row[7] != '' and row[7][0] != '_': #ignore null entries
                userDict[(row[0])] = int(row[7])
            
    allUsers = sorted(userDict, key=userDict.__getitem__, reverse = True) #sort by follower count
    print allUsers[0:25]
    #print len(allUsers)
    return allUsers[0:10000], allUsers[-10000:]

def getMostPopularWords(postfile):
    mostPop, leastPop = getPopularUsers('users--2016-04-01_14-36-26-UTC.csv')
    #print 'mostpop', mostPop

    popWords = {}
    leastPopWords = {}
    popTags = []
    leastPopTags = []

    with open(postfile,'rb') as csvfile:
        postReader = csv.reader(csvfile)
        firstline = True 
        for row in postReader:
            if firstline:    #skip first line
                firstline = False
                continue

            for user in mostPop:
                if row[0] == user:
                    popTags.append(row[3]) #append tagline of each pop user

            for user2 in leastPop:
                if row[0] == user2:
                    leastPopTags.append(row[3]) #append tagline of each least pop user

    for tag in popTags: 
        for word in tag.split():
            if word not in popWords: #populate pop word dictionary
                popWords[word]=1
            else:
                popWords[word] += 1

    for tag2 in leastPopTags:
        for word2 in tag2.split():
            if word2 not in leastPopTags: #populate least pop words dictionary
                leastPopWords[word2]=1
            else:
                leastPopWords[word2] += 1

    popular = sorted(popWords, key = popWords.__getitem__,reverse = True)
    notPopular = sorted(leastPopWords, key = leastPopWords.__getitem__,reverse = True)
    popular = popular[0:100] #get most popular words used for popular and not popular users
    notPopular  = notPopular[0:100]

    for word in popular:
        print popWords[word], word

    print '\n'

    for word in notPopular:
        print leastPopWords[word], word


    # print "WORDS USED BY POPULAR USERS", popular
    # print "\n"
    # print "WORDS USED BY UNPOPULAR USERS", notPopular
    return popular

def getNumPosts(popularUsers):
    
    userPosts = {}
    popularUsers = popularUsers[0:500]
    #print 'POPULAR USERS', popularUsers[0:25]


    with open('users--2016-04-01_14-36-26-UTC.csv','rb') as csvfile:
        postReader = csv.reader(csvfile)
        firstline = True 
        for row in postReader:
            if firstline:    #skip first line
                firstline = False
                continue
            for user in popularUsers:
                if row[0] == user:
                    userPosts[user] = int(row[10])

    l = []
    p = []
    for i in range(0,500):
        #l.append(popularUsers[i])
        p.append(userPosts[popularUsers[i]])
    #print "l",l
    print "p",p
   

    # with open('users--2016-04-01_14-36-26-UTC.csv','rb') as csvfile:
    #     users = ['179569', '72696', '16065', '92', '38308', '749', '15864', '10202', '115732', '93344', '120713', '89993', '13803', '20297', '158779', '123392', '176571', '2', '104430', '160187', '61997', '213030', '29570', '121503', '348647']
    #     result = []
    #     resultDict = {}
    #     postReader = csv.reader(csvfile)
    #     firstline = True 
    #     for row in postReader:
    #         if firstline:    #skip first line
    #             firstline = False
    #             continue

    #         for user in users:
    #             if row[0] == user:
    #                 resultDict[user] = int(row[10])
    #                 result.append(int(row[10]))

    # print 'POSTS',resultDict

    # print userPosts[popular[0]]
    # print userPosts[popular[50]]

    return userPosts #popular

def getNumVotes(popularUsers):
    userVotes = {}
    popularUsers = popularUsers[0:500]

    with open('users--2016-04-01_14-36-26-UTC.csv','rb') as csvfile:
        voteReader = csv.reader(csvfile)
        firstline = True 
        for row in voteReader:
            if firstline:    #skip first line
                firstline = False
                continue

            for user in popularUsers:
                if row[0] == user:
                    userVotes[user] = int(row[9])


    l = []
    p = []
    for i in range(0,500):
        #l.append(popularUsers[i])
        p.append(userVotes[popularUsers[i]])
    #print "l",l
    print "p",p

    # with open('users--2016-04-01_14-36-26-UTC.csv','rb') as csvfile:
    #     users = ['179569', '72696', '16065', '92', '38308', '749', '15864', '10202', '115732', '93344', '120713', '89993', '13803', '20297', '158779', '123392', '176571', '2', '104430', '160187', '61997', '213030', '29570', '121503', '348647']
    result = []
    #     resultDict = {}
    #     voteReader = csv.reader(csvfile)
    #     firstline = True 
    #     for row in voteReader:
    #         if firstline:    #skip first line
    #             firstline = False
    #             continue

    #         for user in users:
    #             if row[0] == user:
    #                 resultDict[user] = (int(row[9]))
    #                 result.append(int(row[9]))

    # print 'VOTES',resultDict

    # print userVotes[popular[0]]
    # print userVotes[popular[50]]

    return result #popular

    
            
def main():
    mostPop, leastPop = getPopularUsers('users--2016-04-01_14-36-26-UTC.csv')
    #getMostPopularWords('posts--2016-04-01_14-36-24-UTC.csv')
    getNumPosts(mostPop)
    #getNumVotes(mostPop)



if __name__=='__main__':
    main()
            
