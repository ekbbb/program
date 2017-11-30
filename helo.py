import threading
import commands
check = commands.getoutput("./post1.sh hosoyaikemen")
def hello():

 print check

t=threading.Timer(600,hello)
t.start()
