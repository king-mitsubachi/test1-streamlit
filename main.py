import streamlit as st
import numpy as np
import pandas as pd


st.title('streamlit 超入門')
st.write('dataflame')

df = pd.DataFrame(
    np.random.rand(100, 2)/ [40, 40] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

"""
```python
st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=500,height=500)
```
"""
