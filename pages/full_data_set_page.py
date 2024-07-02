import streamlit as st
import pandas as pd
from pages.modules.df_location import df_csv_path

df_display_cols = ['seller','Name','country_final','subregion_final','micro_final','Flavor Notes','process_type','fermentation','Varietal Cleaned','first_date_observed','expired','quality_prediction']


@st.cache_data
def load_front_page_data(csv_path):
    in_df = pd.read_csv(csv_path,index_col=0)
    out_df = in_df[df_display_cols].copy()
    col_renames = {'country_final':'Country',
                   'seller':'Seller',
                   'sub_region_final':'Region(s)',
                   'micro_final': 'Micro Location',
                   'process_type': 'Process',
                   'Varietal Cleaned': 'Varietal(s)',
                   'fermentation':'Fermented?',
                   'first_date_observed':'Date First Seen',
                   'expired':'Expired?',
                   'quality_prediction':'Predicted Coffee Review Range'}
    out_df.rename(columns=col_renames, inplace=True)
    return out_df

def full_data_page(csv_path):
    df_filtered = load_front_page_data(csv_path)
    st.header('Data Overview')
    st.write("Below you will find the full data set. You can filter the data by selecting values in the sidebar. The data will update as you select filters. You can sort the data by clicking on the column headers. You can resize the columns by draagging them and resize the data frame by dragging the bottom right corner.")

    # Add filters
    columns_to_filter = ['Country', 'Seller','Process','Expired?']
    filters = {}
    for column in columns_to_filter:
        filters[column] = st.sidebar.multiselect(f'{column}', df_filtered[column].unique())
    
    # Apply filters, the data needs to update as a filter is selected    
    for column, values in filters.items():
        if values:
            df_filtered = df_filtered[df_filtered[column].isin(values)]
    
    selectable = st.dataframe(df_filtered,
                 selection_mode='single-row',
                 on_select='rerun')
    
    if len(selectable.selection.rows) > 0:
        st.session_state.ind = selectable.selection.rows[0]
        if st.button(label='Click here for more information on your selected coffee'):
            st.switch_page('pages/individual_coffee_page.py')
    else:
        st.button(label='Select a coffee to see more information',disabled=True)

full_data_page(df_csv_path)