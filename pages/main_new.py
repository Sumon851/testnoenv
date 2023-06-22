'''Fardini Khandaker
fardini@nawe.ae'''

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
	st.markdown(no_sidebar_style, unsafe_allow_html=True)
	st.header('NAWE DUBAI CONSULTANCY INTELLIGENCE PLATFORM')
	st.markdown("---")
	#st.subheader('please select following criteria to estimate budget
	df1=pd.read_excel('budget-fk.xlsx',sheet_name='Sheet1')
	df_area=pd.read_excel('budget-fk.xlsx',sheet_name='ST-1')
	df_area=df_area.fillna(' ')


	x=st.selectbox('Please specify your project area',options=df_area['Rate'].unique())

	final_df=pd.DataFrame(columns=df_area.columns)
	def main_col(a):

			df=pd.read_excel('budget-fk.xlsx',sheet_name=a)
			df=df.fillna(' ')
			df.index=df.Rate
			df=df.drop(columns='Rate')
			constant_df=df.loc[[x]]
			return constant_df
	main_service=['Stormwater','Water','Sewer'] ###main services

	###list of subservice under main services
	subsevrice=[['Stormwater investigation for detailed plan area','Stormwater investigation for building permit','Stormwater investigation for existing properties','1D stormwater pipe network modelling','Flood investigation (1D-2D overland runoff and pipe modelling)','Stormwater pipe network design'
	],['Water distribution network modelling','Water hammer analysis','Existing water distribution network investigation','Water pipe network design'],['Existing sewer network investigation (gravity and  pressure sewer system)','Sewer network modelling','Sewer network design']]

	selection=[]
	columns=st.columns(3)
	if x==' ':
		st.write(':red[Please select area first]')
	else:
		for i,name in enumerate(main_service):
			with columns[i]:


				st.header(name)
				st.divider()
				a=st.multiselect(f'**:red[Select a service under { name}]**',options=subsevrice[i])[:]
				selection.append(a)

				print(selection)
		selection_flat = [item for sublist in selection for item in sublist]

		#print(selection_flat)
		budget=[]
		final_df=pd.DataFrame()


		for item in selection_flat:
			a=df1['Sheet'].loc[df1['Sub service']==item].values[0]
			print(a)
			constant_df=main_col(a)
			print(constant_df)
			final_df=pd.concat([final_df,constant_df],ignore_index=True)


		final_df['services']=selection_flat

		final_df['area']=x

		final_df.to_excel('new.xlsx',index=False)




		if not selection_flat==[]:
			if st.button('NEXT :arrow_forward:'):
				switch_page('web_app_new')




