import streamlit as st
import pandas as pd
import sqlite3
import requests
import os

# Initialize the database when the application starts
def initialize_database():
    conn = sqlite3.connect('sales_assistant.db')
    cursor = conn.cursor()

    # Create customers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phone TEXT,
        address_street TEXT,
        address_city TEXT,
        address_state TEXT,
        address_zip TEXT,
        address_country TEXT,
        company_name TEXT,
        job_title TEXT
    )
    """)

    # Create interactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interactions (
        interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        date TEXT,
        type TEXT,
        notes TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
    )
    """)

    # Create sales_information table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_information (
        sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        sales_rep_id INTEGER,
        product_service TEXT,
        sales_stage TEXT,
        estimated_deal_value REAL,
        follow_up_date TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
    )
    """)

    # Create preferences table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS preferences (
        preference_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        preferred_contact_method TEXT,
        preferred_contact_time TEXT,
        additional_notes TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
    )
    """)

    conn.commit()
    conn.close()

def upload_customers(df):
    try:
        conn = sqlite3.connect('sales_assistant.db')
        expected_columns = {'first_name', 'last_name', 'email', 'phone', 'address_street', 'address_city', 'address_state', 'address_zip', 'address_country', 'company_name', 'job_title'}
        df = df[list(expected_columns.intersection(df.columns))]
        df = df.astype(str)
        df.to_sql('customers', conn, if_exists='append', index=False)
        conn.close()
        print("Customers data uploaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def upload_interactions(df):
    try:
        conn = sqlite3.connect('sales_assistant.db')
        expected_columns = {'customer_id', 'date', 'type', 'notes'}
        df = df[list(expected_columns.intersection(df.columns))]
        df = df.astype(str)
        df.to_sql('interactions', conn, if_exists='append', index=False)
        conn.close()
        print("Interactions data uploaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def upload_sales_information(df):
    try:
        conn = sqlite3.connect('sales_assistant.db')
        expected_columns = {'customer_id', 'sales_rep_id', 'product_service', 'sales_stage', 'estimated_deal_value', 'follow_up_date'}
        df = df[list(expected_columns.intersection(df.columns))]
        df = df.astype(str)
        df.to_sql('sales_information', conn, if_exists='append', index=False)
        conn.close()
        print("Sales information uploaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def upload_preferences(df):
    try:
        conn = sqlite3.connect('sales_assistant.db')
        expected_columns = {'customer_id', 'preferred_contact_method', 'preferred_contact_time', 'additional_notes'}
        df = df[list(expected_columns.intersection(df.columns))]
        df = df.astype(str)
        df.to_sql('preferences', conn, if_exists='append', index=False)
        conn.close()
        print("Preferences data uploaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def generate_email(customer_name, product_name):
    prompt = f"Generate a personalized email for {customer_name} about {product_name}."
    url = "https://api.groq.com/openai/v1/chat/completions"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "model": "mixtral-8x7b-32768",
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("choices")[0].get("message").get("content")
    else:
        return "Error generating email."

def get_chatbot_response(user_input):
    url = "https://api.groq.com/openai/v1/chat/completions"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": user_input,
            }
        ],
        "model": "mixtral-8x7b-32768",
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("choices")[0].get("message").get("content")

def schedule_task(task, due_date):
    conn = sqlite3.connect('sales_assistant.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description, due_date) VALUES (?, ?)", (task, due_date))
    conn.commit()
    conn.close()

# Initialize the database
initialize_database()

# Function to load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load custom CSS file
local_css("style.css")

# Sidebar navigation and main content
st.title("Sales Assistant Application")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload Data", "Schedule Tasks", "CRM Integration", "Chatbot"])

if page == "Home":
    st.header("Welcome to the Sales Assistant Application!")
    st.write("Use the sidebar to navigate through the app.")

elif page == "Upload Data":
    st.header("Upload Data")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt"])

    if uploaded_file is not None:
        try:
            if uploaded_file.type == 'text/plain':
                df = pd.read_csv(uploaded_file, sep="\t")
            else:
                df = pd.read_csv(uploaded_file)

            st.write("Uploaded data:")
            st.write(df)

            option = st.selectbox(
                'Which data are you uploading?',
                ('Customers', 'Interactions', 'Sales Information', 'Preferences')
            )

            if st.button("Upload"):
                if option == 'Customers':
                    upload_customers(df)
                    st.success("Customers data uploaded successfully!")
                elif option == 'Interactions':
                    upload_interactions(df)
                    st.success("Interactions data uploaded successfully!")
                elif option == 'Sales Information':
                    upload_sales_information(df)
                    st.success("Sales information uploaded successfully!")
                elif option == 'Preferences':
                    upload_preferences(df)
                    st.success("Preferences data uploaded successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

elif page == "Schedule Tasks":
    st.header("Schedule Tasks")
    task = st.text_input("Task Description")
    due_date = st.date_input("Due Date")

    if st.button("Schedule Task"):
        schedule_task(task, due_date)
        st.success("Task scheduled successfully!")

    customer_name = st.text_input("Customer Name")
    product_name = st.text_input("Product Name")

    if st.button("Generate Email"):
        email_content = generate_email(customer_name, product_name)
        st.write(email_content)

elif page == "CRM Integration":
    st.header("CRM Integration")
    crm_option = st.selectbox("Choose CRM", ["Salesforce", "HubSpot", "Zoho"])

    if st.button("Integrate CRM"):
        st.success(f"{crm_option} integrated successfully!")

elif page == "Chatbot":
    st.header("Chatbot")
    st.write("AI Chatbot for initial customer inquiries and lead qualification.")

    user_input = st.text_input("You: ")
    if st.button("Send"):
        chatbot_response = get_chatbot_response(user_input)
        st.write(f"Chatbot: {chatbot_response}")

# CSS for styling
st.markdown("""
<style>
body {
    font-family: Arial, sans-serif;
}
.header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 1em;
}
</style>
""", unsafe_allow_html=True)

