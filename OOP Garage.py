class OOPGarage:
    def __init__(self, num_tickets, num_parking_spaces):
        self.tickets = [i for i in range(1, num_tickets+1)]
        self.parking_spaces = [i for i in range(1, num_parking_spaces+1)]
        self.tickets_dict = {}

    def take_ticket(self):
        if self.tickets:
            ticket_num = self.tickets.remove(-1)
            parking_spot = self.parking_spaces.remove(-1)
            self.new.ticket[ticket_num] = {'parking_spot': parking_spot}
        
    def pay_for_parking(self):
        ticket_num = int(input("enter number:"))
        if self.tickets_dict.get(ticket_num):
            if not self.tickets_dict[ticket_num]['paid']
            self.cnew.ticket[ticket_num]['paid'] = True
            print("Ticket paid. 15 minutes remaining.")
        
    def leave_garage(self):
        ticket_num = int(input("Enter number: "))
        if self.new.ticket.get(ticket_num):
            if self.cnew.ticket[ticket_num]['paid']:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(self.tickets_dict[ticket_num]['parking_spot'])
                del self.new.ticket[ticket_num]
                self.tickets.append(ticket_num)