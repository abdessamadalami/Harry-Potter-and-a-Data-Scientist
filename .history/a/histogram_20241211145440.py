import matplotlib.pyplot as plt
import numpy as np
import describe
import pandas as pd
import sys

houses = {
	"Ravenclaw": 1,
	"Slytherin": 2,
	"Gryffindor": 3,
	"Hufflepuff": 4
}


def plot_hist(data, col):
	plt.figure()
	plt.title(data.columns[col])
	data = data.to_numpy()
	print(data[0])
	for i in range(1, 5):
		curr_house = []
		for row in data:
			if row[1] == i and not np.isnan(row[col]):
				curr_house.append(row[col])
		plt.hist(curr_house, alpha=0.5)
	plt.show()


if __name__ == "__main__":
	np.set_printoptions(suppress=True)
	try:
		data = pd.read_csv("resources/dataset_train.csv")
	except:
		sys.exit("Error")
	data["Hogwarts House"].replace(houses, inplace=True)
	data = data.select_dtypes('number')
	print( data.head())
	metrics = describe.describe(data.to_numpy())
	print(me)
	metrics = metrics.tolist()

	col = metrics[5].index(min(metrics[5]))
	print(col)
	# plot_hist(data, col)
