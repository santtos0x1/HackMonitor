import os
import json
from typing import List

def Collector(listOfNews: List[str]) -> None:
    try:
        storagePath: str = "../HackMonitor/storage/local_storage.json"
        if not os.path.exists(storagePath) or os.path.getsize(storagePath) == 0:
            with open(storagePath, "w") as file:
                json.dump({"sent_news": []}, file, indent=4)
                
        with open(storagePath, "r") as file:
            localStorage: dict = json.load(file)
            
        for link in listOfNews:
            if link not in localStorage["sent_news"] and link.startswith("https://"):
                localStorage["sent_news"].append(link)
                with open(storagePath, "w") as file:
                    json.dump(localStorage, file, indent=4)
                    
    except Exception as e:
        error_msg: str = f"Error in Collector: {e}"
        print(error_msg)
