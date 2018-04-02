'''
from scipy.integrate import quad

# provided with number of heads and tails find certainty that coin is fair
# then provided with fairness, find certainty that coin is heads
# P(fair coin|heads seen) =
# P(heads that were|heads that should have been)P(heads that should have been)/P(heads that were)
# $Posterior = \dfrac{likelihood * prior}{\sum_{\theta} likelihood * prior}$
h = 0
t = 0
θ = 1/2

x = input('Heads[h] or Tails[t]: ')
if x.lower() == 'h':
    h += 1
if x.lower() == 't':
    t += 1
def integrand(h):
    return θ ** h

b = quad(integrand(h), 0, 1)
print(b)
def normalize(possibilities):
  possibility_sum = sum(possibilities)
  for hypothesis in range(0,101):
    possibility = possibilities[hypothesis]
    possibilities[hypothesis] = possibility/possibility_sum

def update_success(possibilities):
  for hypothesis in range(0, 101):
    likelihood = possibilities[hypothesis]
    possibilities[hypothesis] = likelihood*hypothesis/100.0
  normalize(possibilities)

def update_failure(possibilities):
  for hypothesis in range(0, 101):
    likelihood = possibilities[hypothesis]
    possibilities[hypothesis] = likelihood*(1.0-hypothesis/100.0)
  normalize(possibilities)

# set every possibility to be equally possible
possibilities = [1.0]*101

# Coin flip, probability of heads
normalize(possibilities)
update_success(possibilities)
update_failure(possibilities)
update_success(possibilities)
update_success(possibilities)

print(possibilities)
'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_coin_flips = np.random.randint(2, size=1000)
print(np.mean(data_coin_flips))

bernoulli_flips = np.random.binomial(n=1, p=.5, size=1000)
print(np.mean(bernoulli_flips))

def bern_pmf(x, p):
    if (x == 1):
        return p
    elif (x == 0):
        return 1 - p
    else:
        return "Value Not in Support of Distribution"

print(bern_pmf(1, .5))
print(bern_pmf(0, .5))

np.product(st.bernoulli.pmf(data_coin_flips, .5))

sns.set(style='ticks', palette='Set2')

params = np.linspace(0, 1, 100)
p_x = [np.product(st.bernoulli.pmf(data_coin_flips, p)) for p in params]
plt.plot(params, p_x)
sns.despine()

fair_flips = bernoulli_flips = np.random.binomial(n=1, p=.5, size=1000)
p_fair = np.array([np.product(st.bernoulli.pmf(fair_flips, p)) for p in params])
p_fair = p_fair / np.sum(p_fair)
plt.plot(params, p_fair)
sns.despine()


def bern_post(n_params=100, n_sample=100, true_p=.8, prior_p=.5, n_prior=100):
    params = np.linspace(0, 1, n_params)
    sample = np.random.binomial(n=1, p=true_p, size=n_sample)
    likelihood = np.array([np.product(st.bernoulli.pmf(sample, p)) for p in params])
    # likelihood = likelihood / np.sum(likelihood)
    prior_sample = np.random.binomial(n=1, p=prior_p, size=n_prior)
    prior = np.array([np.product(st.bernoulli.pmf(prior_sample, p)) for p in params])
    prior = prior / np.sum(prior)
    posterior = [prior[i] * likelihood[i] for i in range(prior.shape[0])]
    posterior = posterior / np.sum(posterior)

    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 8))
    axes[0].plot(params, likelihood)
    axes[0].set_title("Sampling Distribution")
    axes[1].plot(params, prior)
    axes[1].set_title("Prior Distribution")
    axes[2].plot(params, posterior)
    axes[2].set_title("Posterior Distribution")
    sns.despine()
    plt.tight_layout()

    return posterior