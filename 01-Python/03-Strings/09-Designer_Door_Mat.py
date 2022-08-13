# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use | , . and - characters.


# Sample Design

# Size: 7 x 21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

# Size: 11 x 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------

# Input Format
# A single line containing the space separated values of M and N.

# Constraints
# 5<N<101
# 15<M<300

# Sample Code

N, M = input().split()
N = int(N)
M = int(M)

for i in range(1, N, 2):
    print((".|."*i).center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(N-2, -1, -2):
    print((".|."*i).center(M, "-"))
