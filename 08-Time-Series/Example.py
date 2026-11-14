import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('seaborn-v0_8')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot(dates, y, marker='o', linestyle='solid')

plt.gcf().autofmt_xdate()

# plt.title('Date vs Values')
# plt.xlabel('Date')
# plt.ylabel('Values')

plt.tight_layout()
plt.show()