##Programmer: Emma Davis
#Date Due: Nov. 16, 2016
#This program gets the user to input a keywords file and a tweets file. The program processes these files and
#outputs the happiness score and the number of tweets in each timezone.

#import the graphics file used in this code
import happy_histogram

#Function that opens a file
def openFile(fileName):
    inFile = open(fileName, "r")
    return inFile

#Function that closes a file
def closeFile (inFile):
    inFile.close()

#Function that strips the word that is given to it by taking out the numbers and punctuation and makes it lowercase
def strip(word):
    NUM = "1234567890"
    PUNC = ".;:'?!#@-"
    word = word.strip(PUNC)
    word = word.strip(NUM)
    word = word.lower()
    #returns the stripped word
    return word

#Function that returns the happiness value of the line of tweet that is sent in
def happinessValueTweet(tweet, keywords, happinessValueKeyWords):
    #variables for the happiness values of the keywords and the number of words that are keywords
    happiness = 0
    numWords = 0
    #goes through the list of the words in the tweet word by word
    for word in tweet:
        #if the word in the tweet is in the list of keywords
        if word in keywords:
            #finds the index position of the keyword in the keyword list
            positionKeyword = keywords.index(word)
            #if the word is the same word as the keyword in that position
            if word == keywords[positionKeyword]:
                #adds one to the number of words that are keywords
                numWords = numWords + 1
                ##adds the happiness value of the word that is the keyword using the position of the keyword to the
                #total happiness value of the tweet
                happiness = happiness + happinessValueKeyWords[positionKeyword]

    #if no words are in the happiness value then the happiness score is 0
    if numWords == 0:
        happinessScore = 0
    #otherwise the happiness score is the total happiness value divided by the number of words
    else:
        happinessScore = happiness/numWords
    #returns the happiness score
    return happinessScore

#Function that finds the location of the tweet
def location(lat, long, newTweet, keywords, happinessValueKeyWords):
    #if the tweet is within the latitude range of the timezones
    if lat > 24.660845 and lat < 49.189787:
        #find the happiness value of the tweet
        tweetHappinessValue = happinessValueTweet(newTweet, keywords, happinessValueKeyWords)

        ##if the tweet is in the different timezones then it creates the locationTweet list of the timezone
        #and the happiness value of the tweet
        if long < -67.444574 and long > -87.518395:
            locationTweet = ["eastern", tweetHappinessValue]

        elif long < -87.518395 and long > -101.998892:
            locationTweet = ["central", tweetHappinessValue]

        elif long <-101.998892 and long > -115.236328:
            locationTweet = ["mountain", tweetHappinessValue]

        elif long < -115.236328 and long > -125.242264:
            locationTweet = ["pacific", tweetHappinessValue]

        #if the tweet is not in a specified time zone
        else:
            locationTweet = [0,0]
    #if the tweet is not within any timezone
    else:
        locationTweet = [0,0]
    #returns the timezone and the happiness value of the tweet or two zeros if the tweet is not in any timezone
    return locationTweet

try:
    #prompts the user for input of the keywords file
    fileName = input("Enter the file containing the keywords: ")
    #sends the file to the openFile function
    keywordsFile = openFile(fileName)

    #declare the variables
    keywords = []
    happinessValue = []

    for line in keywordsFile:
        ##splits the line then adds the first part of the splitted line to the keywords list and the second part of the
        #splitted line to the happinessValue list
        list = line.split(",")
        #adds the keyword to the keyword list and makes the word lowercase
        keywords.append(list[0].lower())
        #adds the value of happiness to the happinessValue list and converts it into an integer
        happinessValue.append(int(list[1]))
    #sends the file to the close file function
    closeFile(keywordsFile)

    #prompts the user for the file contining the tweets
    fileName = input("Enter the file containing the tweets: ")
    #sends the file that the user inputed to the open file function
    tweetsFile = openFile(fileName)

    #declare the variables for the happiness score and the number of tweets in each timezone
    easternHappiness = 0
    easternTweets = 0

    centralHappiness = 0
    centralTweets = 0

    mountainHappiness = 0
    mountainTweets = 0

    pacificHappiness = 0
    pacificTweets = 0

    #goes through each line in the tweets file
    for line in tweetsFile:
        #seperates the line of the tweet into the latitude and longitude
        data = []
        data = line.split("]", 1)
        latlong = data[0].split(",")
        lat = float(latlong[0].strip("["))
        long = float(latlong[1].strip())

        #splits the tweet into each seperate word
        tweet = data[1]
        tweet = tweet.split()
        newTweet = []
        #sends the tweet to the strip function
        for word in tweet:
            word = strip(word)
            if word != "":
                newTweet.append(word)

        #sends the latitude and longitude of the tweet to the location function
        locationTweet = location(lat, long, newTweet, keywords, happinessValue)

        #if the tweet does have a happiness value
        if locationTweet[1] != 0:
            ##if the tweet is in the specified timezone then it adds the happiness value of the tweet to the happiness
            #value of the timezone and adds one to the number of tweets in that timezone
            if locationTweet[0] == "eastern":
                easternHappiness = easternHappiness + locationTweet[1]
                easternTweets = easternTweets + 1

            elif locationTweet[0] == "central":
                centralHappiness = centralHappiness + locationTweet[1]
                centralTweets = centralTweets + 1

            elif locationTweet[0] == "mountain":
                mountainHappiness = mountainHappiness + locationTweet[1]
                mountainTweets = mountainTweets + 1

            elif locationTweet[0] == "pacific":
                pacificHappiness = pacificHappiness + locationTweet[1]
                pacificTweets = pacificTweets + 1

    #close the tweets file
    closeFile(tweetsFile)

    #Displays empty lines and the happiness score in each time zone as well as the number of tweets in each time zone
    print()
    print("The happiness score in the Eastern timezone is:", round(easternHappiness/easternTweets, 2))
    print("The number of tweets in the Eastern timezone is:", easternTweets)

    print()
    print("The happiness score in the Central timezone is:", round(centralHappiness/centralTweets, 2))
    print("The number of tweets in the Central timezone is:", centralTweets)

    print()
    print("The happiness score in the Mountain timezone is:", round(mountainHappiness/mountainTweets, 2))
    print("The number of tweets in the Mountain timezone is:", mountainTweets)

    print()
    print("The happiness score in the Pacific timezone is:", round(pacificHappiness/pacificTweets, 2))
    print("The number of tweets in the Pacific timezone is:", pacificTweets)
    print()

    ##calls the function from the graphics file used in this program and sends the happiness value all the different
    #timezones to it
    happy_histogram.drawSimpleHistogram(easternHappiness/easternTweets, centralHappiness/centralTweets, mountainHappiness/mountainTweets,pacificHappiness/pacificTweets)

#excpet IOErrors and ValueErrors and display and error message
except IOError as exception:
    print("Error,", exception)
except ValueError as exception:
    print("Error,", exception)

