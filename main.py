import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris

# لازم تكون أول دالة Streamlit
st.set_page_config(
    page_title="iris_project",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🦈"
)

# دالة مؤقتة للتنبؤ
def predict(x1, x2, x3, x4):
    return "Setosa"

st.header(":blue[Welcome to my application iris project]")

st.title("Iris Project")

st.write("This is a simple web application built using Streamlit to demonstrate the Iris dataset analysis and visualization.")
st.write("The Iris dataset is a classic dataset in machine learning and statistics, containing measurements of iris flowers from three different species.")

st.write("Petal Length : The length of the petal in centimeters.")
st.write("Petal Width : The width of the petal in centimeters.")
st.write("Sepal Length : The length of the sepal in centimeters.")
st.write("Sepal Width : The width of the sepal in centimeters.")

st.caption("This is a string that explains something above.")

# تحميل البيانات
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# عرض البيانات
if st.button("Show Iris Dataset"):
    st.write("Here is the Iris dataset:")
    st.write(df)

# ملخص البيانات
if st.button("Show Iris Dataset Summary"):
    st.write("Here is the summary of the Iris dataset:")
    st.write(df.describe())

# الرسوم البيانية
st.header("Iris Dataset Visualization")

tab1, tab2, tab3 = st.tabs(["Line Chart", "Scatter Chart", "Bar Chart"])

with tab1:
    st.line_chart(
        df,
        x="sepal length (cm)",
        y="sepal width (cm)",
        use_container_width=True,
    )

with tab2:
    st.scatter_chart(
        df,
        x="sepal length (cm)",
        y="sepal width (cm)",
        use_container_width=True,
    )

with tab3:
    st.bar_chart(
        df,
        x="sepal length (cm)",
        y="sepal width (cm)",
        use_container_width=True,
    )

# التنبؤ
st.header("Iris Species Prediction using Sliders")

x1 = st.slider("PETAL WIDTH", 0.0, 10.0, 1.0, step=0.1)
x2 = st.slider("PETAL LENGTH", 0.0, 10.0, 1.0, step=0.1)
x3 = st.slider("SEPAL WIDTH", 0.0, 10.0, 1.0, step=0.1)
x4 = st.slider("SEPAL LENGTH", 0.0, 10.0, 1.0, step=0.1)

if st.button("Predict", type="primary"):
    result = predict(x1, x2, x3, x4)
    st.success(f"The predicted iris species is: {result}")