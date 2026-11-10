## Most Popular Programming Languages

### Code

```python
import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')

ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

languages_counter = Counter()

for response in lang_responses:
    languages_counter.update(response.split(';'))

languages = []
popularity = []

for item in languages_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.title("Most Popular Languages")
plt.barh(languages, popularity)

plt.xlabel("Number of People Who Use")
plt.tight_layout()
plt.show()
```

### Concepts Learned

1. Reading CSV files using Pandas.
2. Extracting columns from a DataFrame.
3. Using `Counter()` to calculate frequencies.
4. Using `update()` to count language occurrences.
5. Using `most_common(15)` to find the top 15 languages.
6. Using `reverse()` to reverse list order.
7. Creating horizontal bar charts using `plt.barh()`.
8. Customizing charts using titles and axis labels.