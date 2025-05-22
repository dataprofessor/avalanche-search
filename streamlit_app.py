import streamlit as st

st.title("❄️ Using Snowflake in Streamlit Community Cloud")

# Connect to Snowflake
conn = st.connection("snowflake")
prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
  
if st.button("Submit", type='primary'):
  response = conn.query(f"SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', '{prompt}') as RESPONSE;")
  response_value = response.loc[0, 'RESPONSE']
  st.code(response_value, language=None)
