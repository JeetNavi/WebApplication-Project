from website import create_app

app = create_app()

if __name__ == '__main__':
    # Only if we run main.py (not import it) will we start the web server
    app.run(debug=True)

