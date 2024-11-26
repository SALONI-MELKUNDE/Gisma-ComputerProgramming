from datetime import datetime

def print_current_date_and_time():
    
    now = datetime.now()
    
    current_date = now.strftime("%Y-%m-%d")  
    print(f"Current Date: {current_date}")
    
    current_time = now.strftime("%H:%M:%S")  
    print(f"Current Time: {current_time}")


print_current_date_and_time()
