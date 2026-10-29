# ECON7890 Big Data Analytics - Programming - Assignment 1
#
# Five questions, one at each difficulty level. 100 marks.
#
#   Q1  authorise              *        15 marks   conditions
#   Q2  bounced_debits         **       15 marks   a list and a for loop
#   Q3  commission_by_client   ***      20 marks   a dictionary built in a loop
#   Q4  trailing_stop          ****     25 marks   a loop that carries state
#   Q5  fund_allocation        *****    25 marks   all of it together
#
# Everything here needs only what weeks 1-4 taught: if/elif/else, and/or/not,
# lists, .append(), for, range(), dictionaries, .get(), min(), max(), round(),
# len(), sum(). You do not need `while`, `break`, Decimal, or any import.
#
#  YOU WRITE THE def LINES
#   Q1 gives you its def line. From Q2 on, write the def line yourself, using
#   the Function Name and the Input Parameters listed, in the SAME ORDER.
#
#  WHAT TO SUBMIT
#   - THIS FILE, with your answers and your tests in it, as a .py file named
#     assignment1.py. Not a notebook, not a zip, not a screenshot.
#   - Upload it to Assignment 1 on Moodle before the deadline shown there.
#     Moodle closes at the deadline.
#   - This is individual work.
#
#  YOUR FILE MUST RUN, FROM THE TOP TO THE BOTTOM
#   Before you submit, run the whole file. It must reach the last line with
#   no error. If it stops on an error, the grader cannot load your file -
#   and that includes one of YOUR OWN asserts failing.
#   So if an assert fails, fix the function or fix the assert. Never submit a
#   file with a failing assert in it.
#
#  AI
#   You may use AI to explain things, quiz you, and decode error messages.
#   One rule: you must be able to explain and defend every line you submit.
#
#  RULES AND PENALTIES
#   None of these are about ability - they are about reading the instructions.
#   - Not a .py file, or not named assignment1.py ........ -20 marks
#   - File does not run (an error anywhere, including a
#     failing assert) .................................... -40% of each question
#   - A function name or its parameters not EXACTLY as
#     given .............................................. -50% of that question
#   - A library other than math or decimal (you need
#     neither) ........................................... -50% of that question
#   - Prints the answer instead of RETURNING it .......... 0 for that question
#   - Late ............................................... no mark
#   Define each function once and only once. Comments are ignored - add your
#   own freely.
#
#  THE RULES IN EACH QUESTION ARE SIMPLIFIED
#   Real banks, brokers and funds have more rules than these. Follow the rules
#   exactly as written here, even where the real world works differently.
#
#  MONEY - YOU DO NOT NEED Decimal
#   Amounts are floats in HK dollars. Where a question says "round to 2
#   places", the normal round(x, 2) is enough - every test was checked with it.
#   Decimal is also accepted, if you prefer it, but no question requires it.
#
#  TESTING IS REQUIRED
#   Just below each function, write asserts that test it. For every question:
#     1. Every example given, as an assert.
#     2. EVERY BRANCH of your code: each if, elif and else you wrote must be
#        reached by at least one assert. If a branch is never tested, you do
#        not know that it works.
#     3. Every case listed under "You must test" for that question.
#   The grader runs many more tests than the examples. A function that only
#   passes the examples will lose marks.
# ---------------------------------------------------------------------------

# Question 1 (15 marks)   Difficulty: *....
# Function Name: authorise
#
# A card payment arrives. Decide what happens to it. Go down this list and use
# the FIRST rule that fits:
#
#   1. The card is frozen:              "declined: card frozen"
#   2. The amount is 0 or less:         "declined: invalid amount"
#   3. The amount is more than the
#      balance:                         "declined: insufficient funds"
#   4. Otherwise:                       "approved"
#
# A payment of exactly the balance is approved.
#
# Input Parameters:
#   - amount  (float) the payment amount
#   - balance (float) the money in the account
#   - frozen  (bool)  True if the card is frozen
#
# Examples:
#   authorise(500.0, 2000.0, False)
#       -> "approved"
#   authorise(2000.0, 2000.0, False)
#       -> "approved"
#   authorise(2500.0, 2000.0, False)
#       -> "declined: insufficient funds"
#   authorise(500.0, 2000.0, True)
#       -> "declined: card frozen"
#   authorise(0.0, 2000.0, False)
#       -> "declined: invalid amount"
#
# You must test (as well as every example and every branch):
#   - each of the four results at least once
#   - a frozen card with an amount of 0 (two rules fit - which wins?)
#   - an amount exactly equal to the balance

def authorise(amount, balance, frozen):
    # Rule 1: The card is frozen
    if frozen:
        return "declined: card frozen"
    # Rule 2: The amount is 0 or less
    if amount <= 0:
        return "declined: invalid amount"
    # Rule 3: The amount is more than the balance
    if amount > balance:
        return "declined: insufficient funds"
    # Rule 4: Otherwise 
    else:
        return "approved"

    print(authorise(500.0, 2000.0, False))    # approved
print(authorise(2000.0, 2000.0, False))   # approved
print(authorise(2500.0, 2000.0, False))   # declined: insufficient funds
print(authorise(500.0, 2000.0, True))     # declined: card frozen
print(authorise(0.0, 2000.0, False))      # declined: invalid amount
print(authorise(0.0, 2000.0, True))       # declined: card frozen 



# Question 2 (15 marks)   Difficulty: **...
# Function Name: bounced_debits
#
# Direct debits (automatic bill payments) come out of an account one at a time,
# in the order given.
#
#   - If the balance is enough, the debit is paid and the balance goes down.
#   - If not, the debit BOUNCES: it is not paid, and the balance does not change.
#     A later, smaller debit may still be paid.
#
# Round the balance to 2 decimal places after every payment.
# Every debit is more than 0.
#
# Return a list of the debits that bounced, in the order they bounced.
#
# Input Parameters:
#   - balance (float)          the money in the account at the start
#   - debits  (list of float)  the debits, in order
#
# Examples:
#   bounced_debits(1000.0, [300.0, 800.0, 500.0, 200.0])
#       -> [800.0]
#   bounced_debits(100.0, [150.0, 50.0, 60.0])
#       -> [150.0, 60.0]
#   bounced_debits(500.0, [])
#       -> []
#
# You must test (as well as every example and every branch):
#   - a debit that is paid, and one that bounces
#   - a debit exactly equal to the balance
#   - a bounce followed by a smaller debit that is paid
#   - an empty list
#
def bounced_debits(balance, debits):
    bounced = []
    current_balance = balance
    for amount in debits:
        if current_balance >= amount:
            current_balance = round(current_balance - amount, 2)
        else:
            bounced.append(amount)
    return bounced


# Test cases
print(bounced_debits(1000.0, [300.0, 800.0, 500.0, 200.0]))
print(bounced_debits(100.0, [150.0, 50.0, 60.0]))
print(bounced_debits(500.0, []))
# Required extra tests
print(bounced_debits(200.0, [200.0, 100.0]))    # debit exactly equal to balance
print(bounced_debits(100.0, [200.0, 80.0]))     # bounce then a smaller successful debit



# Question 3 (20 marks)   Difficulty: ***..
# Function Name: commission_by_client
#
# A broker gives each client some free trades. `trades` is a LIST, in the order
# the trades were made, so it tells you which trade came first.
#
#   - A client's FIRST `free_trades` trades in the list are free.
#   - Every trade that client makes after that costs `fee`.
#   - Each client has their OWN free trades. Amy's trades do not use up Ben's.
#
# Each trade is a dictionary like {"client": "Amy", "stock": "0700"}. Only the
# client matters here.
#
# In the first example below, with free_trades = 2, go down the list:
#   Amy (Amy's 1st: free), Ben (Ben's 1st: free), Amy (Amy's 2nd: free),
#   Amy (Amy's 3rd: 15.0), Amy (Amy's 4th: 15.0)
# so Amy pays 30.0 and Ben pays 0.0.
#
# Return a dictionary: each client -> the total commission they pay, rounded to
# 2 places. Every client who made a trade must appear, even if they paid 0.
#
# Input Parameters:
#   - trades      (list of dict) the trades, in the order they were made
#   - free_trades (int)          how many free trades EACH client gets
#   - fee         (float)        the charge for each trade after that
#
# Examples:
#   commission_by_client([{"client": "Amy", "stock": "0700"},
#       {"client": "Ben", "stock": "0005"},
#       {"client": "Amy", "stock": "0005"},
#       {"client": "Amy", "stock": "0939"},
#       {"client": "Amy", "stock": "0700"}], 2, 15.0)
#       -> {"Amy": 30.0, "Ben": 0.0}
#   commission_by_client([{"client": "Amy", "stock": "0700"},
#       {"client": "Ben", "stock": "0005"}], 0, 15.0)
#       -> {"Amy": 15.0, "Ben": 15.0}
#   commission_by_client([], 2, 15.0)
#       -> {}
#
# You must test (as well as every example and every branch):
#   - a client still inside their free trades, and one past them
#   - two clients, to show each has their OWN free trades
#   - free_trades of 0
#   - a client who pays 0 still appears
#   - an empty list
#
# Write the def line yourself, then the function, then your tests.
def commission_by_client(trades, free_trades, fee):
    # count how many trades each client has made
    trade_count = {}
    commission = {}

    for trade in trades:
        name = trade["client"]
        # initialise if new client
        if name not in trade_count:
            trade_count[name] = 0
            commission[name] = 0.0

        trade_count[name] += 1
        # if this trade is after free quota, add fee
        if trade_count[name] > free_trades:
            commission[name] += fee

    # round every value to 2 decimal places
    for c in commission:
        commission[c] = round(commission[c], 2)

    return commission


# Test cases
print(commission_by_client([
    {"client": "Amy", "stock": "0700"},
    {"client": "Ben", "stock": "0005"},
    {"client": "Amy", "stock": "0005"},
    {"client": "Amy", "stock": "0939"},
    {"client": "Amy", "stock": "0700"}
], 2, 15.0))
# expected {'Amy': 30.0, 'Ben': 0.0}

print(commission_by_client([
    {"client": "Amy", "stock": "0700"},
    {"client": "Ben", "stock": "0005"}
], 0, 15.0))
# expected {'Amy': 15.0, 'Ben': 15.0}

print(commission_by_client([], 2, 15.0))
# expected {}




# Question 4 (25 marks)   Difficulty: ****.
# Function Name: trailing_stop
#
# You buy one share at the first price in the list (day 1). You protect it with
# a trailing stop of `trail` dollars:
#
#   - The stop level is the HIGHEST price seen so far, minus `trail`.
#     So the stop moves UP when the price makes a new high, and never moves down.
#   - The first day the price is AT OR BELOW the stop level, you sell at that
#     day's price. Later days do not matter.
#   - If that never happens, you sell on the last day, at the last price.
#
# Days are counted from 1. `trail` is more than 0.
#
# Return a dictionary {"day": ..., "price": ..., "profit": ...}
# where profit is the selling price minus the buying price, rounded to 2 places.
# If the list is empty, return None.
#
# Hints - the supplementary slides "Two loop patterns" show both of these:
#   - Keep a variable for the HIGHEST price so far. Start it at the first
#     price, and change it whenever a day's price is higher.
#   - Keep a variable for the sale, starting as None. Only fill it in while it
#     is still None - that way only the FIRST day the stop is hit counts.
#
# Input Parameters:
#   - prices (list of float) the closing price on each day, day 1 first
#   - trail  (float)         how far below the highest price the stop sits
#
# Examples:
#   trailing_stop([100.0, 104.0, 110.0, 107.0, 103.0, 101.0], 5.0)
#       -> {"day": 5, "price": 103.0, "profit": 3.0}
#   trailing_stop([50.0, 52.0, 55.0], 5.0)
#       -> {"day": 3, "price": 55.0, "profit": 5.0}
#   trailing_stop([100.0, 95.0, 120.0], 5.0)
#       -> {"day": 2, "price": 95.0, "profit": -5.0}
#   trailing_stop([], 5.0)
#       -> None
#
# You must test (as well as every example and every branch):
#   - the stop is hit, and the stop is never hit
#   - a price exactly at the stop level
#   - a new high that moves the stop up before it is hit
#   - a list of one day, and an empty list
#
# Write the def line yourself, then the function, then your tests.
def trailing_stop(prices, trail):
    if not prices:
        return None

    buy_price = prices[0]
    highest_so_far = buy_price
    sell_day = None
    sell_price = None

    for idx, price in enumerate(prices):
        day = idx + 1
        # update highest price seen so far
        if price > highest_so_far:
            highest_so_far = price
        stop_level = highest_so_far - trail

        # only check sell condition if we haven't sold yet
        if sell_day is None:
            if price <= stop_level:
                sell_day = day
                sell_price = price

    # if never triggered stop-loss, sell on last day
    if sell_day is None:
        sell_day = len(prices)
        sell_price = prices[-1]

    profit = round(sell_price - buy_price, 2)
    return {"day": sell_day, "price": sell_price, "profit": profit}


# Test cases
print(trailing_stop([100.0, 104.0, 110.0, 107.0, 103.0, 101.0], 5.0))
# {'day': 5, 'price': 103.0, 'profit': 3.0}

print(trailing_stop([50.0, 52.0, 55.0], 5.0))
# {'day': 3, 'price': 55.0, 'profit': 5.0}

print(trailing_stop([100.0, 95.0, 120.0], 5.0))
# {'day': 2, 'price': 95.0, 'profit': -5.0}

print(trailing_stop([], 5.0))
# None



# Question 5 (25 marks)   Difficulty: *****
# Function Name: fund_allocation
#
# A new fund can hold at most `capacity` dollars in total. It starts empty.
# Orders are handled one at a time, in order. Each order is a dictionary like
# {"investor": "Amy", "type": "in", "amount": 5000.0}.
#
#   "in"   The investor puts money in. If there is not enough room left in the
#          fund, they get only the room that is left (which may be 0). The rest
#          of their money is turned away.
#
#   "out"  The investor takes money out. They cannot take out more than they
#          hold: if they ask for more, they get everything they hold.
#          Money taken out makes room for later "in" orders.
#
# Return a dictionary: each investor -> how much they hold at the end, rounded
# to 2 places. Every investor who placed any order must appear, even if they
# hold 0.
#
# Input Parameters:
#   - orders   (list of dict) the orders, in order
#   - capacity (float)        the most the fund can hold
#
# Examples:
#   fund_allocation([{"investor": "Amy", "type": "in", "amount": 6000.0},
#       {"investor": "Ben", "type": "in", "amount": 5000.0},
#       {"investor": "Cat", "type": "in", "amount": 2000.0},
#       {"investor": "Amy", "type": "out", "amount": 1500.0},
#       {"investor": "Cat", "type": "in", "amount": 2000.0}], 10000.0)
#       -> {"Amy": 4500.0, "Ben": 4000.0, "Cat": 1500.0}
#   fund_allocation([{"investor": "Dan", "type": "out", "amount": 100.0}], 1000.0)
#       -> {"Dan": 0.0}
#   fund_allocation([], 1000.0)
#       -> {}
#
# You must test (as well as every example and every branch):
#   - an "in" that fits, one partly filled, and one into a full fund
#   - an "out" for less than held, and one for more than held
#   - an "out" that makes room for a later "in"
#   - an empty list
#
# Write the def line yourself, then the function, then your tests.
def fund_allocation(orders, capacity):
    investor_balance = {}
    total_in_fund = 0.0

    for order in orders:
        name = order["investor"]
        o_type = order["type"]
        amount = order["amount"]

        # create entry if investor is new
        if name not in investor_balance:
            investor_balance[name] = 0.0

        if o_type == "in":
            available_space = capacity - total_in_fund
            add_amt = min(amount, available_space)
            investor_balance[name] += add_amt
            total_in_fund += add_amt

        elif o_type == "out":
            take_amt = min(amount, investor_balance[name])
            investor_balance[name] -= take_amt
            total_in_fund -= take_amt

    # round all values to 2 decimal places
    for inv in investor_balance:
        investor_balance[inv] = round(investor_balance[inv], 2)

    return investor_balance


# Test cases
print(fund_allocation([
    {"investor": "Amy", "type": "in", "amount": 6000.0},
    {"investor": "Ben", "type": "in", "amount": 5000.0},
    {"investor": "Cat", "type": "in", "amount": 2000.0},
    {"investor": "Amy", "type": "out", "amount": 1500.0},
    {"investor": "Cat", "type": "in", "amount": 2000.0}
], 10000.0))
# expected {'Amy': 4500.0, 'Ben': 4000.0, 'Cat': 1500.0}

print(fund_allocation([{"investor": "Dan", "type": "out", "amount": 100.0}], 1000.0))
# expected {'Dan': 0.0}

print(fund_allocation([], 1000.0))
# expected {}



