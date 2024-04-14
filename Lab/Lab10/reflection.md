1. difference between Streamlit and Flask

Streamlit is designed to turn data scripts into shareable web apps with minimal web development knowledge required. It is highly interactive and allows for rapid prototyping of data applications with built-in support for visualizations and machine learning. Streamlit apps are essentially Python scripts, which are run from top to bottom, and every time a user interacts with the app, the entire script is rerun.

Flask, on the other hand, is a micro web framework that gives developers more control over the web application and is used for a wide range of applications, from small to large-scale web services. It is minimalist and flexible, making no assumptions or decisions about the backend needed. This means it is often used for both the frontend and backend development, and it requires manual setup for things like database connections, route handling, and page rendering.

2. When would you use Flask instead of Streamlit?
   
Need fine-grained control over the web server behavior, URL routes, and responses.

For applications that require a traditional multi-page web app structure, since Streamlit is more oriented towards single-page applications.

Handle different types of requests (GET, POST, PUT, DELETE) and responses, including APIs that serve data to clients.

When the application has complex server-side logic, requires authentication, or integrates with third-party services.

