# Streamlit Primer
As a web development framework StreamLit caught my attention because it is extremely simple to use: all the code has to do is give it the data and it will automatically handle the rendering, placement and formatting. This is an ideal module for ML projects I work on where the main focus is the back-end with a superficial front-end being sufficient.
This goes into the basics of how to get Streamlit going:
```python
import streamlit as st
```

Start a streamlit server as follows:

```python
streamlit run <filename>.py
```

Streamlit automatically updates the websites when changes are detected in the code. This facilitates development.

Any time anything updates on the page, the code is executed from top to bottom.

## Displaying stuff

Any variable on its own line is automatically rendered.

To formally write something use:

```python
st.write(<contents you wish to write>)
```

This takes in data and automatically deduces how best to render it. If you want to specify how to render the data, then you need to choose another function: `st.write` is general. It doesn’t allow you to pass formatting parameters.

Code to display text, graphs, tables and maps are built into Streamlit.

## Interactive Applications
When you add widgets such as buttons, you can input data into the application. When the input is changed, the entire script reruns to update the page accordingly.

All interactive widgets can either be assigned to a variable that is a Boolean, string or numeric data type based on the widget. Alternatively, they can be give a `key` through which they can be referenced. The key can either be pre-initialised or it can be generated when the widget is initialised.

The session state (`st.session_state`) is a way to make the behaviour of these interactive widgets either more permanent or more temporary. To do this:

1. Define a variable in the session state at the beginning of the code
2. Define a function to update the session state in a particular way
3. Add the function’s behaviour to the widget so that the session state gets updated when the user interacts with the widget

**Caching** is a way to preserve the values returned from a randomly generated set. It stores the first value that is returned and continues to return that same value as the code executes. Streamlit provides two caching decorators for different purposes:

1. `st.cache_data` - this stores data in the form a data structure that is serialiable
2. `st.cache_resource` - this stores global resources that cannot be serialise such as ML models and database connections

## Multipage apps

These are made by adding subpages into a `Pages/` directory in the folder. The sub pages are added in the directory and appear in the sidebar on the main page. 

<aside>
💡 Page labels in the sidebar UI are generated from filenames.

*Filenames are composed of four different parts:*

1. *A `number` — if the file is prefixed with a number.*
2. *A separator — could be `_`, ``, space, or any combination thereof. (this gets replaces by a space in the UI)*
3. *A `label` — which is everything up to, but not including, `.py`.*
4. *The extension — which is always `.py`.*
</aside>
