print('Profit visualization for Term Insuance with sum insured ranging from $1000 to $100,000\n')

sumInsured = float(input('What amount of Term Insurance you are selling?\n'))
term = float(input('What is the Term? (Max 15))\n'))
premium = float(input('What premium you will charge?\n'))
customers = float(input('How many customers do you have for this premium?\n'))
rate = float(input('What semi-annual risk free interest you are getting?\n'))
mc = int(input('Number of time you want to run simulation?\n'))

import random
import matplotlib.pyplot as plt

#randomly generating number of claims asked for each time simulation runs
def randomClaim(sim):
    claim = []
    for i in range(sim):
        claim.append(random.randint(0, customers))
    return claim

#calculating fraction of people who will ask for claim after every year in between total terms of insurance out of total claims
def claimProb():
    a = 1
    prob = []
    for _ in range(0, int(term)):
        b = random.uniform(0., a)
        prob.append(b)
        a = a - b
    return prob


# calculating profit after every year until term is completed
def profit(numClaim):
    net_profit = []
    probList = claimProb()
    
    # those who asked claims meand they are no more bound to pay insurance so calculating remaining number of customers
    rem_cust = []
    for i,j in enumerate(probList):
        if i == 0:
            rem_cust.append(customers - numClaim*probList[i])
        else :
            rem_cust.append(rem_cust[i-1] - numClaim*probList[i])
    
    # finding profit from amount of prev year and then calculating current year amount after settling claims ans recieving insurance from rem customers 
    curr_amount = []
    for i,s in enumerate(probList):
        if i == 0 :
            net = premium*customers
            curr_amount.append(net)
        else:
            net = curr_amount[i-1]*(1+rate/100) - sumInsured*numClaim*probList[i]
            curr_amount.append(net*(1+rate/100) + premium*rem_cust[i-1])

        net_profit.append(net)
    return net_profit
# Creating a list of terms
x = []
for i in range (0,int(term)):
    x.append(i)

# created Dummy list and  used in the process of finding the list for which Profite is maximum after the given terms     
dummy=[0,0,0,0,0,0,0,0]  
#Plotted the graph for all time code been runned and also extracted the list for which Profite is maximum after the given terms
for i in randomClaim(mc):
    y = profit(i)
    if(y[-1]>=dummy[-1]):
     dummy.clear()
     dummy.extend(y)
    plt.plot(x,y)

# here again by copping dummy into y and highled by black to maximum profitable way     
y=dummy
plt.plot(x, y, color='black')
# Leveled the graph with max profite where leveling contain Input values and etc. 
plt.text(x[-1], y[-1],f'("sumInsured={sumInsured} premium={premium}", "Risk free rate={rate} Profite after{term} years={y[-1]}Rs")', ha='center', va='bottom',color='red')

plt.xlabel("term in years")
plt.ylabel("net profit")
plt.title("Profit visualization for Term Insuance with sum insured %d" %(sumInsured))

# Added code to made only +ve y in plot
#max_profit = max(max(y) for y in [profit(i)])
plt.ylim(0, 1e10)

plt.show()

# newma691

    
    
