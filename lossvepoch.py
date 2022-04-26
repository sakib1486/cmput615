import matplotlib.pyplot as plt
import json

#read file
j = open("1500epoch/metrics.json", "r")

js = j.readlines()

iterations = list()
losses = list()

for obj in js:
	res = json.loads(obj)
	iterations.append(res['iteration'])
	losses.append(res['total_loss'])

zipped_list = zip(iterations, losses)
sorted_pairs = sorted(zipped_list)

tuples = zip(*sorted_pairs)

iterations, losses = [list(tup) for tup in tuples]

#plotting

f = plt.figure()
f.set_figwidth(4)
f.set_figheight(4)
plt.plot(iterations, losses)
plt.title("1500 Epochs")
plt.xlabel("Iterations")
plt.ylabel("Total Loss")
plt.show()
