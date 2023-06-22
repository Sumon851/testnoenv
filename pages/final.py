	
import streamlit as st 
import pandas as pd
import webbrowser
st.set_page_config(page_title='NAWE DUBAI INTELLIGENCE PLATFORM',initial_sidebar_state='collapsed',layout='wide')
from streamlit_extras.switch_page_button import switch_page
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
if 'user' not in st.session_state:
    st.error('Unauthorized access. Please login.')
    button_choice = st.button('login')
    if button_choice:
        switch_page('login')

else:
	st.markdown(no_sidebar_style, unsafe_allow_html=True)
	st.header('NAWE DUBAI INTELLIGENT PLATFORM')
	st.markdown("---")
	#Logout Button, Should add this to all pages.

	if st.button('Logout'):
		# Clear user session
		del st.session_state['user']
		st.success('Logged out successfully!')

		# Redirect to login page
		switch_page('login')

	st.markdown(no_sidebar_style, unsafe_allow_html=True)

	st.header("Additional requirement")
	df=pd.read_excel('new.xlsx')
	budget=df['base_factor'].sum()

	services=df.services.unique().tolist()

	extra_prompt1=st.multiselect("For which of the following services do you want PM report to be in Swedish?",options=services )
	extra_prompt2=st.multiselect("For which of the services is external meeting required?",options=services )

	TOTAL=[budget]

	PM=0
	EM=0
	if not extra_prompt1==[]:
		for i in extra_prompt1:
			PM+=df['PM (SEK/hr)'].loc[df['services']==i].values[0]




		print(PM)
		TOTAL.append(PM)
	else:
		PM=0

	if not extra_prompt2==[]:

		EM+=6000
		hours=st.slider("How many meetings?",1,20,1)
		EM=EM*hours



		print(EM)
		TOTAL.append(EM)
	else:
		EM=0
	#st.write(budget,budget1)

	st.divider()

	if len(TOTAL)>1:

		st.write('**:red[Final estimated budget', f'SEK {round(budget+PM+EM)}]**')

	else:
		st.write('*:red[Preliminary estimated budget ', f'SEK {round(budget)} ]*')
	st.divider()
	print('PM ', PM, ' EM ', EM)
	df['final_budget']=sum(TOTAL)
	df.to_excel('new.xlsx',index=False)

	df=pd.read_excel('new.xlsx')
	tab=[]
	tabs=['Main tasks','Data requirement','Deliverable','Duration']



	for serv in services:
		st.write(f'**:blue[{serv}]**')
		tab1,tab2,tab3,tab4=st.tabs(tabs)

		with tab1:

			st.write(df['Main tasks'].loc[df['services']==serv].values[0])



		with tab2:
			st.write(df['Data requirement'].loc[df['services']==serv].values[0])
		with tab3:
			st.write(df['Deliverable'].loc[df['services']==serv].values[0])
		with tab4:
			st.write(df['Duration'].loc[df['services']==serv].values[0])


		st.divider()




	if st.button('Home:house: '):
		switch_page('main')
	url = 'https://www.nawebangladesh.com/about-us/'

	if st.button('NAWE Home'):
		webbrowser.open_new_tab(url)