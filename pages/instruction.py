import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='NAWE DUBAI CONSULTANCY INTELLIGENCE PLATFORM',initial_sidebar_state='collapsed',layout='wide')
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

	st.write(":blue[To get quotation for a specific service , it is a prerequisite to gather few information regarding the project area . A brief description of the required details are given below. Please read them carefully and ensure that the necessary information is available to you before proceeding. ]")
	st.markdown("---")
	st.subheader("Lowest groundwater level: ")
	st.write("The location and probable fluctuation of the groundwater level is of utmost importance. This can directly impact the design and execution process of a project. So, for primary evaluation of a project the NAWE digital platform needs the input of lowest groundwater level from ground, in meter unit, recorded in the project area.")

	st.subheader("Total project area:")
	st.write("The size of the project area is an important variable by which we can get an idea of the vastness and extent of the project. Thus, to evaluate a project we need the client to define the total project area in hectare unit. ")

	st.subheader("Protected land:")
	st.write("The existence of any historic and environmentally protected land can shift the thinking process and outcome of any project. To know about the protected lands in the area beforehand can save a lot of time and money during the project period. The client must address the area of the protected land(s), if present inside the project area, in hectare unit to help the evaluation of the project. ")
	st.subheader("Level difference:")
	st.write("To provide an efficient solution for a project we need a clear concept of the terrain of the project area. Different terrains can contribute to the complexity of the project. The client must input the level difference between the highest and lowest point of the project area to help the platform evaluate the terrain.")
	st.subheader("Land-use (for planned areas):")
	st.write("Planned land use can give us a preliminary concept of the type of development that is planned to occur in the project area. Every project must be analyzed and designed in a different manner, given its planned land use. Here the planned land use signifies a gross estimation to help us evaluate the type of planned development. Client can select the planned land use from a dropdown in the NAWE digital platform.")
	st.subheader("Development status (for existing areas):")
	st.write("The current development status of the project area is another important parameter which is essential for any project. Existing development and its extent can introduce a lot of complexity into a design. The client must provide an estimate of the development currently present in the project area.")

	st.subheader("Population:")
	st.write("The target population for the project plays a significant role in the analysis and design. If the project is to investigate an existing area, then the client must input the current population of the area in investigation. And if the project scope is to design a system for the future, then the client must input the target population in this segment.")
	st.subheader("Soil type:")
	st.write("Soil type is one of the most important parameters for any kind of investigation, design, and construction. Client must input the soil types and their extents in the platform to make the preliminary evaluation of the area possible.")
	st.subheader("Development status (for planned areas): ")
	st.write("The planned development status after the project completion can provide an idea of the changes in the area and the final condition of the project area. The client must select the level of development that is planned for the project area.")
	st.subheader("Project stage:")
	st.write("A project evolves through several stages before completion. We can consider them as investigation stage (feasibility study), Design stage (SH, BH), execution etc. Knowing the stage of the project helps to define the scope of the project. This is an important parameter that the client must input in the platform.")

	st.subheader("Climate zones: ")
	st.write("Areas of every different climate zone have adopted a different approach to the design with respect to their specific requirements. This information is vital for the investigation and design process of the project. The client must input the climate zone which the project area falls within.")
	st.subheader("Involvement of other consultants: ")
	st.write("Involvement of multiple consultants can greatly impact on the timeframe of the project as well as the cost. As we believe in providing integrated solutions for engineering problems, communication and input from different disciplines is a must. So, it is a must for the client to declare the involvement of other consultants, if any.")
	st.subheader("Stormwater pipe network length: ")
	st.write("The approximate length of the stormwater pipe network can help the evaluation of the project. The cost of such a project is always correlated with the length of the stormwater pipe network and the complexity of the network. The client must input an estimated length of the stormwater pipe network to help the platform to evaluate the project.")
	st.subheader("Recipient close to project area: ")
	st.write("For stormwater investigation and design, we need to evaluate the nearest or closest recipient of stormwater. This input from the client can help the evaluation process a lot. In this platform, the client must input the name of the closest recipient of stormwater from the project area.")
	if st.button('Next :arrow_forward:'):
				switch_page('main_new')
