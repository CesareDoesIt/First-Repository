def compounding_interest(interest_rate,
                         time_frame,
                         starting_point,
                         monthly_deposit,
                         months_after_trust):

    monthly_interest = (float(interest_rate) / 100) / 12
    monthly_total = starting_point + monthly_deposit

    while time_frame - 1 > 0:
        monthly_total += monthly_deposit + (monthly_interest * monthly_total)
        time_frame -= 1
    while months_after_trust > 0:
        monthly_total += (monthly_total * monthly_interest)
        months_after_trust -= 1

    return "Compounded Savings: %d" % monthly_total


def mortgage_payoff(interest_rate,
                    origninal_months,
                    starting_point,
                    additional_monthly_payment,
                    months_with_additional,
                    payment_after_trust):

    principal_owed = starting_point
    monthly_interest_rate = (float(interest_rate) / 100) / 12
    time_frame = 0
    excess_payment = 0
    principal_payments = 0
    post_trust_payments = 0
    monthly_payment = starting_point * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** - origninal_months))

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

    print "Total principal payments: %d" % principal_payments
    print "Total paid: %d" % (principal_payments + excess_payment + post_trust_payments)
    print "Total contribution of excess payment: %d" % (excess_payment + post_trust_payments)
    print "Months to pay off: %d" % time_frame

print "Here be the mortgages"

print mortgage_payoff(4.125 , 360, 96000, 746.12, 54, 200)
#print mortgage_payoff(4.125 , 360, 96000, 0, 0, 0)

print compounding_interest(5, 54, 0, 441.15, 0)
#print compounding_interest(5, 54, 0, 1187.27, 54)

#print compounding_interest(5, 306, 89788, 200, 0)