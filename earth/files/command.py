"""
cd C:\mypro\python\python\command -dos

python command.py

# command -dos programm _ writen in 03032020
"""

#import
import sys
print("\n\n\n")
#안내문
print("Welcome to 'COMMAND WORLD'!\nIf you are first in here or need some help, press '/help' in command-dos.\nAnd if you want to stop and quit, press '/exit' in dos for stop this program.\n","=" * 50)


#미리설정해논 설정값들
slash = '/'
z = 0 #chat이 몇번째인지 확인하기 위해서..

user_name = input("what is your NAME? This blanket will be your USER_NAME.\nThis will be deleted when you exit this program...\n")
user_name = str(user_name)
fucklist = ['fuck', 'fuckyou', 'fucking', 'shit', 'ass', 'dick', 'fuckyou', 'fucku', 'fucking damn', 'damn', 'sex', 'sexy', 'fucking sex']
if user_name in fucklist:
    print("you can't use this name < ", user_name," >, your name is not allowed by this system...\nUse another name\n")
    user_name = input("what is your NAME? This blanket will be your USER_NAME.\nThis will be deleted when you exit this program...\n")
    user_name = str(user_name)
    if user_name in fucklist:
        print("=" * 50)
        print("HI, COWARD.")
        command = input('-' * 50 + "\nCOMMAND -DOS>>> ")
        if command in fucklist:
            print("WE HATE COWARD! JUST GO AWAY!")
            sys.exit()
            #욕쟁이퇴출
        else:
            print("-" * 50)
            print("ERROR_^AJ8@2$@  >  I think your windows has some accidents. Just use program like 'V3'and check you computer.")
            sys.exit()
else:
    #욕설이 포함된 이름은 안받으려고 했다가 걍 하기로함,,,
    print("=" * 50)
    print("HI,", user_name + ".")
    #user_name받는곳


#set the command list
command_list = ["/exit", "/help", "/command_lists", "/cl", "/developer", "/dev", "/user", "/mail", "/clear",
"/why", "/who", "/where", "/when", "/how", "/what", "egg"]


# 무한루프 + 캐먼드 제어
while True:
    command = input('-' * 50 + "\nCOMMAND -DOS>>> ") #도스창 계속 나오게 하는 문법
    command = str(command)

    if command in fucklist:
        print("WATCH YOUR MOUTH. do not use these words. we hate them.")

        
    #command - if_line
    elif command in command_list:
        if command == command_list[0]:
            sys.exit()
        elif command == command_list[1]:
            print("'/help' note:> \npress '/command_lists' or '/cl' to see commands, press '/developer' or '/dev' for see developer's details, and about this app.\nThis is help :)")
        elif command == command_list[2] or command == command_list[3]:
            print("""'/command_lists' note:>  
            
/exit  :  for exit this app
/help  :  if you need help
/command_lists or /cl  :  to see commands
/developer of /dev  : to see about this app or developer
/user  :  to set user_data just like user's name
/mail  :  it will give u a email adress about developer!!!
/clear  :  it will clear you dos-lines! it always clean your dos, but this can clean up your room too! oh i'm sorry it was joke :)
/why  :  why about dev
/who  :  who about dev
/where  :  where about dev
/when  :  when about dev
/how  :  how about dev
/what  :  what about dev
/egg  :  Just ester_egg. NOONE know what is that...
/question  :  about yout questions about this app and me! just for fun


""")
        elif command == command_list[7]:
            print("developer's email:> oscar050309@gmail.com\njust give me mail anything and anytime :)\nThank you very much for using this program\npress enter...")
        elif command == command_list[8]:
            print("\n" * 1000)



    elif command[0] == slash:
        print("There is no command < " + command + " > in command_list...")
        #이거 된다. 신기함
    else: #여기서 else이면 그냥 chat인 걸로 인식해야하므로 먼저 user_name을 받는다.
        z = z + 1
        chat = command
        chat = str(chat)
        z = str(z)
        user_name_z = "CHAT_ " + user_name + " - " + z
        user_name_z = str(user_name_z)
        print("-" * 50)
        print(user_name_z, " : " + chat)
        z = int(z)
        #chat data 저장, 메모장 열기
        #chat_data를 저장하려는데 잘안됨..