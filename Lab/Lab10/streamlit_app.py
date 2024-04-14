
# Importing necessary libraries
import sqlite3
import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Template

# Function to connect to the SQLite database and retrieve poems
def get_poems():
    conn = sqlite3.connect('poems.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, text FROM poems")
    poems = cursor.fetchall()
    conn.close()
    return poems

# Function to render HTML using Jinja2
def render_html(poems):
    # HTML template stored in a separate file named 'template.html' under './templates/' directory
    template_path = 'templates/template.html'
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    template = Template(template_content)
    html_content = template.render(poems=poems)
    return html_content

# Main function to set up the Streamlit app
def main():
    # Fetch poems from the database
    poems = get_poems()
    
    # Render the HTML with poem data
    rendered_html = render_html(poems)
    
    # Display the rendered HTML in Streamlit
    components.html(rendered_html, height=400, scrolling=True)

if __name__ == "__main__":
    main()
