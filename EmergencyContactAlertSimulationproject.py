import time
from datetime import datetime

# Enter your emergency contact numbers here manually and pre save
cntcts = {
    "Father": "8374567363",
    "Mother": "7346929283",
    "Brother": "8346596343",
    "Sister": "9385698477",
    "Best Friend": "6546678994"
}


lgBk = []  

def list_cntcts():
    print("\nContact list")  
    print()
    if not cntcts:  
        print("No contacts found")
    else:
        for k, v in cntcts.items():
            print(f"- {k} : {v}")
            
            
    print("\n")

def nwCntct():
    n = input("Name: ").strip()  
    p = input("Phone number: ").strip()
    
    if n and p:  
        cntcts[n] = p
        print(f"[+] Saved {n} to contacts.\n")
    else:
        print("Error: Name or number missing\n")
    

def dlCntct():
    trgt = input("Who do you want to remove? ").strip()
    
    if cntcts.pop(trgt, None):
        print(f"[-] Removed {trgt}.")
    else:
        print("Error: Person not found in list.")
    print()

def view_logs():
    print("\n=== RECENT ACTIVITY ===")
    if len(lgBk) == 0:  
        print("Log is empty.")
    else:
        
        recent = lgBk[-3:]  
        for entry in recent:
            print(entry)
    print("=======================\n")

def trigger_alert():
    print("\nSELECT ALERT TYPE:")
    optns = {
        "1": "Emergency, I'm lost, please help",
        "2": "Current city is Bhopal",
        "3": "Medically I'm not feeling well.",
        "4": "I'm okay.",
        "5": "injured, help.",
        "6": "Custom message:"
    }
    

    for k, v in optns.items():
        
        dspTxt = v if k != "6" else "Write your own.."
        print(f"{k}. {dspTxt}")

    sel = input("Selection: ").strip()  
    
    msgCntnt = ""
    
    
    if sel in ["1", "2", "3", "4", "5"]:
        msgCntnt = optns[sel]
    elif sel == "6":
        msgCntnt = input("Type message: ").strip()
        if not msgCntnt:  
            print("Message can't be empty")
            return
    else:
        print("Invalid selection, stoping...")
        return  

    usrNm = input("Sender name: ").strip()
    if not usrNm:  
        usrNm = "Unknown"
    
    tStmp = datetime.now().strftime("%H:%M:%S") 

    print("\nInitiating alert sequence...")
    time.sleep(0.5) 
    
    sent_count = 0
    for name in cntcts:
        print(f"Sending to {name}..")
        time.sleep(0.2) 
        sent_count += 1
    
    print(f"\nDone! Sent to {sent_count} people")
    
    lgEntry = f"[{tStmp}] {usrNm}: {msgCntnt}"
    lgBk.append(lgEntry)
    

    print(f"""
    Report:
    From: {usrNm}
    Msg: "{msgCntnt}"
    Time: {tStmp}
    
    """)

def app_loop():
    r = True  

    while r:
        print("======= EMERGENCY CONTACT STIMULATOR v1.0 ======")
        print("1. My Contacts")
        print("2. Add New")
        print("3. Delete Contact")
        print("4. TRIGGER ALERT")
        print("5. History")
        print("6. Quit")
        
        try:
            cmd = input(": ").strip()
        except KeyboardInterrupt:
            print("\n\nExiting...")
            r = False

        if cmd == "1": 
            list_cntcts()
        elif cmd == "2": 
            nwCntct()
        elif cmd == "3": 
            dlCntct()
        elif cmd == "4": 
            trigger_alert()
        elif cmd == "5": 
            view_logs()
        elif cmd == "6": 
            print("Exiting system...")
            r = False
            
        else:
            print("Unknown command")


if __name__ == "__main__":
    app_loop()
