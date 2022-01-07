import plotly.figure_factory as  ff, statistics,pandas as pd, csv,plotly.graph_objects as go,random

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)
print(mean,std)

fig = ff.create_distplot([data],["Student_marks"],show_hist = False)
fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean


def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([df],["average"],show_hist = False)
    first_std_start,first_std_end = mean - std, mean + std
    second_std_start,second_std_end = mean -(2*std), mean + (2*std)
    third_std_start,third_std_end = mean -(3*std), mean + (3*std)

    print(first_std_start,first_std_end)
    print(second_std_start,second_std_end)
    print(third_std_start,third_std_end)

    
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

    fig.add_trace(go.Scatter(x=[first_std_start,first_std_start],y=[0,0.17],mode="lines",name="std1"))
    fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="std1"))

    fig.add_trace(go.Scatter(x=[second_std_start,second_std_start],y=[0,0.17],mode="lines",name="std2"))
    fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="std2"))
    
    fig.add_trace(go.Scatter(x=[third_std_start,third_std_start],y=[0,0.17],mode="lines",name="std3"))
    fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="std3"))
    fig.show()

    df = pd.read_csv("data1.csv")
    data = df["Math_score"].tolist()
    mean_of_sample1 = statistics.mean(data)
    print(mean_of_sample1)

    fig = ff.create_distplot([data],["Student_marks"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
    fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.17],mode="lines",name="mean of sample 1"))
    fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="std1"))
    fig.show()

    df = pd.read_csv("data2.csv")
    data = df["Math_score"].tolist()
    mean_of_sample2 = statistics.mean(data)
    print(mean_of_sample2)

    fig = ff.create_distplot([data],["Student_marks"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
    fig.add_trace(go.Scatter(x=[mean_of_sample2,mean_of_sample2],y=[0,0.17],mode="lines",name="mean of sample 2"))
    fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="std1"))
    fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="mean of sample 2"))

    fig.show()

    df = pd.read_csv("data3.csv")
    data = df["Math_score"].tolist()
    mean_of_sample3 = statistics.mean(data)
    print(mean_of_sample3)

    fig = ff.create_distplot([data],["Student_marks"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
    fig.add_trace(go.Scatter(x=[mean_of_sample3,mean_of_sample3],y=[0,0.17],mode="lines",name="mean of sample 3"))
    fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="std3"))
    fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="std3"))
    fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="std3"))
    fig.show()


    z_score = (mean_of_sample1-mean)/std
    print(z_score)
    


def standard_deviation():
    mean = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(100)
        mean.append(set_of_means)

    std = statistics.stdev(mean)
    print("STD: ",std)

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    show_fig(mean_list)

setup()

standard_deviation()



