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
    numbers of followers, calculate top 100 most 
    popular users (i.e. the top 100 users with 
    the most followers. Returns a list of user IDs'''

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

    return allUsers[0:10000]
    
def getMostPopularWords(postfile, popularUsers):
    wordFrequencies = {}
    tagList = []
    with open(postfile,'rb') as csvfile:
        postReader = csv.reader(csvfile)
        firstline = True 
        for row in postReader:
            if firstline:    #skip first line
                firstline = False
                continue

            for user in popularUsers:
                if row[0] == user:
                    tagList.append(row[3])

    for tag in tagList:
        for word in tag.split():
            if word not in wordFrequencies:
                wordFrequencies[word]=1
            else:
                wordFrequencies[word] += 1

    words = sorted(wordFrequencies, key = wordFrequencies.__getitem__,reverse = True)
    print 'top', wordFrequencies[words[0]]
    print words
    return wordFrequencies
    
            
def main():
    popularUsers = getPopularUsers('users--2016-04-01_14-36-26-UTC.csv')
    getMostPopularWords('posts--2016-04-01_14-36-24-UTC.csv', popularUsers)
    
if __name__=='__main__':
    main()
            
