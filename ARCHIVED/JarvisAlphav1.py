import speech_recognition as sr
import time
import datetime
import SendKeys
from BeautifulSoup import BeautifulSoup
import urllib2
import os
import pyttsx
import sys
# Load voice engine settings
engine = pyttsx.init()
# rate for how fast the voice speaks
engine.setProperty('rate', 167)
voices = engine.getProperty('voices')

# Welcome message for user
welcomeMsg = "Welcome Sir"
engine.say(welcomeMsg)
engine.runAndWait()
# only outer scoped variable
request = ""
Alarmset = False
alarmtime = []

#Functions for things
def Googling(i):
    import os
    #base google results url
    google_URL = "https://www.google.ca/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q="

    # Replace all text implementations
    i = i.replace("jarvis ", "")
    i = i.replace("google ", "")
    i = i.replace(" please", "")
    i = i.replace(" for me", "")
    # speech
    engine.say("searching for " + i)
    engine.runAndWait()
    # replace spaces with %20 for google search
    i = i.replace(" ", "%20")
    # Concatenation of string
    google_URL = 'start chrome "%s%s"' % (google_URL, i)
    # open Chrome
    os.system(google_URL)
    for x in range(3):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("--")
            audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        request = r.recognize_google(audio)
        # Fetch the problem problem to give the proper output
        try:
            print("Google Request: " + request)
        except sr.UnknownValueError:
            print("No Audio Detected")
        except sr.RequestError as e:
            print("Internal Error")
        if "open first link" in str(request):
            SendKeys.SendKeys('{DOWN}')
            SendKeys.SendKeys('{ENTER}')
        elif "open second link" in str(request):
            for x in range(2):
                SendKeys.SendKeys('{DOWN}')
            SendKeys.SendKeys('{ENTER}')
        elif "open third link" in str(request):
            for x in range(3):
                SendKeys.SendKeys('{DOWN}')
            SendKeys.SendKeys('{ENTER}')
        elif "open fourth link" in str(request):
            for x in range(4):
                SendKeys.SendKeys('{DOWN}')
            SendKeys.SendKeys('{ENTER}')
        elif "open fifth link" in str(request):
            for x in range(5):
                SendKeys.SendKeys('{DOWN}')
            SendKeys.SendKeys('{ENTER}')
        elif "open sixth link" in str(request):
            for x in range(6):
                SendKeys.SendKeys('{DOWN}')
            SendKeys.SendKeys('{ENTER}')

def machineTime():
    import time
    #Time (localtime off machine)
    dt = list(time.localtime())
    hourtime = dt[3]
    minutetime = dt[4]
    #Calculate AM/PM plus hours and minutes
    if hourtime > 12:
        hourtime -= 12
        timeOfDay = "PM"
    else:
        timeOfDay = "AM"
    if minutetime < 10:
        minute1 = 0
    else:
        minute1 = ""
    time = str(hourtime) + ":" + str(minute1) + str(minutetime) + str(timeOfDay)
    return(time)

def AlarmClock(request):

    global alarmtime
    datetype = "am"
    if "p.m." in str(request):
        datetype = "pm"
    request = request.replace("jarvis","")
    request = request.replace("set an alarm ", "")
    request = request.replace("set alarm ", "")
    request = request.replace("for", "")
    request = request.replace(" ", "")
    request = request.replace("p.m.", "")
    request = request.replace("a.m.", "")
    alarmtime = request.split(":")
    alarmtime.append("am")
    if datetype == "pm":
        alarmtime[2] = "pm"


def AlarmChecker():
    if Alarmset == True:
        dt = list(time.localtime())
        hour = dt[3]
        minute = dt[4]
        #Calculate AM/PM plus hours and minutes
        if hour > 12:
             hour -= 12
             timeOfDay = "pm"
        else:
             timeOfDay = "am"
        # if minute < 10:
        #      minute1 = 0
        # else:
        #      minute1 = ""
        #AlarmClock(request)
        Tsetfor = (str(alarmtime[0])+str(alarmtime[1])+str(alarmtime[2]))
        Tactually = (str(hour)+ str(minute)+ str(timeOfDay))
        if Tactually == Tsetfor:
            wakeUp = "Time to wake up Sir, it is " + machineTime()
            engine.say(wakeUp)
            engine.runAndWait()
            weather()
            AlarmSet = False

def openexes(i):
    if "open wow" in str(i) or "open world or warcraft" in str(i):
        engine.say("Opening World of Warcraft")
        engine.runAndWait()
        # Open WoW
        os.system('C:\Program Files (x86)\World of Warcraft')

    elif "open mine craft" in str(i) or "open minecraft" in str(i):
        engine.say("Opening minecraft")
        engine.runAndWait()
        # open Minecraft
        os.system('"C:/Users/benvc/Desktop/Minecraft.exe"')

    elif "open steam" in str(i):
        engine.say("Opening Steam")
        engine.runAndWait()
        # open Steam
        os.system('"C:/Users/benvc/Desktop/Steam.exe"')
    else:

        # Replace all text implementations and obsurities
        i = i.replace("jarvis ", "")
        i = i.replace("open", "")
        i = i.replace("please", "")
        i = i.replace("dot", ".")
        i = i.replace(" ", "")
        # Get engine to speak
        engine.say("Opening " + request)
        engine.runAndWait()
        # format the website URL with the chrome starter
        SiteURL = 'start chrome "%s"' % request
        # actually open it
        os.system(SiteURL)

def jarvisIdle(i):
    # Remove the text leaving time and h/m/s
    i = i.replace("jarvis", "")
    # Speech
    engine.say(i)
    engine.runAndWait()
    i = i.replace("idle", "")
    i = i.replace("for", "")
    i = i.replace(" ", "")
    # If statements
    if "hour" in str(i) or "hours" in str(i):
        i = i.replace("hour","")
        i = i.replace("s","")
        i = float(i) * 60 * 60
        time.sleep(float(i))

    elif "minute" in str(request) or "minutes" in str(i):
        i = i.replace("minute","")
        i = i.replace("s","")
        i = float(i) * 60
        time.sleep(float(i))

    elif "second" in str(request) or "seconds" in str(i):
        i = i.replace("second","")
        i = i.replace("s","")
        time.sleep(float(i))

def writeNote(i):
    # Remove Jarvis and commands
    i = i.replace("jarvis", "")
    i = i.replace("make a note", "")
    i = i.replace("make note", "")
    i = i.replace("write a note", "")
    i = i.replace("take note", "")
    ts = time.time()
    date1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    f = open("C://Users/benvc/Desktop/JarvisNotes.txt", "a")
    f.write(str(date1) + ": " + i + "\n")
    f.close()
    # Speech
    engine.say("Note Written")
    engine.runAndWait()
    #print("Note Written")
#TODO
def closeExe(i):
    i = i.replace("jarvis", "")
    i = i.replace("close", "")
    i = i.replace(" ", "")

    engine.say("closing " + i)
    if i == "chrome":
        os.system('taskkill /im chrome.exe')
    engine.runAndWait()
    taskkill = "'taskkill /im %s.exe'" % i
    os.system('%s') % taskkill

def closeNotes():
    f = open("C://Users/benvc/Desktop/JarvisNotes.txt", "w")
    f.write("")
    f.close()
    # Speech
    engine.say("Notes Cleared")
    engine.runAndWait()

def jarvisType(i):
    # Remove the question and replace spaces
    i = i[12:]
    i = i.replace(" ", "{SPACE}")
    # Send keystrokes through
    SendKeys.SendKeys(str(i))

def weather():
    #site URL
    url = 'https://weather.gc.ca/city/pages/ns-19_metric_e.html'
    #Open page as HTML
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    #Strip everything but the words
    condition = soup.find("dl", {"class": "col-sm-6 dl-horizontal wxo-dl mrgn-bttm-0"}).contents
    condition = str(condition)
    condition = condition.replace("n'", " ")
    condition = condition.replace("u'", " ")
    condition = condition.replace(" \ ", " ")
    condition = condition.replace("<dt>Condition:</dt>", " ")
    condition = condition.replace("<dd>","")
    condition = condition.replace('class="mrgn-bttm-0',"")
    condition = condition.replace('[ , <dt>Condition:</dt>,  , <dd class="mrgn-bttm-0">', " ")
    condition = condition.replace('<dt>Pressure:</dt>,  , <dd class="mrgn-bttm-0 wxo-metric-hide">101.2&nbsp;<abbr title="kilopascals">kPa</abbr>', "")
    condition = condition.replace('</dd>,  , <dd class="mrgn-bttm-0 wxo-imperial-hide wxo-city-hidden">29.9&nbsp;inches</dd>,  , <dt>Tendency:</dt>,  , <dd class="mrgn-bttm-0">falling</dd>,  , <dt>Visibility:</dt>,  , <dd class="mrgn-bttm-0 wxo-metric-hide">24 <abbr title="kilometres">km</abbr>', "")
    condition = condition.replace('</dd>,  , <dd class="mrgn-bttm-0 wxo-imperial-hide wxo-city-hidden">15 miles</dd>,  ]', " ")
    condition = condition.replace("<dd>", "")
    condition = condition.replace("</dd>","")
    condition = condition.replace('<dt>Pressure:</dt>',"")
    condition = condition.replace(",","")
    condition = condition.replace('<dd class="mrgn-bttm-0 wxo-metric-hide">101.0&nbsp;<abbr title="kilopascals">kPa</abbr>',"")
    condition = condition.replace('<dd class="mrgn-bttm-0 wxo-imperial-hide wxo-city-hidden">29.8&nbsp;inches   <dt>Tendency:</dt>   <dd class="mrgn-bttm-0">falling   <dt>Visibility:</dt>   <dd class="mrgn-bttm-0 wxo-metric-hide">24 <abbr title="kilometres">km</abbr>',"")
    condition = condition.replace('class',"")
    condition = condition[:20]
    condition = condition.replace('<dd class="mrgn-bttm-0', "")
    condition = condition.replace('wxo-metric-hide',"")
    condition = condition.replace('"',"")
    condition = condition.replace('<dd',"")
    condition = condition.replace('dd',"")
    condition = condition.replace('>',"")
    for x in range(10):
        condition = condition.replace(' '," ")
    temp = soup.find("span", {"class": "wxo-metric-hide"}).contents
    tempString = str(temp)
    tempString = tempString.replace("[u'", "")
    #tempString = tempString.replace("-", "")
    tempString = tempString.replace("&deg;', <abbr title=", " Degrees ")
    tempString = tempString.replace(">C</abbr>, u'", " ")
    tempString = tempString.replace('"', "" )
    tempString = tempString.replace("n']", " " )
    tempString = tempString.replace(" \ ", "")
    #Print statement
    Weather = ("The weather is " + condition + "and " + tempString)
    engine.say(Weather)
    engine.runAndWait()
    print(Weather)

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

# Loop until I quit the program
for x in range(10000000):
    while request != "jarvis shut down":
        if request == "jarvis shut down":
            os.quit()
        # Reset request at beginning of loop
        request = ""
        # Try to pick up microphone audio, if it doesn't it fails
        try:
                # recognize speech using Google Speech Recognition
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("..")
                    audio = r.listen(source)
                # recognize speech using Google Speech Recognition
                request = r.recognize_google(audio)

                # Fetch the problem problem to give the proper output
                try:
                    print("Accepted Speech: " + request)
                except sr.UnknownValueError:
                    print("No Audio Detected")
                except sr.RequestError as e:
                    print("Internal Error")

                # Make the request in lower
                request = request.lower()

                # If to see if Jarvis is said
                if "jarvis" in str(request) or "service" in str(request) or "travis" in str(request):
                    # Commands in If statements Woot woot
                    if "make a note" in str(request) or "make note" in str(request) or "write a note" in str(request) or "take note" in str(request):
                        writeNote(request)

                    # Weather right now
                    elif "weather right now" in str(request) or "what's the weather like" in str(request) or "how is the weather" in str(request):
                        weather()


                    # Idle Jarvis for a time amount
                    elif "idle for" in str(request):
                        jarvisIdle(request)

                    # Clear the notepad file
                    elif "clear my notes" in str(request) or "clear notes" in str(request) or "clear my nose" in str(request):
                        closeNotes()

                    # Make Jarvis Tab
                    elif "jarvis tab" in str(request):
                        #Tab using Sendkeys
                        SendKeys.SendKeys("%{TAB}")

                    # Chrome switch tab
                    elif "switch tab" in str(request):
                        #Tab using Sendkeys
                        SendKeys.SendKeys("^{TAB}")

                    # Google search
                    elif "search this" in str(request) or "jarvis google" in str(request) or "jarvis look up" in str(request):
                        Googling(request)

                    # Get Jarvis to type things out
                    elif "type" in str(request):
                        jarvisType(request)

                    # Second command for Jarvis typing
                    elif "say" in str(request):
                        jarvisType(request)

                    # Open anything
                    elif "open" in str(request):
                        openexes(request)

                    elif "jarvis close" in str(request):
                        print("close")
                        closeExe(request)

                    # set alarm
                    elif "set alarm" in str(request)or "set an alarm" in str(request):
                        Alarmset = True
                        AlarmClock(request)
                        engine.say("Alarm is set")
                        engine.runAndWait()

                    elif "turn off alarm" in str(request):
                        Alarmset = False
                    # time
                    elif "what time is it?" in str(request):
                        engine.say("It is " + str(machineTime()) + " sir")
                        engine.runAndWait()

                    elif "restart 202" in str(request):
                        restart()

                    # print process time
                    elif "current process time" in str(request):
                        runtime = time.clock()
                        engine.say(str(runtime.format(2)) + " seconds of run time.")
                        engine.runAndWait()

                    else:
                        print("Nothing Triggered")
                        if Alarmset == True:
                            AlarmChecker()
                else:
                    print("Nothing")
                    if Alarmset == True:
                        AlarmChecker()
        except:
            if Alarmset == True:
                AlarmChecker()
            print(str(time.clock()) + " seconds of run time.")
			
			
			
			

