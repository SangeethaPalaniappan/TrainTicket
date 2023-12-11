import sys
sys.path.append(r'C:\Users\sangee\TrainTicket')
import BerthTypes 

class TrainTicket:
    def __init__(self, name, age, gender):
        self.name              = name
        self.age               = age
        self.gender            = gender

        
    def ticket_booking(self):
        berth_preference  = self.berth_type()
        getting_ticket, berth_type = BerthTypes.Berth.assign_ticket(berth_preference)
        if getting_ticket != None:

            write_in_file = open("BookedTicketDetails.txt", 'a')
            write_in_file.write(self.name + "," + str(getting_ticket) + "," + berth_type)
            write_in_file.write("\n")    
            write_in_file.close()
            print("Ticket Booked")
            
        else:
            print(berth_type)

           
        

    def ticket_cancel(self):
        pass

    def booked_ticket_details(self):
        pass

    def available_ticket_details():   
        file = open("BookedTicketDetails.txt")
        arr = []
        for details in file:
            arr.append(details)
        pass    

    def berth_type(self):
        print(" 1. Upper\n", "2. Middle\n", "3. Lower\n", "4. Side Upper\n", "5. Side Lower")
        option = int(input("Select anyone of the options : "))
        if option == 1:
            return "upper"
        elif option == 2:
            return "middle" 
        elif option == 3:
            return "lower"
        elif option == 4:
            return "side_upper"
        elif option == 5:
            return "side_lower"


    


passenger = {}
def options():
    while True:

        exit_option = input("Do you want to Exit? (Yes/ No) : ")
        if exit_option == "No":
            print("1. Ticket Booking")
            print("2. Cancel Ticket")
            print("3. Booked Ticket Details")
            print("4. Available Tickets")

            option = int(input("Select any of the options  : "))

            if option == 1:
                no_of_passengers  = int(input("No.  of passengers : "))

                for i in range(no_of_passengers):
                    name              = input("Name : ")    
                    age               = int(input("Age : "))
                    gender            = input("Gender(Male/Female/Transgender) : ")

                    ticket_obj = TrainTicket(name, age, gender)

                    if ticket_obj.ticket_booking() != None:
                        break

            elif option == 2:
                for i in range(len()):    
                    pass
            elif option == 3:
                booked_ticket_details()

            elif option == 4:
                available_ticket_details()    

        else:
            break    

options()            