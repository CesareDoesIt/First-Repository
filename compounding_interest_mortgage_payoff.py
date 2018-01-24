from appJar import gui


def compounding_interest(interest_rate,
                         duration_months,
                         initial_balance,
                         monthly_deposit,
                         months_after_trust):

    monthly_interest = (float(interest_rate) / 100) / 12
    monthly_total = initial_balance + monthly_deposit

    while duration_months - 1 > 0:
        monthly_total += monthly_deposit + (monthly_interest * monthly_total)
        duration_months -= 1

    while months_after_trust > 0:
        monthly_total += (monthly_total * monthly_interest)
        months_after_trust -= 1

    return monthly_total


def mortgage_payoff(interest_rate,
                    original_months,
                    starting_point,
                    additional_monthly_payment,
                    months_with_additional,
                    payment_after_trust
                    ):

    principal_owed = starting_point
    monthly_interest_rate = (float(interest_rate) / 100) / 12
    time_frame = 0
    excess_payment = 0
    principal_payments = 0
    post_trust_payments = 0
    monthly_payment = starting_point * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** - original_months))

    while principal_owed > 0:
        if months_with_additional > 0:
            principal_owed -= (monthly_payment + additional_monthly_payment - (monthly_interest_rate * principal_owed))
            time_frame += 1
            excess_payment += additional_monthly_payment
            principal_payments += monthly_payment
            months_with_additional -= 1
        else:
            principal_owed -= (monthly_payment + payment_after_trust - (monthly_interest_rate * principal_owed))
            time_frame += 1
            principal_payments += monthly_payment
            post_trust_payments += payment_after_trust

    total = principal_payments + excess_payment + post_trust_payments
    total_contribution = excess_payment + post_trust_payments
    interest_saved = (monthly_payment * original_months) - total

    return (principal_payments, total, total_contribution, time_frame, interest_saved)


mortgage_info = mortgage_payoff(
    4.125,
    360,
    96000,
    746.12,
    54,
    200
)

print("Total principal payments: %d" % mortgage_info[0])
print("Total paid: %d" % mortgage_info[1])
print("Total contribution of excess payment: %d" % mortgage_info[2])
print("Months to pay off: %d" % mortgage_info[3])
print("Total interest saved: %d" % mortgage_info[4])

print()
#print mortgage_payoff(4.125 , 360, 96000, 0, 0, 0)

print("Compounding interest savings: %d" % compounding_interest(5, 54, 0, 441.15, 0))
#print compounding_interest(5, 54, 0, 1187.27, 54)

#print compounding_interest(5, 306, 89788, 200, 0)

def on_calculate(buttons):
    # calculate
    interest = app.getEntry("Interest rate")
    total_term = app.getEntry("Total term")
    principle = app.getEntry("Principle")
    extra_payments = app.getEntry("Extra payments")
    extra_payments_term = app.getEntry("Extra payments term")
    extra_payments_after_trust = app.getEntry("Extra payments after trust")

    print(interest)

    mortgage_info = mortgage_payoff(
        interest,
        total_term,
        principle,
        extra_payments,
        extra_payments_term,
        extra_payments_after_trust
    )

    app.setLabel("total_principle", "Total principal payments: %d" % mortgage_info[0])
    app.setLabel("total_paid", "Total paid: %d" % mortgage_info[1])
    app.setLabel("total_contribution", "Total contribution of excess payment: %d" % mortgage_info[2])
    app.setLabel("total_months", "Months to pay off: %d" % mortgage_info[3])
    app.setLabel("interest_saved", "Total interest saved: %d" % mortgage_info[4])


app = gui()
app.addLabel("title", "Welcome to Cesare's money calculation program")
app.setLabelBg("title", "red")

entries = [
    ("Interest rate", "4.125"),
    ("Total term", "360"),
    ("Principle", "96000"),
    ("Extra payments", "746.12"),
    ("Extra payments term", "54"),
    ("Extra payments after trust", "200")
]

for title, value in entries:
    app.addLabelNumericEntry(title)
    app.setEntry(title, value)

app.addButtons(["Calculate"], on_calculate)

app.addLabel("total_principle", "")
app.addLabel("total_paid", "")
app.addLabel("total_contribution", "")
app.addLabel("total_months", "")
app.addLabel("interest_saved", "")



# start the GUI
app.go()