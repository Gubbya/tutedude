from flask import Flask, request , render_template
import datetime

app = Flask(__name__) # 1)http://127.0.0.1:5000 is the default address where Flask runs. given in terminal.
@app.route('/')
def home():
    return 'Helcome to Home Page!' # this was used in 1st step.
   
@app.route('/second') # 3) Here we are giving  route for the second page.
def second():
    return 'Welcome to Second Page!'

# 4) Fetching a value from the URL.
@app.route('/app/<name>') # 4) this is syntax for getting a value from the URL.
def name(name):
       # print(name) #4.1) this will print the name in the terminal.
        #return 'Hello, Welcome to the app!.'
        
        length = len(name) # 4.2) this will calculate the length of the name.
        result = "Hello, " + name + "!" # 4.3) Disply Name in web page.
        return result #4.3.1)
      # if length > 5: # 4.2.1) this will check if the length of the name is greater than 5.
      #     return 'Name is too long!' 
      # else: # 4.2.2)
      #     return 'Nice Name!'
        
# 5) Fetching two values from the URL and do some math.
@app.route('/add/<a>/<b>') # 5) this is syntax for getting two values from the URL.
def  sum(a, b): # def  sum instead of name to avoid confusion with the previous function.
        answer = int(a) + int(b) # 5.1) here int is used to convert the string values to integers.
        result = {
      'ans' : answer # Interger gives error in web so coverte it to string.
  }
        return result 

# 6) fetch usnig Json format.
@app.route('/api') # how to pass value to URL is "http://127.0.0.1:5000/api?name=your_name&age=your_age" after ? what ever we out that is call request parameters. it must be in Key value pair format.
def newjson():
    
        name = request.values.get('name') # 6.1) this will get the name from the URL. request is imported from flask.
        age = request.values.get('age') # 6.2) this will get the
        batch = request.values.get('batch')
        result = {
            'name': name, # 6.3) this will return the name in the JSON format.
            'age': age ,# 6.4) this will return the age in the JSON format.
            'batch': batch # 6.5) this will return the batch in the JSON format.
        }
    
        return result
# fetch usnig Json format and add some condition.
@app.route('/api2') 
def newjson2():
    
        name = request.values.get('name')        
        age = request.values.get('age')  
        age = int(age)
        if age > 18:
            return 'Welcome to the app!' + name + '!' 
        else:
            return 'You are to young to access this app!'        
        
        # 7) Using Render Template to render HTML files.
@app.route('/index') # 7) this is the route for the index.html file.
def index():
    return render_template('index.html') # 7) this will render or open the index.html file
       
        #8) Get current day of the week as a string (e.g., 'Monday')

@app.route('/day') # 8) this is the route for the day.html file.
def day():
    current_day = datetime.datetime.today().strftime('%A')
    print("Today is:", current_day) # 8.1) this will print the current day in the terminal.
    return current_day  # 8.2) this will return the current day in the web page. 
                           
                           
 # 9) this will return the current day in html the web page.     
@app.route('/day2') # 9) this is the route for the day2.html file.
def day2():
    current_day = datetime.datetime.today().strftime('%A') # 9.1) this will get the current day of the week as a string (e.g., 'Monday').
    return render_template('date.html', current_day=current_day)  # 9.1) this will return the current day in the web page using render_template.


 # 10) this will return the current day, date & time in html the web page.     
@app.route('/day3') 
def day3():
    current_day = datetime.datetime.today().strftime('%A')
    current_date = datetime.datetime.today().strftime('%Y-%m-%d')
    current_time = datetime.datetime.today().strftime('%H:%M:%S')
    info = f"{current_day}<br>Date: {current_date}<br>Time: {current_time}" 
    # here current_day, current_date, and current_time are formatted as strings and combined with <br> tags for line breaks.
    # In the HTML template, we will use the Jinja "|safe" filter to ensure that the <br> tags are rendered as line breaks.
    # This allows us to display each item (day, date, time) on a separate line in the web page.
    
    return render_template('date.html', current_day=info)


if __name__ == '__main__':
    app.run(debug=True) # 2) debug=True enables debug mode so real-time changes can be seen without restarting the server.

