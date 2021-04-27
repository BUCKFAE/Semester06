"""Mittelwert, Median, Varianz und Standardabweichung"""

import math

nums = sorted([15, 150, 12, 8, 65, 8, 34, 42])
print("Numbers: %s" % nums)


mean = sum(nums) / len(nums)
median = (nums[(len(nums) - 1) // 2] + nums[(len(nums) - 1) // 2 + 1]) / 2
variance = 1 / (len(nums) - 1) * sum([(n - mean) ** 2 for n in nums])
standard_deviation = math.sqrt(variance)

print("Mean: %s" % mean)
print("Median: %s" % median)
print("Variance: %s" % variance)
print("Standard deviation: %s" % standard_deviation)
