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
    #print len(allUsers)
    return allUsers[0:10000], allUsers[-10000:]

def getMostPopularWords(postfile):
    mostPop, leastPop = getPopularUsers('users--2016-04-01_14-36-26-UTC.csv')

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

    print "POPWORDS", popular
    print "\n"
    print "LEAST", notPopular
    return popular

def getNumPosts(popularUsers):
    
    userPosts = {}

    with open('users--2016-04-01_14-36-26-UTC.csv','rb') as csvfile:
        postReader = csv.reader(csvfile)
        firstline = True 
        for row in postReader:
            if firstline:    #skip first line
                firstline = False
                continue
            for user in popularUsers:
                if row[0] == user:
                    userPosts[user] = row[10]

    popular = sorted(userPosts, key = userPosts.__getitem__, reverse = True)
    popular = popular[0:100]

    print userPosts[popular[0]]
    print userPosts[popular[50]]

    return popular

def getNumVotes(popularUsers):
    userVotes = {}

    with open('users--2016-04-01_14-36-26-UTC.csv','rb') as csvfile:
        voteReader = csv.reader(csvfile)
        firstline = True 
        for row in voteReader:
            if firstline:    #skip first line
                firstline = False
                continue
            for user in popularUsers:
                if row[0] == user:
                    userPosts[user] = row[9]

    popular = sorted(userPosts, key = userPosts.__getitem__, reverse = True)
    popular = popular[0:100]

    print userVotes[popular[0]]
    print userVotes[popular[50]]

    return popular

    
            
def main():
    mostPop, leastPop = getPopularUsers('users--2016-04-01_14-36-26-UTC.csv')
    #getMostPopularWords('posts--2016-04-01_14-36-24-UTC.csv')
    #print getNumPosts(mostPop)
    print getNumVotes(mostPop)



if __name__=='__main__':
    main()
            
