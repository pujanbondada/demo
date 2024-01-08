import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")
col1,col2 = st.columns(2)
with col1:
  st.subheader("cars>people")
  st.image("./pexels-trace-constant-707046.jpg",caption="anger cars",width=300,use_column_width=True)
  st.write("cars are most beatiful")
with col2:
  st.subheader("bmw cars")
  st.image("./wallpaperflare.com_wallpaper.jpg",caption="bmw cars",width=300,use_column_width=True)
  st.write("these cars are more fast")
