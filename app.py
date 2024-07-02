import streamlit as st

st.set_page_config(page_title='Green Coffee in the USA', page_icon='☕️', layout='wide', initial_sidebar_state='expanded')

pages = [st.Page('pages/about_page.py',title='About the Home Greens Project',default=True), 
         st.Page('pages/full_data_set_page.py',title='All Green Coffees'), 
         st.Page('pages/individual_coffee_page.py',title='Individual Coffee Information'), 
         st.Page('pages/fresh_dashboard_page.py',title='Fresh Arrival Dashboard')]


pg = st.navigation(pages,position='sidebar')
pg.run()