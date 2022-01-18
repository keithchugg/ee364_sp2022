
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def p_clash(k):
    p = 1
    for i in range(k):
        p = p * (365 - i) / 365
    return 1 - p


N_students = 60

## probabiliy of no common b-days in class of size k: (365/365)*(364/365)*(363/365) ... ((365 - k + 1)/365)
p_clashes = np.zeros(N_students)
for k in range(N_students):
    p_clashes[k] = p_clash(k + 1)

plt.figure()
plt.plot(np.arange(N_students) + 1, p_clashes)
plt.axhline(y = 0.5, c = 'r', linewidth = 2)
plt.axvline(x=23, c='r')
ax = plt.gca()
ax.set_xlabel('class size (k)')
ax.set_ylabel('probability common birthday')
plt.title('Birthday Paradox: with 23 or more people, clashed more probable than not')