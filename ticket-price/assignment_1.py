from datetime import datetime

# get the current day
today = datetime.now().strftime("%A")

# message which will be shown
message = "Ticket Price is ${}";

# take the age of user
age = input("Enter Your Age: ");
age = int(age)

ticketPrice=12;

# for children set the ticketPrice
if age < 18:
    ticketPrice = 8;
    
# offer user dicount if the day is special  
if today =='Thursday':
    print("Congrats! we are offering you a $2 offer")
    ticketPrice -=2

# finally show message

print(message.format(ticketPrice))
