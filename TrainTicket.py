import sys
sys.path.append(r'C:\Users\sangee\TrainTicket')
import BerthTypes 

class TrainTicket:
    booked_details_arr = []
    write_in_file = open("BookedTicketDetails.txt")
    for details in write_in_file:
        if details != '0\n':
            booked_details_arr.append(details.split(","))
    write_in_file.close()    

    def __init__(self, name, age, gender):
        self.name              = name
        self.age               = age
        self.gender            = gender
        self.berth_obj = BerthTypes.Berth()
        
        
    def ticket_booking(self):
        berth_preference  = self.berth_type()
        getting_ticket, berth_type = self.berth_obj.assign_ticket(berth_preference)
        if getting_ticket != None and berth_type != "WL" and berth_type != "RAC":

            write_in_file = open("BookedTicketDetails.txt", 'a')
            write_in_file.write(self.name + "," + str(getting_ticket) + "," + berth_type + "," + "CNF" + ",")
            write_in_file.write("\n")    
            write_in_file.close()
            print("Ticket Booked")

        elif berth_type == "WL":
            count = int(self.berth_obj.tickets_dict["waiting_list"])
            number = 10 - count
            ticket_no = getting_ticket + "-" + str(number)
            write_in_file = open("WaitingListTicketDetails.txt", 'a')
            write_in_file.write(self.name + "," + berth_type + "," + ticket_no + "," + ",")
            write_in_file.write("\n")    
            write_in_file.close()
            print("Waiting List")


        elif berth_type == "RAC":
            
            count = int(self.berth_obj.tickets_dict["rac_berths"])
            number = 18 - count
            ticket_no = getting_ticket + "-" + str(number)
            write_in_file = open("RACTicketDetails.txt", 'a')
            write_in_file.write(self.name + "," + berth_type + "," + ticket_no + "," + ",")
            write_in_file.write("\n")    
            write_in_file.close()
            print("RAC")
            
        else:
            print(berth_type)
            return 

           
        
    @classmethod
    def ticket_cancel(cls):
        no_of_passengers  = int(input("No.  of passengers : "))
        berth_obj = BerthTypes.Berth()
        for i in range(no_of_passengers):
            name              = input("Name       : ")    
            coach             = input("Enter coach : ")
            ticket_no         = input("Ticket No. : ")
            ticket            = coach + "-" + ticket_no
            status            = input("Ticket Status (CNF/RAC/WL) : ") 
            for details in range(len(cls.booked_details_arr)):
                if cls.booked_details_arr[details][1] == ticket:
                    if cls.booked_details_arr[details][0] == name:
                        berth_type = cls.booked_details_arr[details][2]
                        

                        cancel = berth_obj.ticket_cancellation(berth_type, ticket, status)
                        if cancel != None:
                            cls.booked_details_arr.remove(cls.booked_details_arr[details])
                            print(name, "Your ticket has been cancelled")
                            if cancel != 1:
                                cls.booked_details_arr.append(cancel)
                            write_in_file = open("BookedTicketDetails.txt", 'w')
                            for i in range(len(cls.booked_details_arr)):
                                write_in_file.write(cls.booked_details_arr[i][0] + "," + cls.booked_details_arr[i][1] + "," + cls.booked_details_arr[i][2] + "," )
                                write_in_file.write("\n")
                            write_in_file.close()  
                            seat_file = open("AvailableSeats.txt", "w")  
                            for seats in berth_obj.seat_arr:
                                seat_file.write(seats[0] + "," )
                                seat_file.write("\n") 
            
                            seat_file.close() 
                            break
                    else:
                        print("Enter Correct Name")    
                        continue
            
            for details in range(len(berth_obj.rac_arr)):
                if berth_obj.rac_arr[details][2] == ticket:
                    if berth_obj.rac_arr[details][0] == name:
                        berth_type = berth_obj.rac_arr[details][2]

                        cancel = berth_obj.ticket_cancellation(berth_type, ticket, status)
                        if cancel != None:
                            
                            berth_obj.rac_arr.remove(berth_obj.rac_arr[details])

                            print(name, "Your ticket has been cancelled")
                            if cancel != 1:
                                berth_obj.rac_arr.append(cancel)
                                # berth_obj.rac_arr.append(cancel)
                            rac_file = open("RACTicketDetails.txt", "w")
                            i = 1
                            for details in berth_obj.rac_arr:
                                rac_file.write(details[0] + "," + "RAC" + "," + "R-" + str(i) + "," + ",") # RAC counts
                                rac_file.write("\n")    
                                i += 1
                            rac_file.close()

                            wl_file = open("WaitingListTicketDetails.txt", "w")
                            i = 1
                            for details in berth_obj.wl_arr:
                                wl_file.write(details[0] + "," + details[1] + "," + "WL-" + str(i) + "," + ",") # RAC counts
                                wl_file.write("\n")    
                                i += 1
                            wl_file.close()
                            
                            seat_file = open("AvailableSeats.txt", "w")  
                            for seats in berth_obj.seat_arr:
                                seat_file.write(seats[0] + "," )
                                seat_file.write("\n") 
            
                            seat_file.close() 
                            break      

                    else:
                        print("Enter correct Name") 
                        continue   


            for details in range(len(berth_obj.wl_arr)):
                if berth_obj.wl_arr[details][2] == ticket:
                    if berth_obj.wl_arr[details][0] == name:
                        berth_type = berth_obj.wl_arr[details][2]

                        cancel = berth_obj.ticket_cancellation(berth_type, ticket, status)
                        if cancel != None:
                            
                            berth_obj.wl_arr.remove(berth_obj.wl_arr[details])

                            print(name, "Your ticket has been cancelled")
                            if cancel != 1:
                                berth_obj.wl_arr.append(cancel)
                                # berth_obj.wl_arr.append(cancel)
                            wl_file = open("WaitingListTicketDetails.txt", "w")
                            i = 1
                            for details in berth_obj.wl_arr:
                                wl_file.write(details[0] + "," + details[1] + "," + "WL-" + str(i) + "," + ",") # RAC counts
                                wl_file.write("\n")    
                                i += 1
                            wl_file.close()

                            seat_file = open("AvailableSeats.txt", "w")  
                            for seats in berth_obj.seat_arr:
                                seat_file.write(seats[0] + "," )
                                seat_file.write("\n") 
            
                            seat_file.close() 
                            break      

                    else:
                        print("Enter correct Name") 
                        continue   

    @classmethod        
    def booked_ticket_details(cls):
        write_in_file = open("BookedTicketDetails.txt")
        i = 0
        for details in write_in_file:
            cls.booked_details_arr.append(details.split(","))
            print(cls.booked_details_arr[i][0] + "\t\t" + cls.booked_details_arr[i][1] + "\t\t" + cls.booked_details_arr[i][2])
            i += 1
        write_in_file.close()

        berth = BerthTypes.Berth()
        rac = berth.rac_arr

        for ticket in rac:
            ticket_no = berth.seat_arr.pop()
            berth.berth_type_dict["side_lower_rac"] -= 1
            print(ticket[0], "\t",  ticket_no[0], "\t", "side_lower_rac")

        
        file_1 = open("BerthTypeDetails.txt", "w")
        for i in range(len(berth.berth_type_det)):
            file_1.write(berth.berth_type_det[i][0] + "," + str(berth.berth_type_dict[berth.berth_type_det[i][0]]) + ",")
            file_1.write("\n")
        file_1.close()
        


    def available_ticket_details():   

        berth_obj = BerthTypes.Berth()
        arr = berth_obj.arr
        if int(arr[0][1]) == 0 and int(arr[1][1]) > 0:
            print("RAC_AVL\t", int(arr[1][1]))
        elif int(arr[0][1]) > 0:
            print("AVL\t", int(arr[0][1]))    
        elif int(arr[2][1]) > 0:
            print("WL\t", int(arr[2][1]))
        else:
            print("REGRET")    

    def berth_type(self):
        print(" 1. Upper\n", "2. Middle\n", "3. Lower\n", "4. Side Upper\n", "5. Side Lower")
        option = int(input("Select anyone of the options : "))
        if self.age > 60:
            option = 3
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
                TrainTicket.ticket_cancel()
            elif option == 3:
                TrainTicket.booked_ticket_details()

            elif option == 4:
                TrainTicket.available_ticket_details()    

        else:
            break    

options()            