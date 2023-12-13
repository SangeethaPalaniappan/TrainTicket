import sys 
sys.path.append(r'C:\Users\sangee\TrainTicket')
import TrainTicket

class TicketCancel:
    def ticket_cancel():
        no_of_passengers  = int(input("No.  of passengers : "))

        for i in range(no_of_passengers):
            name              = input("Name       : ")    
            ticket_no         = input("Ticket No. : ")
         
            for details in TrainTicket.booked_details_arr:
                if TrainTicket.booked_details_arr[1] == ticket_no :
                    TrainTicket.booked_details_arr = 0

                    berth_type = TrainTicket.booked_details_arr[2]
                    