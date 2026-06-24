from logger import Logger
from filter import TransferFiles
from reminder import TimerOfThread
from checkNewFile import CheckNewFile


cnf = CheckNewFile() 
oldFile = cnf.CheckFile()
while True:
    value = input("Do you to transfer all while in categrized way: (y)")
    # root = input("Do you want to add the root directory")
    tf=None
    rem=None
    log= Logger()
    if(value.lower()=='y'):        
        tf= TransferFiles('.') 
        docsPrompt = input("Do you want to categorized the docs(y): ")
        if(docsPrompt.lower()=='y'):
            tf.CategorizeByDocs()
            print("The files are categorized")
            log.AdditionLog("The docs are categorized")
        imagePrompt = input("Do you want to categorized the images(y): ")
        if(imagePrompt.lower()=='y'):
            tf.CategorizeByImage()
            log.AdditionLog("The images are categorized")
    value2 = input("Do you want to add the reminder in your setting:  (y)")
    if(value2.lower() == 'y'):
        seconds = int(input("Enter the reminder of the timer: "))
        message = input("Enter the message for the timer")
        rem = TimerOfThread(seconds,message)
        rem.Start()
        log.AdditionLog(f"The reminder with message starts --{message}--")

        while True:
            value = input("The stop message (y/n): ")

            if value.lower() == "y":
                rem.Stop()
                print("Processing Stopped")
                log.AdditionLog(f"The reminder with message ends here --{message}--")
                break
    value3 = input("Do you want to check new files: (y)")
    if(value3.lower()=="y"):
        newFiles = cnf.CheckFile()
        if(len(newFiles)==0):print("Not new files")
        else:
            print(f"New Files add:  {newFiles}")
                
    
    choice = input(
        "Do you want to exit or restart? (e/r): "
    )

    if choice.lower() == 'r':
        continue
    else:
        break
    

    
        
        
        


