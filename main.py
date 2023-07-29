from website import create_app

app = create_app()

# run file directory in server
if __name__ == '__main__':
    app.run(debug=True) #run webserver
