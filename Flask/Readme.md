
## Flask

<aside>
💡 **Flask** is a micro web framework for Python that allows developers to build web applications quickly and easily. It is designed to be simple, lightweight, and modular, with minimal dependencies and a flexible architecture that allows developers to customize and extend it as needed.

</aside>

Some key features of Flask include:

- **Routing**: Flask provides a simple way to map URLs to functions, allowing developers to define routes for different parts of their application and handle HTTP requests and responses.
- **Templates**: Flask includes a powerful templating engine that allows developers to separate the presentation of their web application from the underlying logic, making it easier to maintain and update the application over time.
- **Extensions**: Flask provides a modular architecture that allows developers to add or remove functionality as needed, with a large number of third-party extensions available for common tasks such as database integration, user authentication, and more.
- **Testing**: Flask includes built-in support for testing, with a testing client that allows developers to simulate HTTP requests and responses and automate testing of their web application.

# Flask architecture

The Flask architecture is based on the Model-View-Controller (MVC) design pattern, which separates the application into three main components: models, views, and controllers.

1. **Models**: Models represent the data and the business logic of the application. They define how data is stored, retrieved, and manipulated in the application. In Flask, models are typically implemented using an Object-Relational Mapping (ORM) library such as SQLAlchemy.
2. **Views**: Views are responsible for handling requests from the user and returning responses. They retrieve data from the models, process it as necessary, and render a template or return a JSON response. In Flask, views are implemented as Python functions decorated with the **`@app.route`** decorator.
3. **Controllers**: Controllers provide the glue between the models and the views. They are responsible for coordinating the flow of data between the models and views and for implementing any additional business logic required by the application. In Flask, controllers are often implemented as modules or packages containing related views and models.

## Model View Control (MVC ) Example

To demonstrate how a web application structured using the **[Model-View-Controller](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)**
 pattern (or **MVC**) works in practice,

You’re ten years old, sitting on your family room floor, and in front of you is a big bucket of Legos. There are Legos of all different shapes and sizes. Some blue, tall, and long. Like a tractor trailer. Some red and almost cube shaped. And some are yellow - big wide planes, like sheets of glass. With all these different types of Legos, there’s no telling what you could build.

But surprise, surprise, there’s already a **request**. Your older brother runs up and says, “Hey! Build me a spaceship!”

“Alright,” you think, “that could actually be pretty cool!” A spaceship it is.

So you get to work. You start pulling out the Legos you think you’re going to need. Some big, some small. Different colors for the outside of the spaceship, different colors for the engines. Oh, and different colors for the blaster guns. (You gotta have blaster guns!)

Now that you have all of your **building blocks** in place, it’s time to assemble the spaceship. And after a few hours of hard work, you now have in front of you - a spaceship!

You run to find your brother to show him the finished product. “Wow, nice work!”, he says. “Huh,” he thinks, “I just asked for that a few hours ago, didn’t have to do a thing, and there it is. I wish *everything* was that easy.”

What if I were to tell you that building a web application is exactly like building with Legos?

### **It all starts with a *request*…**

In the case of the Legos, it was your brother who asked you to build something. In the case of a web app, it’s a user entering a URL, requesting to view a certain page.

So your brother is the user.

### **The request reaches the *controller*…**

With the Legos, you are the controller.

The controller is responsible for grabbing all of the necessary **building blocks** and organizing them as necessary.

### **Those building blocks are known as *models*…**

The different types of Legos are the models. You have all different sizes and shapes, and you grab the ones you need to build the spaceship. In a web app, models help the controller retrieve all of the information it needs from the database.

### **So the request comes in…**

The controller (you) receives the request.

It goes to the models (Legos) to retrieve the necessary items.

And now everything is in place to produce the final product.

### **The final product is known as the *view*…**

The spaceship is the view. It’s the final product that’s ultimately shown to the person who made the request (your brother).

In a web application, the view is the final page the user sees in their browser.

## **To summarize…**

**When building with Legos:**

1. Your brother makes a request that you build a spaceship.
2. You receive the request.
3. You retrieve and organize all the Legos you need to construct the spaceship.
4. You use the Legos to build the spaceship and present the finished spaceship back to your brother.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a54135ea-1538-4737-b865-4d7c21d480ee/Untitled.png)

**And in a web app:**

1. A user requests to view a page by entering a URL.
2. The **Controller** receives that request.
3. It uses the **Models** to retrieve all of the necessary data, organizes it, and sends it off to the…
4. **View**, which then uses that data to render the final webpage presented to the the user in their browser.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ba6c767e-6800-4990-8bf2-4b5b0ea2abd5/Untitled.png)

## **From a more technical standpoint**

- With the MVC functionality summarized, let’s dive a bit deeper and see how everything functions on a more technical level.
- When you type in a URL in your browser to access a web application, you’re making a request to view a certain page within the application. But how does the application know which page to display/render?
- When building a web app, you define what are known as **routes**. Routes are, essentially, URL patterns associated with different pages. So when someone enters a URL, behind the scenes, the application tries to match that URL to one of these predefined routes.
- So, in fact, there are really *four* major components in play: **routes**, **models**, **views**, and **controllers**.

### **Routes**

Each route is associated with a controller - more specifically, a certain function *within* a controller, known as a **controller action**. So when you enter a URL, the application attempts to find a matching route, and, if it’s successful, it calls that route’s associated controller action.

Let’s look at a basic [Flask](https://realpython.com/python-web-applications-with-flask-part-i/) route as an example:

```python
@app.route('/')
def main_page():
    pass
```

Here we establish the `/` route associated with the `main_page()` view function.

### **Models and Controllers**

Within the controller action, two main things typically occur: the models are used to retrieve all of the necessary data from a database; and that data is passed to a view, which renders the requested page. The data retrieved via the models is generally added to a data structure (like a list or dictionary), and that structure is what’s sent to the view.

Back to our Flask example:

```python
@app.route('/')
def main_page():
    """Searches the database for entries, then displays them."""
    db = get_db()
    cur = db.execute('select * from entries order by id desc')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)
```

Now within the view function, we grab data from the database and perform some basic logic. This returns a list, which we assign to the variable `entries`, that is accessible within the *index.html* template.

### **Views**

Finally, in the view, that structure of data is accessed and the information contained within is used to render the HTML content of the page the user ultimately sees in their browser.

Again, back to our Flask app, we can loop through the `entries`, displaying each one using the Jinja syntax:

```python
{% for entry in entries %}
  <li>
    <h2>{{ entry.title }}</h2>
    <div>{{ entry.text|safe }}</div>
  </li>
{% else %}
  <li><em>No entries yet. Add some!</em></li>
{% endfor %}
```

### **Summary**

So a more detailed, technical summary of the MVC request process is as follows:

1. A user requests to view a page by entering a URL.
2. The application matches the URL to a predefined **route**.
3. The **controller action** associated with the route is called.
4. The controller action uses the **models** to retrieve all of the necessary data from a database, places the data in an array, and loads a **view**, passing along the data structure.
5. The **view** accesses the structure of data and uses it to render the requested page, which is then presented to the user in their browser.

In addition to the MVC components, Flask also includes the following key features:

1. **Routing**: Flask provides a simple and flexible routing system that allows you to map URLs to views and controllers.
2. **Templates**: Flask supports the use of templates for rendering dynamic HTML pages. Templates are typically implemented using the Jinja2 templating engine.
3. **Static files**: Flask allows you to serve static files such as CSS and JavaScript files directly from the application.
4. **Extensions**: Flask has a large ecosystem of extensions that provide additional functionality such as user authentication, database integration, and email support.

Overall, the Flask architecture is designed to be lightweight and flexible, allowing you to build web applications quickly and easily while still providing the necessary features for building robust and scalable applications.

### **Basic concepts and features of Flask:**

1. **Routes**: Flask uses decorators to define URL routes for your application. For example, the following code defines a route for the root URL of your application:

```python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

```

1. **Views:** In Flask, a view is a function that handles a request and returns a response. In the example above, the **`index`** function is a view that returns the string "Hello, world!" when the root URL is requested.
2. **Templates**: Flask uses the Jinja2 template engine to render HTML templates. Templates allow you to separate your application logic from your presentation layer. For example, you could define a template that includes a placeholder for a user's name, and then use the **`render_template`** function to fill in the name dynamically:

```python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()

```

1. **Static files**: Flask allows you to serve static files (such as CSS, JavaScript, and images) directly from your application. You can use the **`url_for`** function to generate URLs for your static files:

```python

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    css_url = url_for('static', filename='styles.css')
    return f'<link rel="stylesheet" href="{css_url}">'

if __name__ == '__main__':
    app.run()

```

1. **Forms**: Flask includes support for handling HTML forms. You can use the **`request`** object to access form data that is submitted by the user:

```python

from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate the user's credentials
    else:
        return '''
            <form method="post">
                <input type="text" name="username">
                <input type="password" name="password">
                <input type="submit" value="Login">
            </form>
        '''

if __name__ == '__main__':
    app.run()

```

These are just a few of the basic concepts and features of Flask. Flask is a versatile and powerful framework that can be used to build a wide variety of web applications, from simple prototypes to complex production-ready systems.

Here's a simple example of a Flask application:

```python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()

```

In this example, we create a Flask application that defines a single route for the root URL ("/") and a corresponding view function that returns a simple "Hello, world!" message. We then start the application by calling the **`run`** method on the **`app`** object, which starts a local development server and listens for incoming HTTP requests.

Overall, Flask is a popular choice for building web applications in Python due to its simplicity, flexibility, and ease of use.

flask

### **app =Flask(__name__)**

- **`app = Flask(__name__)`** is a line of code in a Python script that creates a new instance of the **`Flask`** class, which is the central object of a Flask application.
- The **`Flask`** class is defined in the Flask library and represents the core of the web application. It is responsible for handling incoming HTTP requests, routing them to the appropriate view functions, and generating HTTP responses that are sent back to the client.
- The **`__name__`** parameter passed to the **`Flask`** constructor is a special Python variable that refers to the name of the current module or package. In the context of a Flask application, it is used to help Flask locate resources such as templates and static files.

- When you create a new instance of the **`Flask`** class, you typically assign it to a variable named **`app`**, which is then used to define the routes and views for the application. For example, you might define a route for the root URL of the application like this:

```python

@app.route('/')
def index():
    return 'Hello, World!'
```

- In this example, we use the **`@app.route`** decorator to associate the **`/`** URL with the **`index`** function, which returns a simple "Hello, World!" message.
- Overall, the **`app = Flask(__name__)`** line of code is an essential part of any Flask application, as it sets up the basic framework for handling HTTP requests and responses.

### @app.route()

- **`@app.route`** is a decorator in Flask that is used to associate a URL with a view function, which is responsible for generating an HTTP response for that URL.
- In a Flask application, you define routes by decorating view functions with the **`@app.route`** decorator, followed by a string that specifies the URL path for the route. For example:

```python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

```

- In this example, we define a route for the root URL (**`/`**) of the application, by using the **`@app.route`** decorator to associate it with the **`index`** function. When a client requests the root URL of the application, Flask will invoke the **`index`** function and return the string "Hello, World!" as an HTTP response.
- The **`@app.route`** decorator can also be used with URL patterns that include parameters, such as:

```

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

```

- In this example, we define a route for URLs that include a username parameter, by using the **`<username>`** syntax to specify where the parameter should be located in the URL.
- When a client requests a URL that matches this pattern, Flask will invoke the **`show_user_profile`** function and pass the value of the **`username`** parameter as an argument.
- Overall, the **`@app.route`** decorator is a key feature of Flask that allows developers to define the routes for their web application in a clear and concise manner.

### if __name__ == ”__main__”:

- **`if __name__ == "__main__":`** is a conditional statement that is often used in Python scripts to ensure that certain code is only executed when the script is run as the main program, rather than being imported as a module by another script.
- In the context of a Flask application, the **`if __name__ == "__main__":`** statement is typically used to start the Flask development server, which listens for incoming HTTP requests and handles them by invoking the appropriate view functions.
- Here's an example of how the **`if __name__ == "__main__":`** statement might be used in a Flask application:

```python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

```

- In this example, we define a simple Flask application that includes a single route for the root URL and a corresponding view function that returns a "Hello, world!" message.
- We then use the **`if __name__ == "__main__":`** statement to start the development server by calling the **`run`** method on the **`app`** object.
- When you run this script from the command line using **`python app.py`**, the **`if __name__ == "__main__":`** statement will evaluate to **`True`**, and the Flask development server will start listening for incoming HTTP requests.
- However, if you were to import this script as a module in another script, the **`if __name__ == "__main__":`** statement would evaluate to **`False`**, and the Flask development server would not be started.
- Overall, the **`if __name__ == "__main__":`** statement is a useful tool for ensuring that certain code is only executed under specific conditions, and is commonly used in Python scripts that include Flask applications.

## app.run()

**`app.run()`** is a method in the Flask library that starts the development server and listens for incoming HTTP requests.

In a Flask application, you typically call the **`run`** method on the **`app`** object to start the development server, like this:

```

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

```

- In this example, we define a simple Flask application that includes a single route for the root URL and a corresponding view function that returns a "Hello, world!" message.
- We then use the **`if __name__ == "__main__":`** statement to start the development server by calling the **`run`** method on the **`app`** object.
- When you run this script from the command line using **`python app.py`**, the **`app.run()`** method will start the Flask development server and listen for incoming HTTP requests on the default port (usually 5000).
- You can then open a web browser and visit **`http://localhost:5000`** to see the "Hello, world!" message generated by the **`hello`** view function.
- The **`app.run()`** method can also accept a number of optional parameters, such as the host and port to listen on, as well as options for SSL/TLS encryption and automatic reloading of the server when the code changes.
- Overall, the **`app.run()`** method is an essential part of any Flask application, as it starts the development server and allows the application to handle incoming HTTP requests.

## redirect

In Flask, **`redirect`** is a function that is used to redirect the client to a different URL.

Here's an example of how the **`redirect`** function might be used in a Flask application:

```

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/redirect-example')
def redirect_example():
    # Redirect to the about page
    return redirect(url_for('about'))

if __name__ == '__main__':
    app.run()

```

- In this example, we define three routes: one for the root URL (**`/`**), one for the **`/about`** URL, and one for a **`/redirect-example`** URL. When a client requests the **`/redirect-example`** URL, the **`redirect_example`** view function uses the **`redirect`** function to redirect the client to the **`/about`** URL.
- The **`redirect`** function takes a URL or endpoint as its argument, and returns an HTTP response that instructs the client to make a new request to the specified URL or endpoint. In this example, we use the **`url_for`** function to generate a URL for the **`about`** endpoint, and pass it to the **`redirect`** function.
- Overall, the **`redirect`** function is a useful tool for implementing client-side redirects in Flask applications, and is often used in conjunction with the **`url_for`** function to generate URLs dynamically.

## url_for

- In Flask, **`url_for`** is a function that is used to generate a URL for a given endpoint.
- Endpoints are typically defined using the **`@app.route`** decorator in Flask, and represent the URLs that the application can handle. For example, here's a simple Flask application that defines two endpoints:

```

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run()

```

- In this example, we define two endpoints: one for the root URL (**`/`**), and one for the **`/about`** URL. When a client requests either of these URLs, Flask invokes the appropriate view function (**`index`** or **`about`**) to generate a response.
- The **`url_for`** function is used to generate a URL for a given endpoint. For example, to generate a URL for the **`about`** endpoint in the example above, you would use the following code:

```

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    about_url = url_for('about')
    return f'The URL for the about page is {about_url}'

@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run()

```

- In this example, the **`index`** view function uses the **`url_for`** function to generate a URL for the **`about`** endpoint, and then returns a message that includes the generated URL.
- The **`url_for`** function takes the name of the endpoint as its argument, and returns a URL that is appropriate for the current application context. The generated URL will include any necessary query string parameters, and will be relative to the current request's host and port.
- Overall, the **`url_for`** function is a useful tool for generating URLs dynamically in Flask applications, and is often used in conjunction with the **`redirect`** function to implement client-side redirects.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6f51f156-8d5d-4c6e-bdda-c91f5883276a/Untitled.png)

login.py

```python
from flask import Flask, redirect ,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=='POST':
        user=request.form['usr_name']   #request.form is dictonary,usr_name is key
        return redirect(url_for('user',usr=user))
    return render_template("login.html")

@app.route('/<usr>')
def user(usr):
    return f"Hello {usr}!"

if __name__ =="__main__":
    app.run(debug=True)
```

login.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Welcome to login page</h1>
    
        <form action="#" method="Post">
            <input type="text" name="usr_name" >
            <input type="submit" value="submit">
        </form>
        
  
</body>
</html>
```

Unlike cookies, Session (session) data is stored on the server. The session
is the interval at which the client logs on to the server and logs out the
server. The data that is required to be saved in the session is stored in a
temporary directory on the server.

Assign session IDs to sessions for each client. Session data is stored at the
top of the cookie, and the server signs it in encrypted mode.For this
encryption, the Flask application requires a defined SECRET _ KEY.
