import smtplib
from colorama import Fore
from colorama import init
from termcolor import colored
from discord_webhook import DiscordWebhook, DiscordEmbed
from urllib.request import Request, urlopen


init()

print(colored('', 'green', 'on_red'))

print(Fore.RED + """

                                __ __                                                                               
                               /  /  |                                                                              
  ______  _____  ____   ______ $$/$$ |        _______  ______   ______  _____  ____  _____  ____   ______   ______  
 /      \/     \/    \ /      \/  $$ |       /       |/      \ /      \/     \/    \/     \/    \ /      \ /      \ 
/$$$$$$  $$$$$$ $$$$  |$$$$$$  $$ $$ |      /$$$$$$$//$$$$$$  |$$$$$$  $$$$$$ $$$$  $$$$$$ $$$$  /$$$$$$  /$$$$$$  |
$$    $$ $$ | $$ | $$ |/    $$ $$ $$ |      $$      \$$ |  $$ |/    $$ $$ | $$ | $$ $$ | $$ | $$ $$    $$ $$ |  $$/ 
$$$$$$$$/$$ | $$ | $$ /$$$$$$$ $$ $$ |       $$$$$$  $$ |__$$ /$$$$$$$ $$ | $$ | $$ $$ | $$ | $$ $$$$$$$$/$$ |      
$$       $$ | $$ | $$ $$    $$ $$ $$ |      /     $$/$$    $$/$$    $$ $$ | $$ | $$ $$ | $$ | $$ $$       $$ |      
 $$$$$$$/$$/  $$/  $$/ $$$$$$$/$$/$$/       $$$$$$$/ $$$$$$$/  $$$$$$$/$$/  $$/  $$/$$/  $$/  $$/ $$$$$$$/$$/       
                                                     $$ |                                                           
                                                     $$ |                                                           
                                                     $$/                                                            


""")


email_me = str(input(" enter your email: "))
email_pass = str(input(" enter your email password: "))
email_subject = str(input(" enter your email subject: "))
email_body = str(input(" enter your email body: "))
print('\n', '\n',
      'if you do not want to send to multiple emails just put the same email in each option DONT LEAVE IT BLANK THE '
      'CODE WONT WORK', '\n', '\n')
target_email = str(input(" enter target email 1 : "))
target_email2 = str(input(" enter target email 2 : "))
target_email3 = str(input(" enter target email 3 : "))
target_email4 = str(input(" enter target email 4 : "))
target_email5 = str(input(" enter target email 5 : "))
send_amount = int(input(" enter how many emails you want to send: "))
print("emails sent:")
index = 0

def email_spammer_lol():
    global index
    index += 1
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(str(email_me), str(email_pass))
        subject = str(email_subject)
        body = str(email_body)

        msg = f"subject: {subject}\n\n{body}"

        smtp.sendmail('gay@gmail.com', str(target_email), msg)
        smtp.sendmail('gay@gmail.com', str(target_email2), msg)
        smtp.sendmail('gay@gmail.com', str(target_email3), msg)
        smtp.sendmail('gay@gmail.com', str(target_email4), msg)
        smtp.sendmail('gay@gmail.com', str(target_email5), msg)
        print(str(index))


for x in range(0, int(send_amount)):
    email_spammer_lol()

