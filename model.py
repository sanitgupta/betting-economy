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

    def __init__(self, unique_id, model, risky, rich, base_wealth = 100):
        
        super().__init__(unique_id, model)
        
        self.init_risky = risky

        self.risky = risky
        self.rich = rich

        if self.rich:
            self.base_wealth = base_wealth * 10
        else:
            self.base_wealth = base_wealth
        
        self.wealth = self.base_wealth


    def step(self):

        if self.wealth < self.base_wealth / 4:
            self.risky = False

        if self.risky:
            if self.random.random() < 0.5:
                self.wealth += self.wealth / 2
            else:
                self.wealth -= self.wealth / 2
        else:
            if self.random.random() < 0.9:
                self.wealth += self.wealth / 20
            else:
                self.wealth -= self.wealth / 10


class MoneyModel(Model):

    def __init__(self, N, risky_frac = 0.5, rich_frac = 0.5):

        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.risky_frac = risky_frac

        for i in range(self.num_agents):

            if self.random.random() < risky_frac:
                risky = True
            else:
                risky = False

            if self.random.random() < rich_frac:
                rich = True
            else:
                rich = False
            
            a = MoneyAgent(i, self, risky, rich)
            self.schedule.add(a)


        self. datacollector = DataCollector(
            model_reporters = {"Gini": compute_gini},
            agent_reporters = {"Wealth": "wealth"}
            )


    def step(self):

        self.datacollector.collect(self)
        self.schedule.step()


np.set_printoptions(precision = 2)

model = MoneyModel(10000)

for i in range(20):
    model.step()

# gini = model.datacollector.get_model_vars_dataframe()
# gini.plot()
# plt.show()

rr = [a.wealth for a in model.schedule.agents if a.init_risky == True and a.rich == True]
sr = [a.wealth for a in model.schedule.agents if a.init_risky == False and a.rich == True]
rp = [a.wealth for a in model.schedule.agents if a.init_risky == True and a.rich == False]
sp = [a.wealth for a in model.schedule.agents if a.init_risky == False and a.rich == False]


print("            ", "       Max       ", "       Mean       ", "       Median       ")
print("Risky Rich: ", max(rr), np.mean(rr), np.median(rr))
print("Safe Rich: ", max(sr), np.mean(sr), np.median(sr))
print("Risky Poor: ", max(rp), np.mean(rp), np.median(rp))
print("Safe Poor: ", max(sp), np.mean(sp), np.median(sp))



