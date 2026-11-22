# Streamlit Primer

Small learning examples for tables, maps, layout and widgets. This is a tutorial snapshot, not a hosted dashboard.

```bash
python -m venv .venv
# Activate .venv using your shell's normal command.
python -m pip install -r requirements.txt
python -m streamlit run Basic.py
```

- [Basic.py](Basic.py) displays tables, a chart, and a map.
- [Synthetic pickups](pages/1_Uber.py) shows filtering and map views without downloading a dataset. The points are generated for demonstration, not real trips. Basemap tiles may need network access.
- [Layout](pages/2_layout.py) and [interactive widgets](pages/3_Interactive.py) illustrate sidebar controls and session state.

Streamlit reruns the script when a widget changes. Use `st.session_state` for values that must survive reruns, `st.cache_data` for reusable data, and `st.cache_resource` for shared resources such as model or database objects.

The original learning notes are in [PRIMER_NOTES.md](PRIMER_NOTES.md).
