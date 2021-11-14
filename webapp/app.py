from flask import Flask, render_template


app = Flask(__name__)



def create_app():

    app = Flask(__name__)

    @app.route("/hello")
    def get_index():
        # return render_template("webapp/templates/index.html")
        return "hello world"



    return app


# if __name__=="__main__":
#     app.run()