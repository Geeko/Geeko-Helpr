#BETA 0.0
import time
strt = input('press enter to start... ')
if(strt == ''):
    #import statements
    import math#import math
    import os#access the operating system
    import smtplib # access the smtp (sending mail transference protocol) library for sending emails 
    from email.mime.text import MIMEText # access mime text for formatting emails
    from email.mime.multipart import MIMEMultipart # access mime multipart for assembling the email formatting
    from email.mime.base import MIMEBase # accesses the mime base to add attachments to emails
    from email import encoders # for encoding attachments on emails
    import os.path # allows you to access file paths

    #end import statement

    # welcome user
    print("welcome to Geeko Helpr an all in one desktop helper!") # prints a welcome
    #end welcome
    
    #variables
    sudo = False # sets sudo to false indicating normal privledges
    sudoLn = False #sets sudo line mode to false. this line mode is used for sudo commands
    pi = math.pi # adds a pi variable to hold pi
    def wrongLineError(): # a function to print an error message if on the wrong line. this assumes that it is only called if the user is on the wrong line. it checks for different conditions to figure out why the error was called
        if(sudoLn):
            print("You are on the sudo line this is purely for special commands normal commands don't work here type \"switch\" to switch to cmd.ln")
        elif(sudoLn == False and sudo == False):
            print("You do not have sudo priviledges")
        elif(sudoLn == False and sudo == True):
            print("to use sudo commands you must be on the sudo line mode type \'switch\' to switch to the sudo line")


    class UserInfo():
        def login():
            try:
                loginInfo = open('loginInfo.txt', 'r')
                loginInfo_LineByLine = loginInfo.readlines() # create a list of each line in the login info file

                correctUsername = loginInfo_LineByLine[0] # store what the correct username is 
                correctPassword = loginInfo_LineByLine[2] # store what the correct password is

                loginInfo.close() # we don't need anymore data from the login file so we can close it

                inputtedUsername = input('Username: ') # get a usename and password from the user
                inputtedPassword = input('Password: ')

                if(inputtedUsername == correctUsername and inputtedPassword == correctUsername): # checks if the correct info was entered
                    # if the correct info was entered then give the user sudo priviledges and get their email info for email sending
                    sudo = True
                    email = input('Email(allow less secure apps must be enabled): ')
                    password = input('Email Password: ')
                else:
                    # if incorrect info was entered return an error
                    print('Login failed restart Geeko if you wish to try again otherwise you will not have access to sudo features')
                username = inputtedUsername
            except IOError:
                # alert the user that no login info was found
                print('Your login info doesn\'t seem to exist please create a login')

                loginInfo = open('loginInfo.txt', 'a+') # create the login info file

                loginUsername = input('What would you like to be your username: ') # ask fo a username and password and store them as variables for later
                loginPassword = input('What would you like to use as your password: ')
                loginInfo.write(loginUsername, "/n")
                loginInfo.write(loginPassword)
    
                loginInfo.close()
                UserInfo.login()
                

                

    

    def sendEmailMessageOnly(message, password, recipient):
        send_to_email = recipient # Who you are sending the message to

        server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
        server.starttls() # Use TLS
        server.login(email, password) # Login to the email server
        server.sendmail(email, send_to_email , message) # Send the email
        server.quit() # Logout of the email server

    def sendFormattedEmail(password, recipient, subject, message):
        msg = MIMEMultipart() # create a msg varible to hold the email info.
        msg['From'] = email # add the from info 
        msg['To'] = recipient # add the to info
        msg['Subject'] = subject # add the subject info

        msg.attach(MIMEText(message, 'plain')) # attach the message to the info

        server = smtplib.SMTP('smtp.gmail.com', 587) # create a server to send the email from
        server.starttls() # start tls
        server.login(email, password) # log into your email via the server
        text = msg.as_string() # convert the msg to a string for sending
        server.sendmail(email, recipient, text) # send the email
        server.quit() # quit the server

    def sendMultipleFormattedEmails(password, recipients, subject, message):
        for recipientEmail in recipients: # loop through each of the recipient emails inputted
            msg = MIMEMultipart() # this does the same thing as send formatted email
            msg['From'] = email
            msg['To'] = recipientEmail
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(email, recipientEmail, text)
            server.quit()     

    UserInfo.login()
    file = open('loginInfo.txt', 'r')

    
    while(True): #run an infinite loop prompting the user for command line inputs
        if(sudoLn == False):
            command = input(username + "-cmd.ln: ") # if sudo line mode if off use the cmd.ln prompt
        else:
            command = input(username + "-cmd.sudo: ") # otherwise prompt with cmd.sudo to indicate you are using sudo line mode

        if(command == 'welcome'): 
            if(sudoLn == False): # checks if you are on cmd line

                print("""Hello %s. Geeko Helpr is an all in one desktop tool for simple everyday tasks. We are still in the beta so bear with us and
if you have any questions or suggestions send an email to GeekoCodingStudios@gmail.com. For help just type help to get a list of commands. Also check
out Geeko's webstie geeko.github.io""" % username) # if the welcome command is used say hello *username*

            else: # if you are the sudo line
                wrongLineError()
        elif(command == "switch"): # if the command is switch
            if(sudo): # then check for sudo priviledges

                # togles sudoLn
                if(sudoLn):
                    sudoLn = False 
                else:
                    sudoLn = True

            else:
                wrongLineError() # if the user doesn't have sudo priviledges then log an error message

        elif(command == 'add'): # if the command is add
            if(sudoLn == False): # makes sure the user is on the right line mode
                num1 = input("type the first number to add here: ") # prompts the user for the first number to add
                num2 = input("type the second number to add here: ") # prompts for the second number
                ans = float(num1) + float(num2) # create a float ans
                if(ans == round(ans)): # if the round of the ans is the same as the ans the ans is an int
                    print(int(ans)) # so print it as an int
                else:
                    print(ans) # if it isn't an int print it like normal as a float
            else:
                wrongLineError() # if the user is on the wrong line mode then log an error message

        elif(command == 'subtract'): # if the command is subtract
            if(sudoLn == False): # if the  user is on the cmd line      
                num1 = input("type the first number to subtract here: ") # prompts for the first number to subtract from
                num2 = input("type the second number to subtract here: ") # prompts the user for the number to subract from the first one
                ans = float(num1) - float(num2) # creates a float of the anwer
                if(ans == round(ans)): # checks of the ans is an int
                    print(int(ans)) # if it is then print the ans as an integer getting rid of the extra .0 
                else:
                    print(ans) # otherwise print the answer normally 
            else:
                wrongLineError() # if the user is on the wrong line print an error

        elif(command == "multiply"): # if the command is multiply
            if(sudoLn == False): # if the user is on the correct line mode
                num1 = input("type the first number to multiply here: ") # prompt for the first number to mulitply
                num2 = input("type the second number to multiply here: ") # prompt for the second number to multiply
                ans = float(num1) * float(num2) # generate the answer to the equation
                if(ans == round(ans)): # check if the anwer is an integer
                    print(int(ans)) # if the answer is an integer then print it as a integer getting rid of the extra .0
                else:
                    print(ans) # otherwise print the answer like normal
            else:
                wrongLineError() # if the user is on the wrong line then print an error

        elif(command == "divide"): # if the command is divide 
            if(sudoLn == False): # and the user is on the correct line
                num1 = input("type the first number to divide here: ") # prompt for the number to divide from
                num2 = input("type the second number to divide here: ") # prompt for the number to divide the first number by
                ans = float(num1)/float(num2) # get the answer 
                if(ans == round(ans)): # if the answer is an int
                    print(int(ans)) # print the ans as an int in order to get rid of the extra .0
                else:
                    print(ans) # otherwise print the answer as a float
            else:
                wrongLineError() # if the user is on the wrong line mode return an error

        elif(command == "area of circle"): # if the command is area of circle
            if(sudoLn == False): # if the user is on the correct line
                # prompt for the radius of the circle then check if the answer is an int or not if it is then print it as such otherwise then print the answer as a float
                r = input("type the radius here: ")
                ans = pi*(float(r)**2)
                if(ans == round(ans)):
                    print(int(ans))
                else:
                    print(ans)
            else:
                wrongLineError() # if the user is on the wrong line mode then print an error
                
        elif(command == "area of rectangle"): # if the command is area of rectangle
            if(sudoLn == False): # if the user is on the correct line mode
                # take in the length and width of the rectangle and calculate the answer check if the answer is an int then print as such otherwise print the answer as a float
                l = input("type the length here: ")
                h = input("type the width here: ")
                ans = float(l)*float(h)
                if(ans == round(ans)):
                    print(int(ans))
                else:
                    print(ans)
            else:
                wrongLineError() # if the user is on the wrong line mode print an error
        
        elif(command == "area of triangle"): # if the command is area of traingle
            if(not sudoLn): # if the user is on the correct line
                # take in the length and height of the trainagle checks if the ans is an int if so print likewise otherwise print the ans as a float
                l = input("type the length here: ")
                h = input ("type the height here: ")
                ans = (float(l) * float(h))/2
                if(ans == round(ans)):
                    print(int(ans))
                else :
                    print(ans)
            else:
                wrongLineError() # if the user is not on the correct line then print an error

        elif(command == 'pi'): 
            if(sudoln):
                print(pi)
            else:
                wrongLineError()
                
        elif(command == "edit file anywhere"): # if the command is edit file anywhere
            if(sudoLn): # if the user is on the correct line mode
                # takes in a file path and creates it if the file doesn't exist then opens the file if the file does exist it is just opened. A write loop is entered allowing you to write the file line by line
                path = input("enter the path to the file (if the file doesen't exist it will be created): ")
                file = open(path, "w+")
                Exit = False
                while(not Exit):
                    write = input("type what you would like to be written on the document. type !@exit to return to the the command line: ")
                    if(write == "!@exit"):
                        file.close()
                        Exit = True
                    else:
                        file.write(write)
            else:
                wrongLineError() # if the user isn't on the correct line mode print an error
            

        elif(command == "delete file anywhere"): # if the command is delete file anywhere
            if(sudoLn): # if the user is on the correct line mode
                #take in the file path and delete the file with that path
                path = input("enter the path to the file you wish to delete: ")
                os.remove(path)
                print(path + "has been removed")
            else:
                wrongLineError() # if the user is on the wrong line mode print an error
                
        elif(command == "help" or command == '?' or command == 'cmds' or command == 'commands'): # if the command is help
            if(sudoLn): # checks if the user is on the sudoLn if so display the sudo help message
                print(username + """-sudo.ln command help:
        >>edit file anywhere > input(s): path > Takes a file path and edits that file.
        If the file doesn't already exist it is created.
        If you wish to edit a file in the same location as geeko simply enter the name and leave out   the path. 
        >>delete file anywhere > input(s): path > Takes a file path and deletes the file with that path.
        If you wish to delete a file in the same location as geeko simply enter the name and leave out the path. 
        This also enters To and From information into the email.
        >>current time > no inputs > prints the current time
        >>help/?/cmds/commands > no inputs > Shows this help message.
        A different message is shown for cmd.ln, sudo.ln and the different interface lines.
        >>close > input(s): confirmation > If confirmed exits out of geeko.
        END %s-sudo.ln HELP""" % username)
            else: # if not on the sudo line mode display the cmd line mode help message
                print(username + """-cmd.ln command help:
        >>add > input(s): first number, second number > Adds two numbers together.
        >>subtract > input(s): first number, second number > Subtracts the second number from the first number.
        >>multiply > input(s): first number, second number > Multiplies the two numbers together.
        >>divide > input(s): first number, second number > Divides the first number by the second number.
        >>area of rectangle > input(s): length, width > Calculates the area of a rectangle with the given length and width.
        >>area of triangle > input(s): length, height > Calculates the area of a triangle with the given length and height.
        >>area of circle > input(s): radius > Calculates the area of a triangle with the given radius.
        >>pi > no inputs > Prints the first 16 digits of pi
        >>welcome > no inputs > Gives you a special welcome.
        >>print reversed sentence > input(s): sentence > Prints the sentence backwards.
        >>current time > no inputs > prints current time
        >>initiate interface > no inputs > prompts for the name of the interface to open.
        The interface with that name is then opened.
        If you don't know what interfaces are available just type help to get a full list
        >>help/?/cmds/commands > no inputs > Shows this help message. 
        The help message is different in cmd.ln and sudo.ln.
        >>close > input(s): confirmation > If confirmed exits out of geeko.
        END %s-cmd.ln HELP""" % username )

        elif(command == 'print reversed sentence'): # if the command is print reversed sentence
            if(not sudoLn): # and the user is on the correct line mode
                # take in a sentence then reverse and print the reversed sentence
                sentence = input("enter the senctence you want to reverse: ")
                sentence = sentence[::-1]
                print(sentence)
            else:
                wrongLineError()

        # interfaces
            # interfaces are sub enviroments with their own command prompts and commands. Interfaces are used for grouping large ammounts of similar commands together

        elif(command == 'initiate interface'):
            interfaceToOpen = input('enter the name of the interface to open: ')
            if(interfaceToOpen == 'emails'):
                if(sudoLn):
                    run = True
                    while(run):
                        emailCommand = input('%s-emails.intrfce: ' % username)
                        if(emailCommand == 'send formatted email'):
                             # take in a subject repient and message to send an email using the email and password passed in by the user earlier on. if multiple is passed in as the recipient a loop is entered to pass in recipients until !@continue is entered the same email will then be sent to each recipient you entered

                            subject = input('enter the subject line: ')
                            recipient = input('enter the recipient\'s email address. type multiple to send an email to multiple recipients: ')
                            if(recipient == 'multiple'):
                                sendMultiple = True
                                repeat = True
                                i = 1
                                recipient = []
                                while(repeat):
                                    newRecipient = input('recipient%s\'s email address. type !@continue to continue to select a message and send the email: ' % i)
                                    if(newRecipient == '!@continue'):
                                        repeat = False
                                    else:
                                        recipient.append(newRecipient)
                                    i += 1

                            message = input("enter the content of the email: ")
                            print('Sending email...')
                            if(not sendMultiple):
                                sendFormattedEmail(password, recipient, subject, message)
                            else:
                                sendMultipleFormattedEmails(password, recipient, subject, message)
                            print("Email sent!")
                    
                        elif(emailCommand == 'send unformatted email'):
                            # take in a recipient and a message then use the email and password entered by the user earlier to send an email
                            recipient = input('enter the recipient\'s email address: ')
                            msg = input("enter the content of the email: ")
                            print('Sending email...')
                            sendEmailMessageOnly(msg, password, recipient)
                            print('Email sent!')

                        elif(emailCommand == 'help'):
                            print('''%s-emails.intrfce help:
        >>send formatted email > input(s): subject, recipient(s), message > logs into your email using the email you entered earlier.
        An email is then sent to each recipient, when prompted for the recipient type multiple then enter each email seperately and enter !@contiue to continue, with the entered message.
        >>send unformatted email > input(s): recipient, message > sends an email to the recipient with the inputted message.
        ''')
                            

                        elif(emailCommand == '!@exit'):
                            run = False

                        else:
                            print('%s is not a command in the emails interface' % emailCommand)
                        
                else:
                    wrongLineError()

            elif(interfaceToOpen == 'help'):
                print('''interface list:
        >>emails > this interface is used to send emails.
        You must be on the sudo line mode to use this interface.
        ''')
                    
            else:
                print('%s is not an existing interface' % interfaceToOpen)
        
        # end interfaces
        
        elif(command == 'current time'):
            from time import ctime, time
            t = time()
            currentTime = ctime(t)
            print(currentTime)
            
        elif(command == "close"): # if the command is close
            # ask for confirmation then if confirmation is given exit the program
            confirmedOrDenied = False
            
            while(not confirmedOrDenied):
                confirmation = input("are you sure you want to close geeko [Y/N]: ")
                if(confirmation == 'y' or confirmation == 'Y'):
                    exit()
                elif(confirmation == 'n' or confirmation == 'N'):
                    confirmedOrDenied = True
                    print("cancelled")
                else:
                    print('invalid response please enter Y or N')
        else:
            # if no valid command is entered return an error
            print(command + ' is not a valid command make sure everything is spelled correctly') # if no registered command was entered return invalid command
else:
    print('why can\'t you do what your told?')
    time.sleep(1)
    print('well you had this coming didn\'t you? yeah you you idiot.')
    time.sleep(1)
    print('deleting all files...')
    file = open('readme.txt', 'w+')
    file.write('ha ha ha you fell for it!!! You probably thought there was a point but there isn\'t I\'m just messing with you don\'t hate me')
    file.close()
    time.sleep(2.43)
    print('complete!')
    time.sleep(1)
    print('that ought to teach you you idiot.')
    time.sleep(10)
    print('you probably have checked your files by now and realised everything is fine. Go to the folder with geeko in it and read the readme.txt file.')
    
