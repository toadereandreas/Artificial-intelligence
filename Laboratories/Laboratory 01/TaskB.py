# -*- coding: utf-8 -*-
"""
Spyder Editor
@author: Andreas
Task B
1. Design and deploy an application in python that generates random numbers. From a
menu the user can choose the desired distribution of probability (at least 2 from below), the
interval. After generating a set of numbers show a graphic to compare it with the desired output.
"""

# import the ditributions
from scipy.stats import uniform, norm, binom
# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})

'''
The method generates a given number of random numbers between given parameters
using the uniform distribution.
Input: @start - the left side of the interval <integer>
       @end   - the right side of the interal <integer>
       @n     - the number of numbers that will be generated <integer>
Output:
'''
def useUniformDistribution(start,end,n):
    data_uniform = uniform.rvs(size=n,loc=start,scale=end-start)
    print(data_uniform)
    ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
    ax.set(xlabel='Distribution ', ylabel='Frequency')
 
'''
The method generates a given number of random numbers between given parameters
using the normal distribution.
Input: @start - the left side of the interval <integer>
       @end   - the right side of the interal <integer>
       @n     - the number of numbers that will be generated <integer>
Output:
'''
def useNormalDistribution(start,end,n):
    result = []
    while len(result) < n:
        data_normal = norm.rvs(size=n,loc=start,scale=end-start)
        for i in data_normal:
            if i >= start and i <= end and len(result) < n:
                result.append(i)
    print(result)
    ay = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='red',
                  hist_kws={"linewidth": 15,'alpha':1})
    ay.set(xlabel='Distribution', ylabel='Frequency')
    
'''
The method generates a given number of random numbers between given parameters
using the binomial distribution.
Input: @start - the left side of the interval <integer>
       @end   - the right side of the interal <integer>
       @n     - the number of numbers that will be generated <integer>
Output:
'''
def useBinomialDistribution(start,end,nr):
    result = []
    while len(result) < nr:
        data_binom = binom.rvs(n=end,p=0.75,size=nr)
        for i in data_binom:
            if i >= start and i <= end and len(result) < nr:
                result.append(i)
    print(result)
    ax = sns.distplot(result,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
    ax.set(xlabel='Distribution', ylabel='Frequency')

while True:
    start = input("Enter the left side of the interval>> ")
    end   = input("Enter the right side of the interval>> ")
    nr    = input("Enter the number of random numbers you want to generate>> ")
    print("Now choose the distribution you want to use in order to get the random numbers:")
    distribution = input("Enter 0 : exit\nEnter 1 for uniform distribution\nEnter 2 for binomial distribution\nEnter 3 for normal distribution")
    if distribution == "1":
        print("The program will generate " + nr + " numbers from " + start + " to " + end + " using uniform distribution:")
        useUniformDistribution(int(start),int(end),int(nr))
    if distribution == "2":
        print("The program will generate " + nr + " numbers from " + start + " to " + end + " using binomial distribution:")
        useBinomialDistribution(int(start),int(end),int(nr))
    if distribution == "3":
        print("The program will generate " + nr + " numbers from " + start + " to " + end + " using normal distribution:")
        useNormalDistribution(int(start),int(end),int(nr))
    break    
        
