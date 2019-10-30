import random, numpy, math, copy, matplotlib.pyplot as plt
nodes = 40
cities = [random.sample(range(100), 2) for x in range(nodes)];
tour = random.sample(range(nodes),nodes);
for temperature in numpy.logspace(0,5,num=100000)[::-1]:
 [i,j] = sorted(random.sample(range(nodes),2));
 newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:];
 oldDistances = sum([math.sqrt(sum([(cities[tour[(k + 1) % nodes]][d] - cities[tour[k % nodes]][d]) ** 2 for d in [0, 1]])) for k in [j, j - 1, i, i - 1]])
 newDistances = sum([math.sqrt(sum([(cities[newTour[(k + 1) % nodes]][d] - cities[newTour[k % nodes]][d]) ** 2 for d in [0, 1]])) for k in [j, j - 1, i, i - 1]])
 if math.exp((oldDistances - newDistances) / temperature) > random.random():
     tour = copy.copy(newTour);
plt.plot([cities[tour[i % nodes]][0] for i in range(nodes+1)], [cities[tour[i % nodes]][1] for i in range(nodes+1)], 'xb-');
plt.show()