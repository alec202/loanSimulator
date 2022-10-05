class project1:
    def __init__(self, payment_history, debt_amount, credit_history, credit_application_num, num_credit_cards):
        # initialize the initial set of variables
        self.payment_history = payment_history
        self.debt_amount = debt_amount
        self.credit_history = credit_history
        self.credit_application_num = credit_application_num
        self.num_credit_cards = num_credit_cards
        # intialize score variables
        self.payment_history_score = 0
        self.debt_amount_score = 0
        self.credit_history_score = 0
        self.credit_application_score = 0
        self.num_credit_cards_score = 0
        self.overall_score = 500

        # line to run project class
        self.run_project()



    def run_project(self):
        # class method to run the other methods
        self.get_payment_history_score()
        self.get_debt_amount_score()
        self.get_credit_history_score()
        self.get_credit_application_score()
        self.get_num_credit_cards_score()
        self.get_total_score()
        self.__str__()



    # method to get payment_history_score
    def get_payment_history_score(self):
        if self.payment_history == -1:
            self.payment_history_score = 75
        elif self.payment_history < 6:
            self.payment_history_score = 10
        elif self.payment_history < 12:
            self.payment_history_score = 15
        elif self.payment_history < 24:
            self.payment_history_score = 25
        elif self.payment_history >= 24:
            self.payment_history_score = 55



    def get_debt_amount_score(self):
        if self.debt_amount == -1:
            self.debt_amount_score = 30
        elif self.debt_amount == 0:
            self.debt_amount_score = 55
        elif self.debt_amount < 100:
            self.debt_amount_score = 65
        elif self.debt_amount < 500:
            self.debt_amount_score = 50
        elif self.debt_amount < 750:
            self.debt_amount_score = 40
        elif self.debt_amount < 1000:
            self.debt_amount_score = 25
        elif self.debt_amount >= 1000:
            self.debt_amount_score = 15



    def get_credit_history_score(self):
        if -1 < self.credit_history < 12:
            self.credit_history_score = 12
        elif self.credit_history < 24:
            self.credit_history_score = 35
        elif self.credit_history < 48:
            self.credit_history_score = 60
        elif self.credit_history >= 48:
            self.credit_history_score = 75
        else:
            print("Impossible number entered, rerun program")



    def get_credit_application_score(self):
        if self.credit_application_num == 0:
            self.credit_application_score = 70
        elif self.credit_application_num == 1:
            self.credit_application_score = 60
        elif self.credit_application_num == 2:
            self.credit_application_score = 45
        elif self.credit_application_num == 3:
            self.credit_application_score = 25
        elif self.credit_application_num >= 4:
            self.credit_application_score = 20



    def get_num_credit_cards_score(self):
        if self.num_credit_cards == 0:
            self.num_credit_cards_score = 15
        elif self.num_credit_cards == 1:
            self.num_credit_cards_score = 25
        elif self.num_credit_cards == 2:
            self.num_credit_cards_score = 50
        elif self.num_credit_cards == 3:
            self.num_credit_cards_score = 65
        elif self.num_credit_cards >= 4:
            self.num_credit_cards_score = 50



    def get_total_score(self):
        self.overall_score += self.payment_history_score + self.debt_amount_score + self.credit_history_score + \
                              self.credit_application_score + self.num_credit_cards_score



    def __str__(self):
        if self.payment_history == -1 and self.overall_score > 800:
            print("Applicant approed for a loan from $500 to $10,000.")
        elif self.credit_application_num == 0 and self.payment_history > 12 and self.overall_score > 700:
            print("Applicant approved for a loan from $500 to $2,000.")
        elif self.credit_application_num == 0 and self.payment_history == -1 and self.overall_score > 700:
            print("Applicant approved for a loan from $500 to $5,000.")
        else:
            print("Applicant not approved for any loans")


# chunk of code to get the information about the applicant
payment_history = int(input("Enter the number of months since a negative report was made about the applicant.\n"))
outstanding_debt = int(input("Enter the clients debt balance.\n"))
credit_history_length = int(input("Number of months applicant has had credit\n"))
new_credit_applications = int(input("Number of new credit attempts in the last 6 months by the client.\n"))
credit_card_number = int(input("Number of credit accounts that are credit cards.\n"))
print()


# last chunk of code to run the actual project
run_class = project1(payment_history, outstanding_debt, credit_history_length, new_credit_applications,
                     credit_card_number)
