import pandas as pd
import streamlit as st



from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title='NAWE DUBAI INTELLIGENCE PLATFORM',initial_sidebar_state='collapsed',layout='wide')
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

st.header('NAWE DUBAI INTELLIGENCE PLATFORM')
st.subheader('please provide following information')

df = pd.read_excel('factor.xlsx', sheet_name='Sheet1')
factors = pd.read_excel('factor.xlsx', sheet_name='factor_sheet')
print(df.columns)
df = df.fillna(' ')
final_df = pd.read_excel('new.xlsx')
services = final_df.services.unique()
sheet = []
coln_list = []
q_list = []
x = []
help_list = []

try:
    for coln, c in enumerate(df.columns):
        if not c.startswith('f'):
            if not c.startswith('help'):
                # print(coln,c)

                coln_list.append(coln)
                q_list.append(c)
            else:
                help_list.append(df['c'][:])
                print(help_list)


    def filter_criteria(q_list):
        for i, q in enumerate(q_list):

            if len(x) == 0:

                bar = st.selectbox(" {}".format(q), options=(df[str(q)].unique()), help=help_list[i])
            else:
                bar = st.selectbox(" {}".format(q), options=(df[str(q)].unique()))
            x.append(bar)

            if len(x) == 9:
                expander = st.expander('*:red[See climate zone map]*')

                expander.image('climate_zone.png')


    filter_criteria(q_list)
    total_f = []
    # x=['<1','1-3','1-5']
    df1 = pd.DataFrame()
    # def selectionq(x):

    for i in range(len(q_list)):
        # print('q_list', q_list)
        # print(df[q_list[i]])
        df1 = df.loc[df[q_list[i]] == x[i]]

        total_f.append(df1.iloc[:, coln_list[i] + 1].values[0])
    print(total_f)

    landuse = ['', 'agriculture', 'office', 'industry', 'school', 'residential', 'commercial', 'block']
    option = [' ', '0-10', '11-30', '31-50', '51-100', '101-200', '201-350', '351-500', '501-700', '701-1000', '>1000'
              ]
    option_block = [' ', '0-2', '3-5', '6-10', '11-20', '21-35', '36-50', '51-65', '66-80', '81-100', '>100']

    factor = ['0', '0.2', '0.5', '1', '1.5', '2.1', '2.8', '3.6', '4.5', '6', '10']

    landuse = st.selectbox(
        'What is the landuse in the area? Please choose from the follwing options. If landuse is mixed, select- *:blue[block]* ',
        options=landuse
        ,
        help='Planned land use can give us a preliminary concept of the type of development that is planned to occur in the project area. Every project must be analyzed and designed in a different manner, given its planned land use. Here the planned land use signifies a gross estimation to help us evaluate the type of planned development. Client can select the planned land use from a dropdown in the NAWE digital platform.')
    if not landuse == '':
        if landuse == 'block':
            block = st.selectbox('Number of block/ property', options=option_block, key='landuse1')
            index = option_block.index(block)
            f = float(factor[index])
        else:
            use = st.selectbox(f'Area of {landuse} (st)', options=option, key='landuse2')
            index = option.index(use)
            f = float(factor[index])
    st.write('Soil information')
    # expander=st.expander('i')
    help_soil = (
        'Soil type is one of the most important parameters for any kind of investigation, design, and construction. Client must input the soil types and their extents in the platform to make the preliminary evaluation of the area possible.')


    def soil_q():
        soils = ['Filling material (no contamination)', 'Sand', 'Gravel', 'Rock', 'Silt', 'Clay', 'Peat',
                 'Filling material (contaminated)']
        factor_soil = ['0.02', '0.03', '0.05', '0.075', '0.1', '0.15', '0.2', '0.5']
        number_fruits = []
        top = []
        max_value = None

        col = st.columns(len(soils[:3]), gap='small')
        col2 = st.columns(len(soils[3:]), gap='small')
        for idx, types in enumerate(soils):

            if idx < 3:
                number = col[idx].number_input(f'{types} %', max_value=max_value, help=help_soil)
            else:
                number = col2[idx - 3].number_input(f'{types} %', help=help_soil)

            top.append(number * float(factor_soil[idx]))
            number_fruits.append(number)

            if sum(number_fruits) == 100:
                break
        soil_sum = sum(top) / 100
        return soil_sum


    soil_sum = soil_q()
    print('soil and land', soil_sum, f)
    final_df['factor'] = ' '
    for s in services:
        factor_range = int(factors['range'].loc[factors['Sub service'] == s].values[0])
        print(factor_range)
        factor_sum = sum(total_f[:factor_range]) + f + soil_sum

        final_df['factor'].loc[final_df['services'] == s] = factor_sum
    final_df['base_factor'] = final_df['Base Amount in SEK/hr'] * final_df['factor']

    final_df.to_excel('new.xlsx', index=False)
except:
    st.write(':red[Please select all the above boxes]')
else:
    if st.button('NEXT   :arrow_forward:  '):
        switch_page('final')



