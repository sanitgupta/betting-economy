import numpy as np
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt

def compute_gini(model):
    
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents

    B = sum(xi * (N-i) for i, xi in enumerate(x)) / (N * sum(x))

    return (1 + (1/N) - 2 * B)

class MoneyAgent(Agent):

    def __init__(self, unique_id, model, risky, init_wealth = 100):
        
        super().__init__(unique_id, model)
        self.wealth = init_wealth
        self.risky = risky

    def step(self):

        if self.wealth == 0:
            return

        if self.risky:
            if self.random.random() < 0.5:
                self.wealth += (self.wealth / 2) / 2 
            else:
                self. wealth -= self.wealth / 2
        else:
            if self.random.random() < 0.9:
                self.wealth += self.wealth / 20
            else:
                self.wealth -= self.wealth / 10


class MoneyModel(Model):

    def __init__(self, N, risky_frac = 0.5):

        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.risky_frac = risky_frac

        for i in range(self.num_agents):
            if self.random.random() < risky_frac:
                risky = True
            else:
                risky = False
            
            a = MoneyAgent(i, self, risky)
            self.schedule.add(a)


        self. datacollector = DataCollector(
            model_reporters = {"Gini": compute_gini},
            agent_reporters = {"Wealth": "wealth"}
            )


    def step(self):

        self.datacollector.collect(self)
        self.schedule.step()

model = MoneyModel(10000)

for i in range(20):
    model.step()

gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
plt.show()

risky_agent_wealth = [a.wealth for a in model.schedule.agents if a.risky == True]
print("Risk Takers (max and mean wealth at the end): ", max(risky_agent_wealth), np.mean(risky_agent_wealth))
plt.hist(risky_agent_wealth)
plt.show()


notrisky_agent_wealth = [a.wealth for a in model.schedule.agents if a.risky == False]

print("Risk Avoiders (max and mean wealth at the end): ", max(notrisky_agent_wealth), np.mean(notrisky_agent_wealth))
plt.hist(notrisky_agent_wealth)
plt.show()