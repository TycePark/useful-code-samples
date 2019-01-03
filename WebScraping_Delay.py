##Use this function for sleep during webscraping with Selenium to mimick human activity

from scipy.stats import truncnorm
from time import sleep

def get_truncated_normal(mean, sd, low, upp):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

print("This is the output")
seconds = round(get_truncated_normal(mean=6, sd=3, low=3, upp=9).rvs(),2)
sleep(seconds)
print("This is the next output")
