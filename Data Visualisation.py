import pandas as pd

data = pd.read_csv("Data Sales3.csv", delimiter = ";")
print(data.head(10))


# Scater Plot
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.scatter(data['Category'], data['Quantity'])
plt.title("Test")
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
plt.show()


# Line Chart

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.plot(data['Category'])
plt.plot(data['Quantity'])
plt.title("Test")
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.savefig('line.png', dpi=300, bbox_inches='tight')
plt.show()


# Bar Chart
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.bar(data['Category'], data['Quantity'])
plt.title("Test")
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.savefig('bar.png', dpi=300, bbox_inches='tight')
plt.show()


# Histogram
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.hist(data['Category'])
plt.title("Histogram")
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
plt.show()


# Pie Chart
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")
sales = ['Category', 'Quantity']
datasales = [23, 10]

plt.pie(datasales, labels=sales)
plt.title("Sales Data")
plt.savefig('pie.png', dpi=300, bbox_inches='tight')
plt.show()