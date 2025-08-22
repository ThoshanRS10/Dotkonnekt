
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set plot style
sns.set_theme(style="whitegrid")

def plot_histogram(df, column):
    fig = px.histogram(df, x=column, title=f"Distribution of {column}")
    return fig

def plot_bar(df, column):
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, 'count']
    fig = px.bar(counts, x=column, y='count', title=f"Count of {column}")
    return fig

def plot_scatterplot(df, x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs. {x_col}", trendline="ols")
    return fig

def plot_heatmap(df):
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        corr = numeric_df.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        return fig
    return None

# Custom Visualization (Innovation Requirement)
def plot_geo_map(df, lat_col, lon_col, color_col=None):
    fig = px.scatter_geo(df,
                         lat=lat_col,
                         lon=lon_col,
                         color=color_col,
                         hover_name=color_col,
                         projection="natural earth",
                         title="Geographic Data Distribution")
    return fig

