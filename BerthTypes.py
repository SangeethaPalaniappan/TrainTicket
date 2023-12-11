

class Berth:
    tickets_dict = {}
    arr = []
    file = open("AvailableTicketDetails.txt")
    i = 0
    for tickets in file:
        arr.append(tickets.split(","))    
        tickets_dict[arr[i][0]] = int(arr[i][1])
        i += 1  
    file.close()

    berth_type_dict = {}
    berth_type_det = []
    file_1 = open("BerthTypeDetails.txt")
    i = 0
    for tickets in file_1:
        berth_type_det.append(tickets.split(","))    
        berth_type_dict[berth_type_det[i][0]] = int(berth_type_det[i][1])
        i += 1  
    file_1.close()
    print(berth_type_dict)    

    seat_arr = []
    seat_file = open("AvailableSeats.txt")  
    for seats in seat_file:
        seat_arr.append(seats.split(",")) 
    seat_file.close()    

    @classmethod
    def assign_ticket(cls, berth_preference): 
        possibility = 0
        for berths in cls.tickets_dict:
            if cls.tickets_dict[berths] > 0:
                if berths == "rac_berths":
                    berth_type = cls.check_berth_availability("side_lower_rac")
                    berth_preference = "side_lower_rac"
                else:    
                    berth_type = cls.check_berth_availability(berth_preference)  
                cls.tickets_dict[berths] -= 1 
                possibility = 1 
                cls.reduce_ticket(berth_preference, berths)
                seat_no = cls.seat_allotment()
                break
        if possibility == 0:
            return None, "Currently No Tickets available"
        return seat_no, berth_type
    @classmethod
    def reduce_ticket(cls, berth_type, berth): 
        write_in_file = open("BerthTypeDetails.txt", 'w')
        for i in range(len(cls.berth_type_det)):
            write_in_file.write(cls.berth_type_det[i][0] + "," + str(cls.berth_type_dict[cls.berth_type_det[i][0]]) + ",")
            write_in_file.write("\n")    
        write_in_file.close()
        file_1 = open("AvailableTicketDetails.txt", "w")  
        for i in range(len(cls.arr)):
            file_1.write(cls.arr[i][0] + "," + str(cls.tickets_dict[cls.arr[i][0]]) + ",")
            file_1.write("\n") 
    
        file_1.close()

    @classmethod
    def seat_allotment(cls):
        seat_no = cls.seat_arr[len(cls.seat_arr) - 1][0]
        cls.seat_arr.pop()
        seat_file = open("AvailableSeats.txt", "w")  
        for seats in cls.seat_arr:
            seat_file.write(seats[0] + "," )
            seat_file.write("\n") 
    
        seat_file.close()
        return seat_no
    
    @classmethod
    def check_berth_availability(cls, berth_preference):
        if cls.berth_type_dict[berth_preference] > 0 :
                cls.berth_type_dict[berth_preference] -= 1
                type = berth_preference

        else:
            for type in cls.berth_type_dict :
                if type != berth_preference and type != "side_lower_rac":
                    cls.berth_type_dict[type] -= 1 
                    break
        return type        
        

    def move_to_rac():
        pass

    def over_ride_details():
        pass
