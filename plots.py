from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt

all_values = []
directory = "/Users/kristen/Desktop/650/"
for i in range(101,108):
    filepath = directory + str(i) + "_total.txt"
    result_dict = eval(open(filepath,"r").readlines()[0])
    all_values = all_values + result_dict.values()


df = pd.DataFrame(all_values, columns = ['cossim'])

plot = df.plot(kind = 'density', title = 'cosine-similarity distribution, all topics', legend = False, xlim = (0,0.5), ylim=(-0.1,70.0))
plot.set_xlabel('cosine-similarity')
plot.set_ylabel('frequency')

#plt.savefig('density.jpg')


# plot each individiual topics
for i in range(101,108):
    filepath = directory + str(i) + "_total.txt"
    result_dict = eval(open(filepath,"r").readlines()[0])
    values = result_dict.values()
    title = 'cosine-simalrity disribution, topic ' + str(i-1)
    df = pd.DataFrame(values, columns = ['cossim'])
    plot = df.plot(kind = 'density', title = title, legend = False, xlim = (0,0.5), ylim=(-0.1,70.0))
    plot.set_xlabel('cosine-similarity')
    plot.set_ylabel('frequency')
    out_title = "density_topic" + str(i-1) + ".jpg"
    plt.savefig(out_title)
