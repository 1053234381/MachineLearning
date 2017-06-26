import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv("UNRATE.csv")
unrate = pd.to_datetime(unrate["DATE"])
print(unrate.head(12))
plt.plot()
plt.show()
