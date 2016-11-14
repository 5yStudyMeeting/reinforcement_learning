import numpy as np
import matplotlib.pyplot as plt
import math

class N_Armed_Bandit(object):
    def __init__(self):
        # 0 < value < 2
        self.v_astes = (0.2, 1.2, 0.7, 0.1, 1.1, 1.5, 0.4, 1.8, 0.5, 1.0)
        self.act_counts  = np.asarray([0 for _ in range(10)])
        self.Q_t    = np.asarray([0.3 for _ in range(10)])
        ########
        #
        # Q_t = ( r_1 + r_2 + ... + r_n ) / k_a ,
        #
        # where k_a is the number of selecting the action,
        #
        # and default Q_t is 0.3
        ####################
        self.value_aves  = []
        self.value_sum   = 0

    def e_greedy(self,epsilon=0.1):
        m = np.random.rand()
        tmp = math.floor(np.random.rand()*10)
        act = self.Q_t.argmax() if m>epsilon else tmp
        return act

    def update_Qt(self,act,r):
        q = self.Q_t[act] * self.act_counts[act]
        # q = r_ave * n = sum(r_a)
        self.act_counts[act] += 1
        Q_t = ( q + r ) / self.act_counts[act]
        self.Q_t[act] = Q_t
        return

    def gen_reword(self,act):
        mu = self.v_astes[act]
        r = np.random.normal(mu,1)
        return r

    def gen_graph(self,n):
        x = np.arange(0, n, 1)
        plt.plot(x, self.value_ave)

    def train(self,n):
        for i in range(1,n+1):
            act = self.e_greedy()
            r = self.gen_reword(act)
            self.value_sum += r
            self.value_aves.append(self.value_sum/i)
            self.update_Qt(act,r)
        #self.gen_graph(n)

if __name__ == "__main__":
    narm_eg = N_Armed_Bandit()
    narm_eg.train(1000)
    narm_g = N_Armed_Bandit(e_g=False)
    narm_g.train(1000)

    plt.plot(narm_eg.value_aves, label="e-greedy")
    plt.plot(narm_g.value_aves, label="greedy")
    plt.legend()

    plt.title("N_armed_bandit")
    plt.xlabel("Number of trials")
    plt.ylabel("Got reword")
    plt.show()
