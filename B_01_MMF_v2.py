import pandas


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
         at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full world
        or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire world
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
    
    
For each ticket holder enter...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the
ticket cost (and the profit).

Once you have either sold all of the tickets or entered the
exit code ('xxx), the program will display the ticket
sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the
draw (their ticket is free).

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be a blank. Please try again.\n")


def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer more than zero."

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def currency(x):
    """Formats numbers are currency ($#.##)"""
    return "${:.2f}".format(x)


# Main routine goes here

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialise variables / non-default options
payment_ans = ('cash', 'credit')

# Ticket Price List
CHILD_PRICE = 7.50
Adult_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# lists to hold ticket details
all_names = []
all_tickets_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_tickets_costs,
    'Surcharge': all_surcharges
}

# Program main heading
make_statement("Mini-Movie Fundraiser Program", "🍿")

# Ask user if they want to see the instructions
# display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# Loop to get name, age and payment details
while tickets_sold < MAX_TICKETS:
    # ask user for their name (and check it's not blank)
    print()
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue

    # Child ticket price is $7.50
    elif age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket ($10.50)
    elif age < 65:
        ticket_price = Adult_PRICE

    # Senior Citizen ticket ($6.50)
    elif age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    # if paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # add name, ticket cost and surcharge
    all_names.append(name)
    all_tickets_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# End of Ticket Loop!

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total payable for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Output movie frame without index
print(mini_movie_frame.to_string(index=False))

print(mini_movie_frame)
print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets)")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
