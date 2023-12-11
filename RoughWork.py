import sys
sys.path.append(r'C:\Users\sangee\TrainTicket')
import BerthTypes
seat_arr = []
seat_file = open("AvailableSeats.txt")  
for seats in seat_file:
    seat_arr.append(seats.split(",")) 
seat_file.close()  
seat_no = seat_arr[len(seat_arr) - 1]
seat_arr.pop()
seat_file = open("AvailableSeats.txt", "w")  
for seats in seat_arr:
    seat_file.write(seats[0] + "," )
    seat_file.write("\n") 

seat_file.close()