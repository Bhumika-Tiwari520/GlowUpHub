
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date

st.set_page_config(page_title='Aura AI', page_icon='💜', layout='wide')

st.markdown('''
<style>
.stApp{background:linear-gradient(180deg,#050816,#0b1020);}
</style>
''', unsafe_allow_html=True)

st.session_state.setdefault('chat', [])
st.session_state.setdefault('journal', [])

st.sidebar.title('💜 Aura AI')
page = st.sidebar.radio('Navigation',['Dashboard','AI Chat','Mood Journal','Burnout Detector','Study Balance','Focus Mode','Safety Tools','Wellness Hub','Progress Insights','Achievements','Settings'])

if page=='Dashboard':
    st.title('💜 Aura AI Dashboard')
    c1,c2,c3,c4=st.columns(4)
    c1.metric('Mood','84%')
    c2.metric('Focus','78%')
    c3.metric('Balance','81%')
    c4.metric('Stress','32%')

elif page=='AI Chat':
    st.title('🤖 Offline Chatbot')
    for r,m in st.session_state.chat:
        st.write(f'**{r}:** {m}')
    msg = st.chat_input('Type here')
    if msg:
        st.session_state.chat.append(('You',msg))
        st.session_state.chat.append(('Aura AI','You are doing great. Keep moving forward 💜'))
        st.rerun()

elif page=='Mood Journal':
    st.title('📔 Mood Journal')
    mood=st.selectbox('Mood',['Happy','Calm','Anxious','Stressed','Sad'])
    txt=st.text_area('Entry')
    if st.button('Save'):
        st.session_state.journal.append({'Mood':mood,'Entry':txt})
    if st.session_state.journal:
        st.dataframe(pd.DataFrame(st.session_state.journal))

elif page=='Burnout Detector':
    st.title('🔥 Burnout Detector')
    sleep=st.slider('Sleep',0,12,6)
    score=max(0,min(100,(8-sleep)*10))
    fig=go.Figure(go.Indicator(mode='gauge+number',value=score))
    st.plotly_chart(fig,use_container_width=True)

elif page=='Study Balance':
    st.title('📚 Study Balance')
    st.metric('NDA Countdown',(date(2027,4,15)-date.today()).days)

else:
    st.title(page)
