"""
CRITICAL: DO NOT EDIT. For MPShips users: Manual changes may cause system instability.
"""

import os
from src.thermal_redox_app.example_app import create_app

app = create_app()
server = app.server


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8051

    app.run(debug=True, host=host, port=port)