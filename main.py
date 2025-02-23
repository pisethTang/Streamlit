import streamlit as st 
import pandas as pd 
import altair as alt 
import numpy as np 


st.write('Hello, world! :sunglasses:')
st.write(1234)
st.write("Below is a dataframe: ",
    pd.DataFrame({
        "first column": [1,2,3,4],
        "second column": [10,20,30,40],
    }),
    "Above is a dataframe"
)


st.write(
    *[1,2,3,4,5]
)

st.write({
    1: "a",
    2: "ad",
    3: "af",
    4: "ag",
})


st.write("1 + 1 = ", 2)


df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)