import matplotlib.pyplot as plt
import numpy as np

x = [10000,20000,30000,40000,50000]
# increasing
ins1 = [59996,119996,179994,239994,299996]
sele1 = [150055001,600110001,1350165001,2400220001,3750275001]
plt.title("increasing")
# plt.plot(x, ins1)
# plt.plot(x, sele1)
# plt.show()

# decreasing
# ins1 = [200039994,800079996,1800119995,3200159997,5000199996]
# sele1 = [177055001,700110001,1575165001,2800220003,4375275002]
# plt.title("decreasing")

# random
# ins1 = [100833779,401695771,897168975,1602276572,1882474183]
# sele1 = [150132718,600277774,1350430897,2400584444,3750745744]

plt.plot(x, ins1, label="insertion sort")
plt.plot(x, sele1, label="selection sort")
leg = plt.legend(loc='upper center')
plt.show()