import praw
import requests
import urllib.request
import os
import time
import prawredsettings as settings

startpro = time.time()


# Enter your app details below
reddit = praw.Reddit(client_id=settings.clientid,
                     client_secret=settings.secret,
                     user_agent=settings.agent)

#Enter Username
user_name = str(input("User Name: "))
submissions = reddit.redditor(user_name).submissions.new(limit=None)
comments = reddit.redditor(user_name).comments.new(limit=None)

def wipeUserFile(user_name):
    start = time.time()
    if not os.path.exists("users/"):
        os.mkdir("users/")
    userfile = open("users/{} Reddit Data.txt".format(user_name),"w", encoding='utf-8')
    userfile.close()
    print("It took {0:0.1f} seconds to wipe {1}'s file".format(time.time() - start, user_name))
    return

def writeUserFile(user_name,self_texts):
    start = time.time()
    if not os.path.exists("users/"):
        os.mkdir("users/")
    userfile = open("users/{} Reddit Data.txt".format(user_name),"a", encoding='utf-8')
    userfile.write(str(self_texts))
    print("It took {0:0.1f} seconds to write to {1}'s file".format(time.time() - start, user_name))
    return

###Todo Finish
def getUserPosts(user_name):
    start = time.time()
    self_texts = []
    postnum = 0
    self_texts.append("----Posts----\n")
    for link in submissions:
        # listcontent = (link.title,"\n",link.selftext,"\n","Post Score: ",str(link.score),"\n","--------------------------------------------------------------------\n")
        self_texts.append(link.title)
        self_texts.append("\n")
        self_texts.append("Subreddit: ")
        self_texts.append(str(link.subreddit))
        self_texts.append("\n")
        self_texts.append(link.url)
        self_texts.append("\n")
        self_texts.append(link.selftext)
        self_texts.append("\n")
        self_texts.append("Post Score: ")
        self_texts.append(str(link.score))
        self_texts.append("\n")
        self_texts.append("Comments: ")
        self_texts.append(str(link.num_comments))
        self_texts.append("\n")
        self_texts.append("--------------------------------------------------------------------\n")
        postnum += 1
        os.system("cls")
        print("Current Post Number: ",str(postnum))
        print("{0:0.1f} Seconds".format(time.time() - start))
        # self_texts.append(str(listcontent))
    print('It took {0:0.1f} seconds to complete posts. The user has {1} posts'.format(time.time() - start, postnum))
    posttime = time.time() - start 
    return self_texts,posttime

def getUserComments(user_name):
    start = time.time()
    self_texts = []
    f = ""
    g = ""
    commentnum = 0
    self_texts.append("----Comments----\n")
    for link in comments:
        # listcontent = ("Comment Post Name: ",link.submission.title,"\n",link.body,"\n","Comment Score: ",str(link.score),"\n", "--------------------------------------------------------------------\n") Using this breaks everything
        self_texts.append("Comment Post Name: ")
        self_texts.append(link.submission.title)
        self_texts.append("\n")
        self_texts.append("Subreddit: ")
        self_texts.append(str(link.submission.subreddit))
        self_texts.append("\n")
        self_texts.append(str(link.submission.url))
        self_texts.append("\n")
        self_texts.append(link.body)
        self_texts.append("\n")
        self_texts.append("Post Score: ")
        self_texts.append(str(link.score))
        self_texts.append("\n")
        self_texts.append("--------------------------------------------------------------------\n")
        # self_texts.append(str(listcontent))
        commentnum += 1
        os.system("cls")
        print("Current Comment Number: ",str(commentnum))
        print("{0:0.1f} Seconds".format(time.time() - start))
        
    wipeUserFile(user_name)
    commenttime = time.time() - start
    poststuff = getUserPosts(user_name)
    print('It took {0:0.1f} seconds to complete comments. The user has {1} comments'.format(commenttime, commentnum))
    posttime = poststuff[1]
    writeUserFile(user_name,g.join(poststuff[0]))
    writeUserFile(user_name,f.join(self_texts))
    return    

getUserComments(user_name)

print('It took {0:0.1f} seconds for the full program'.format(time.time() - startpro))
