import seaborn as sns
import matplotlib.pyplot as plt


def boxplot(df, column):
    sns.boxplot(data=df, x=df[f"{column}"])
    plt.title(f"Boxplot of coordinate  {column}")
    plt.show()

    plt.scatter(df['x'], df['y'],color = "r", s = 50)
    plt.grid()
    plt.title("Umfeld");
    plt.show()

    import plotly.express as px

    # plotting scattered graph
    fig = px.scatter([i for i in range(len(df['z']))], y=df['z'])
    fig.show()



    anomalies = df[df['ifor-Outlier'] == -1]
    # importing the plot
    import plotly.graph_objects as go

    # plotting the graph for outliers
    normal = go.Scatter(x=df.index.astype(str), y=df['z'], name="Dataset", mode='markers')
    outlier = go.Scatter(x=anomalies.index.astype(str), y=anomalies['z'], name="Anomalies", mode='markers',
                         marker=dict(color='red', size=6,
                                     line=dict(color='red', width=1)))
    # labeling the graph
    layout = go.Layout(title="Isolation Forest", yaxis_title='Price', xaxis_title='x-axis', )

    # plotting
    data = [normal, outlier]
    fig = go.Figure(data=data, layout=layout)
    fig.show()

    # importing the module
    import seaborn as sns

    # setting the size of plotting
    sns.set(rc={'figure.figsize': (15, 8)})

    # plotting bar plot
    sns.countplot(df['outlier'])
    plt.show()
