import sqlite3
import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Template

def get_poems():
    conn = sqlite3.connect('poems.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, text FROM poems")
    poems = cursor.fetchall()
    conn.close()
    poems = [{'title': title, 'author': author, 'text': text} for title, author, text in poems]
    return poems

def render_html(poems):
    template_path = 'templates/template.html'
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    template = Template(template_content)
    html_content = template.render(poems=poems)
    return html_content

def main():
    poems = get_poems()

    rendered_html = render_html(poems)

    components.html(rendered_html, height=400, scrolling=True)

if __name__ == "__main__":
    main()

