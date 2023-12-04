# main.py
from streamlit import cli as stcli
import uvicorn

# Importa tu aplicación Streamlit
import app

# Lanza la aplicación Streamlit usando la CLI de Streamlit
stcli._main_run = lambda _: None
stcli._main_run(["run", "app.py", "--server.enableCORS=false", "--server.enableXsrfProtection=false"])

# Configura y lanza Uvicorn con la aplicación Streamlit integrada
if __name__ == "__main__":
    uvicorn.run("main:stcli", host="0.0.0.0", port=8000, reload=True)