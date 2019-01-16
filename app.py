from flask import Flask
#from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    #the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")    
    return 'Halló heimur! <br>' \
           '<a href="/about">about </a>' \
           '<a href="/biography">Biography </a>' \
           '<a href="/pictures">Pictures </a>'

    #<img src="http://loremflickr.com/600/400">
    #""".format(time=the_time)
    
@app.route('/biography')
def Biography():
    return 'Biography! <br>' \
           '<a href="/about">about </a> ' \
           '<a href="/biography">Biography </a>' \
           '<a href="/pictures">Pictures </a>'

@app.route('/pictures')
def Pictures():
    return 'Pictures! <br>' \
           '<a href="/">about </a> ' \
           '<a href="/biography">Biography </a> ' \
           '<a href="/pictures">Pictures </a>'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

