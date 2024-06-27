from website import create_app
#! This code deploys and creats the flask app

app = create_app()
if __name__=="__main__":
    app.run(debug=True, port=8000)
    