class Berth:
    def __init__(self):
        self.tickets_dict = {}
        self.arr = []
        file = open("AvailableTicketDetails.txt")
        i = 0
        for tickets in file:
            self.arr.append(tickets.split(","))    
            self.tickets_dict[self.arr[i][0]] = int(self.arr[i][1])
            i += 1  
        file.close()

        self.berth_type_dict = {}
        self.berth_type_det = []
        file_1 = open("BerthTypeDetails.txt")
        i = 0
        for tickets in file_1:
            self.berth_type_det.append(tickets.split(","))    
            self.berth_type_dict[self.berth_type_det[i][0]] = int(self.berth_type_det[i][1])
            i += 1  
        file_1.close()
  

        self.seat_arr = []
        seat_file = open("AvailableSeats.txt")  
        for seats in seat_file:
            self.seat_arr.append(seats.split(",")) 
        seat_file.close()    

        self.wl_arr = []
        wl_file = open("WaitingListTicketDetails.txt")
        for details in wl_file:
            self.wl_arr.append(details.split(","))
        wl_file.close()

        self.rac_arr = []
        rac_file = open("RACTicketDetails.txt")
        for details in rac_file:
            self.rac_arr.append(details.split(","))
        rac_file.close()


    def assign_ticket(self, berth_preference): 
        possibility = 0
        for berths in self.tickets_dict:
            if self.tickets_dict[berths] > 0:
                if berths == "rac_berths":
                    self.tickets_dict[berths] -= 1
                    del self.seat_arr[0]
                    seat_file = open("AvailableSeats.txt", "w")  
                    for seats in self.seat_arr:
                        seat_file.write(seats[0] + "," )
                        seat_file.write("\n") 
                    seat_file.close()    
                    
                    return "R", "RAC"


                elif berths == "waiting_list":
                    self.tickets_dict[berths] -= 1
                    del self.seat_arr[0]
                    seat_file = open("AvailableSeats.txt", "w")  
                    for seats in self.seat_arr:
                        seat_file.write(seats[0] + "," )
                        seat_file.write("\n") 
                    seat_file.close()    
                    
                    return "WL", "WL"
                else:    
                    berth_type = self.check_berth_availability(berth_preference)  
                    self.tickets_dict[berths] -= 1 
                    
                possibility = 1 
                
                seat_no = self.seat_allotment()
                break
        if possibility == 0:
            return None, "Currently No Tickets available"
        return seat_no, berth_type
    
    
    def override_ticket_details(self): 
        write_in_file = open("BerthTypeDetails.txt", 'w')
        for i in range(len(self.berth_type_det)):
            write_in_file.write(self.berth_type_det[i][0] + "," + str(self.berth_type_dict[self.berth_type_det[i][0]]) + ",")
            write_in_file.write("\n")    
        write_in_file.close()
        file_1 = open("AvailableTicketDetails.txt", "w")  
        for i in range(len(self.arr)):
            file_1.write(self.arr[i][0] + "," + str(self.tickets_dict[self.arr[i][0]]) + ",")
            file_1.write("\n") 
    
        file_1.close()

    
    def seat_allotment(self):
        seat_no = self.seat_arr[0][0]
        seat_file = open("AvailableSeats.txt", "w") 
        i = 0 
        for seats in self.seat_arr:
            if i == 0:
                i = 1
            else:    
                seat_file.write(seats[0] + "," )
                seat_file.write("\n") 
    
        seat_file.close()
        return seat_no
    
    
    def check_berth_availability(self, berth_preference):
        if self.berth_type_dict[berth_preference] > 0 :
                self.berth_type_dict[berth_preference] -= 1
                type = berth_preference

        else:
            for type in self.berth_type_dict :
                if type != berth_preference and type != "side_lower_rac":
                    self.berth_type_dict[type] -= 1 
                    break
        return type        
        
    def ticket_cancellation(self, berth_type, ticket_no, status):

        if self.tickets_dict["total_normal_berth"] != 0 and status == "CNF":
            self.seat_arr.insert(0, [ticket_no , "\n"])
            self.berth_type_dict[berth_type] += 1
            self.tickets_dict["total_normal_berth"] += 1
            
            
            return 1
        elif self.tickets_dict["rac_berths"] != 0: 
            if status == "RAC":
            
                self.tickets_dict["rac_berths"] += 1
                self.seat_arr.insert(0, 'R') 
                
                return 1


            elif status == "CNF":
                first_in_rac = self.rac_arr[0]
                first_in_rac[1], first_in_rac[2], first_in_rac[3] = ticket_no, berth_type, "CNF"
                del self.rac_arr[0]
                rac_file = open("RACTicketDetails.txt", "w")
                i = 1
                for details in self.rac_arr:
                    rac_file.write(details[0] + "," + details[1] + "," + str(i) + "," + ",")
                    rac_file.write("\n")
                    i += 1
                rac_file.close()
                self.tickets_dict["rac_berths"] += 1
                
                return first_in_rac

        else:
            if status == "WL":
                self.tickets_dict["waiting_list"] += 1
                self.seat_arr.insert(0, 'WL') 
                

                
                return 1

            elif status == "RAC":
                first_in_wl = self.wl_arr[0]
                first_in_wl[1], first_in_wl[2], first_in_wl[3] = ticket_no, "RAC", ""
                del self.wl_arr[0]
                self.seat_arr.append(["WL", "\n"])
                
                self.tickets_dict["waiting_list"] += 1

                
                return first_in_wl

            elif status == "CNF":
                first_in_rac = self.rac_arr[0]
                first_in_rac[1], first_in_rac[2], first_in_rac[3] = ticket_no, berth_type, "CNF"
                del self.rac_arr[0]
        
                
                first_in_wl = self.wl_arr[0]
                first_in_wl[1], first_in_wl[2], first_in_wl[3] = ticket_no, "RAC", ""
                del self.wl_arr[0]
                self.rac_arr.append(first_in_wl)

                rac_file = open("RACTicketDetails.txt", "w")
                i = 1
                for details in self.rac_arr:
                    rac_file.write(details[0] + "," + "RAC" + "," + "R-" + str(i) + "," + ",")
                    rac_file.write("\n")
                    i += 1
                rac_file.close()

                wl_file = open("WaitingListTicketDetails.txt", "w")
                i = 1
                for details in self.wl_arr:
                    wl_file.write(details[0] + "," + "WL" + "," + "WL-" + str(i) + "," + ",") # RAC counts
                    wl_file.write("\n")    
                    i += 1
                wl_file.close()
                self.tickets_dict["waiting_list"] += 1
                
                self.seat_arr.append(["WL", "\n"])
                return first_in_rac


        


