import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("archiva.csv")
target = 'bug'
numeric_cols = df.select_dtypes(include='number').columns.tolist()

st.title("Bug Prediction Dashboard 📊")
st.write("Visualize how each metric relates to bug occurrence.")

# Distribution of Bug Labels
st.subheader("Bug Label Distribution")
fig, ax = plt.subplots()
sns.countplot(data=df, x=target, ax=ax)
st.pyplot(fig)

# Boxplots
st.subheader("Metric vs Bug")
selected_metric = st.selectbox("Choose a metric:", numeric_cols)
fig2, ax2 = plt.subplots()
sns.boxplot(x=target, y=selected_metric, data=df, ax=ax2)
st.pyplot(fig2)

# Correlation Matrix
st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

