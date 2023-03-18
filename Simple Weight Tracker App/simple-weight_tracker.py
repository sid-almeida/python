import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = 'weight.csv'
APP_TITLE = 'Weight Tracking'


def main():
    st.set_page_config(page_title=APP_TITLE)

    st.sidebar.title(APP_TITLE)

    menu_options = ['Add New Weight', 'View Weight History']
    menu_selection = st.sidebar.radio('Menu', menu_options)

    if menu_selection == 'Add New Weight':
        add_new_weight()
    elif menu_selection == 'View Weight History':
        view_weight_history()


def add_new_weight():
    st.header('Add New Weight')

    with st.form(key='weight_form'):
        weight = st.text_input('Weight (kg):')
        date = st.text_input('Date (yyyy-mm-dd):')

        submit_button = st.form_submit_button(label='Add Weight')

    if submit_button and validate_weight(weight) and validate_date(date):
        weight_data = {'date': [date], 'weight': [float(weight)]}
        df = pd.DataFrame(data=weight_data)

        if file_exists(FILE_NAME):
            df.to_csv(FILE_NAME, mode='a', header=False, index=False)
        else:
            df.to_csv(FILE_NAME, index=False)

        st.success('Weight added successfully.')


def view_weight_history():
    st.header('View Weight History')

    if file_exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        st.dataframe(df)

        plt.plot(df['date'], df['weight'])
        plt.xlabel('Date')
        plt.ylabel('Weight (kg)')
        plt.title('Weight History')
        st.pyplot()
    else:
        st.warning('No weight data found.')


def validate_weight(weight):
    if not weight:
        st.warning('Please enter a weight.')
        return False

    try:
        float(weight)
    except ValueError:
        st.warning('Please enter a valid weight.')
        return False

    return True


def validate_date(date):
    if not date:
        st.warning('Please enter a date.')
        return False

    try:
        pd.to_datetime(date)
    except ValueError:
        st.warning('Please enter a valid date in the format yyyy-mm-dd.')
        return False

    return True


def file_exists(file_name):
    try:
        pd.read_csv(file_name)
    except FileNotFoundError:
        return False

    return True
st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == '__main__':
    main()
