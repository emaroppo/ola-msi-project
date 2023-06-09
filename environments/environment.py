import numpy as np

class Environment:
    def __init__(self, probabilities):
        self.probabilities = probabilities

    def round(self, pulled_arm):
        reward = np.random.binomial(1, self.probabilities[pulled_arm])       
        return reward
    
    def opt(self):
        return np.max(self.probabilities)




