import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title='NAWE DUBAI INTELLIGENCE PLATFORM',initial_sidebar_state='collapsed',layout='wide')
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

	title_alignment="""
	<style>
	#the-title {
	  text-align: center
	}
	</style>
	"""
	st.markdown(no_sidebar_style, unsafe_allow_html=True)
	st.subheader('NAWE DUBAI CONSULTANCY INTELLIGENCE PLATFORM')
	st.markdown("---")

	st.write("*:green[NAWE digital platform is to build a sophisticated program to help both the clients and the service provider (NAWE Dubai) to reach a design solution in an efficient and cost-effective manner. To achieve this goal some parameters have been selected that must be addressed by the client to evaluate the state of the project. The parameters contributes to the execution process of the project work assigned to the service provider.]* ")
	st.markdown("---")

	country= st.selectbox("Select Country",options=["","Sweden","Denmark","Norway","USA","UAE","Singapore","Finland","Canada"])
	if country=='Sweden':
			if st.button('Next :arrow_forward:'):
				switch_page('instruction')
	elif country== '':
		  st.write("*:red[Please Select the country.. ]*")
	else:
		  st.write("*:red[Service for your country is upcoming. Please stay tuned. ]*")