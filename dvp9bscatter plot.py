import plotly.express as px

# Load the Iris dataset
df = px.data.iris()

# Create a 3D scatter plot
fig = px.scatter_3d(
    df,
    x="petal_length",
    y="petal_width",
    z="sepal_length",
    color="species",
    title="3D Scatter Plot of Iris Dataset"
)

fig.update_layout(
    scene=dict(
        xaxis_title="Petal Length",
        yaxis_title="Petal Width",
        zaxis_title="Sepal Length"
    )
)

fig.show()