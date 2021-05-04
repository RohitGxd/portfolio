from flask import Flask,render_template,request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open ('database.txt' , mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"] 
        file=database.write(f'\n{email},{subject},{message}') 


def write_to_csv(data):
    with open ('database.csv' , mode='a', newline='') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"] 
        csv_writer =csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route("/submit_form" , methods=['POST' , 'GET'])
def submit_form():
    if request.method=="POST":
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect("submitted.html")
        except:
            return "did not save into database"    
    else:
        return "something went wrong Try again later."    




if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')



























# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/work.html")
# def singleWork():
#     return render_template('work.html')


# @app.route("/about.html")
# def about():
#     return render_template('about.html')



# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html' )


# @app.route("/components.html")
# def components():
#     return render_template("components.html" )




















# @app.route('/')
# def hello_world():
#     return render_template('index.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')





# @app.route('/blog')
# def blog():
#     return 'This is my knowledge of blog'


# @app.route('/blog/2020/dogs')
# def dog_vlog():
#     return 'I love the dogs which are cute and small'

