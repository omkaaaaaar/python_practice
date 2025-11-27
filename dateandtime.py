from datetime import datetime

def show_date() -> None:   #-> None: means the function does not return any value, it only shows the output it does not return anything to the function caller
    print("Current time:")
    print(datetime.now())

show_date()
show_date()
