line = input()
totalTickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0


while line != "Finish":
    movie_name = line
    free_seats = int(input())
    sold_tickets_per_movie = 0
    command = input()

    while command != "End":
        ticket_type = command
        totalTickets += 1
        sold_tickets_per_movie +=1
        if ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
        else:
            kid_tickets += 1

        if sold_tickets_per_movie == free_seats:
            break
        command = input()
    percentSeats = (sold_tickets_per_movie / free_seats) * 100
    print(f"{movie_name} - {percentSeats:.2f}% full.")
    line = input()
print(f"Total tickets: {totalTickets}")
percent_student_tick = (student_tickets / totalTickets) * 100
print(f"{percent_student_tick:.2f}% student tickets.")

percent_standard_tick = (standard_tickets / totalTickets) * 100
print(f"{percent_standard_tick:.2f}% standard tickets.")

percent_kid_tick = (kid_tickets / totalTickets) * 100
print(f"{percent_kid_tick:.2f}% kids tickets.")