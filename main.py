from flask import Flask
import os
import sys

app = Flask(__name__)

# Access environment variables
custom_variable = os.environ.get("batch", "")


@app.route("/")
def hello():
    return f"Hello, Welcome to HelloCloud! We are {custom_variable} members"


if __name__ == "__main__":
    # Get custom argument (in the format "listen:80") or use default (listen:5000)
    arg = sys.argv[1] if len(sys.argv) > 1 else "listen:5000"

    # Extract the port from the argument
    port = int(arg.split(":")[1])

    app.run(debug=True, host="0.0.0.0", port=port)
