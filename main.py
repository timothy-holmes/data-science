#%%

import numpy as np
from matplotlib import pyplot as plt

quotes = [(650,1036),
    (745,992),
    (800,956),
    (900,902),
    (1200,816),
    (1700,756),
    (2200,642)]

coverage = np.array([coverage for coverage,premium in quotes])
premium = np.array([premium for coverage,premium in quotes])

m,b = np.polyfit(coverage,premium,1)

plt.plot(coverage,premium,'o')
plt.plot(coverage,m*coverage+b)
plt.show()


# %%

import numpy as np
from matplotlib import pyplot as plt

quotes = [
    (11500,683),
    (12500,703),
    (13500,721),
    (14500,739),
    (15500,758),
    (16500,778),
    (17000,805),
    (17500,836),
    (18500,911),
    (19500,981),
    (16000,768),
    (15000,748),
    (16700,786),
    (16300,774)]

# from observation
breakpoint = 16500

# split tuples into single variable and limited domain
coverage = np.array([coverage for coverage,_ in quotes if coverage >= breakpoint])
premium = np.array([premium for coverage,premium in quotes if coverage >= breakpoint])
coverage_alt = np.array([coverage for coverage,_ in quotes if coverage <= breakpoint])
premium_alt = np.array([premium for coverage,premium in quotes if coverage <= breakpoint])

# linear regression for both segments
m, b = np.polyfit(coverage, premium, 1)
m_alt, b_alt = np.polyfit(coverage_alt, premium_alt, 1)

plt.plot(coverage, premium,'o')
plt.plot(coverage_alt, premium_alt,'o')
plt.plot(coverage, m*coverage + b)
plt.plot(coverage_alt, m_alt*coverage_alt + b_alt)
plt.show()

# %%
