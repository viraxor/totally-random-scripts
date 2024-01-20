from matplotlib import pyplot as plt
import random

start_balance = 100
gambling = 1

balance_list = [start_balance]
win_list = []

balance = start_balance
print(balance)

while balance > 0:
    outcome = random.randint(0, 2)
    if outcome == 0:
        balance -= gambling
    elif outcome == 2:
        balance += gambling
    balance_list.append(balance)
    win_list.append(outcome)
    
win_percent = round(win_list.count(2)/len(balance_list) * 100, 2)
lose_percent = round(win_list.count(0)/len(balance_list) * 100, 2)
nothing_percent = round(win_list.count(1)/len(balance_list) * 100, 2)
average_balance = round(sum(balance_list)/len(balance_list))
    
plt.plot(balance_list)
plt.title(f"Gambling {gambling}, starting from {start_balance}")
plt.xlabel("Amount of gambles")
plt.ylabel("Balance")
plt.figtext(0.99, 0.01, f"Total amount of gambles: {len(balance_list)}\nHighest balance: {max(balance_list)}\nWin: {win_percent}% ({win_list.count(2)} times), Lose: {lose_percent}% ({win_list.count(0)} times), Nothing: {nothing_percent}% ({win_list.count(1)} times)\nAverage balance: {average_balance}, deviation {average_balance-start_balance}", 
horizontalalignment='right')

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()