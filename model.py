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

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 100

    def step(self):

        if self.wealth == 0:
            return
        
        if self.random.random() < 0.5:
            self.wealth += (self.wealth / 2) /2 
        else:
            self. wealth -= self.wealth / 2

class MoneyModel(Model):

    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)

        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)


        self. datacollector = DataCollector(
            model_reporters = {"Gini": compute_gini},
            agent_reporters = {"Wealth": "wealth"}
            )


    def step(self):
        '''Advance the model by one step.'''
        self.datacollector.collect(self)
        self.schedule.step()

model = MoneyModel(1000)

for i in range(20):
    model.step()

gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
plt.show()

agent_wealth = [a.wealth for a in model.schedule.agents]
print(max(agent_wealth))

plt.hist(agent_wealth)
plt.show()