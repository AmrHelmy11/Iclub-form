import streamlit as st
import sqlite3
import pandas as pd
import os

# Function to create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('ihub.db')  # Create or connect to the database
    return conn

# Function to create the table if it doesn't exist
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone number INTEGER NOT NULL,
            id INTEGER NOT NULL,
            faculty TEXT NOT NULL,
            year INTEGER NOT NULL,
            email TEXT NOT NULL,
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(name, phone_number, id, faculty, year, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, phone_number, id, faculty, year, email) VALUES (?, ?, ?, ?, ?, ?)', (name, phone_number, id, faculty, year, email))
    conn.commit()
    conn.close()

# Function to save data to a CSV file
def save_to_csv(data):
    # Check if the CSV file exists
    if os.path.exists('_ihub_.csv'):
        # If it exists, append the new data
        existing_data = pd.read_csv('_ihub_.csv')
        updated_data = pd.concat([existing_data, data], ignore_index=True)
        updated_data.to_csv('_ihub_.csv', index=False)
    else:
        # If it doesn't exist, create a new one
        data.to_csv('_ihub_.csv', index=False)

# Create the table
create_table()

# Streamlit form
st.title("User  Data Entry Form")

with st.form(key='data_form'):
    name = st.text_input("Name")
    phone_number = st.number_input("phone number", min_value=0)
    id = st.number_input("id", min_value=0)
    faculty = st.text_input("faculty")
    year = st.number_input("year", min_value=0, max_value=7)
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Insert the data into the database
        insert_data(name, phone_number, id, faculty, year, email)

        # Create a DataFrame from the input data
        data = pd.DataFrame({
            'Name': [name],
            'Phone Number': [phone_number],
            'ID': [id],
            'Faculty': [faculty],
            'Year': [year],
            'Email': [email],
        })

        # Save the data to CSV
        save_to_csv(data)

        st.success("Data saved successfully!")


