# mov_inf = open("bookings.txt", "a")



# def make_booking():
#     name = input("Please state your name: ")
#     movie = input("What is the movie you would like to see?: ")
#     seats = input("How many seats would you like?: ")
#     vip = input("Would you like vip seats? (TRUE, FALSE): ")
#     booking = f"Name: {name}, Movie: {movie}, Seats: {seats}, VIP: {vip}\n"
#     return booking
# def choice():
#     end = input("Would you like to add more? (YES, NO): ")

#     return end

# Dude = "man"

# while Dude == "man":
#     make_booking()
#     choice()
#     mov_inf.write(make_booking)

#     if choice().end.upper() == "NO":
#         break  
mov_inf = open("bookings.txt", "a")

def make_booking():
    name = input("Please state your name: ")
    movie = input("What is the movie you would like to see?: ")
    seats = input("How many seats would you like?: ")
    vip = input("Would you like vip seats? (TRUE, FALSE): ")
    booking = f"Name: {name}, Movie: {movie}, Seats: {seats}, VIP: {vip}\n"
    return booking

def choice():
    end = input("Would you like to add more? (Y, N): ")
    return end.upper()

while True:
    booking = make_booking()
    ans = choice()
    mov_inf.write(booking)
    if ans == "N":
        break  

mov_inf.close()


# name = input("Please state your name: ")
# movie_name = input("What is the movie you would like to see?: ")
# num_seats = input("How many seats would you like?: ")
# vip = input("Would you like vip seats? (TRUE, FALSE): ")

# new_line = f"Name: {name}, Movie: {movie_name}, Seats: {num_seats}, VIP: {vip}\n"

# mov_inf.write(new_line)