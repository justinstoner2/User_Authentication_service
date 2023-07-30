# User_Authentication_service
A micro service for checking a username and password to a given acceptable username and password dictionary. This service returns a boolean that represents if the information sent is a valid username and password. 

Communication Contract:

This service rus on a FLASK webb server locally on port 5001. When sending a request to the service you need to provide a json objects that contains both the username and password that you want to validate and also a dictionary of all valid usernames and passwords. Below is an example of how you can successfully use the service. The example below is using a flask webserver and what is shown is a route. The URL to check log in info shold be http://localhost:5001/checkLogin

Example:
users = {"bo": "542", "jo": "123", "justin": "huidf"}


    @app.route("/checkLogIn")
        def checkLogIn():
    
        response = requests.post(
            http://localhost:5001/checkLogin, json={"login_info": ["bo", "542"], "users": users.json})
        
        is_login_valid = response.json()
    
        if is_login_valid:
            return "<p>Correct Login Info</p>"
        else:
            return "<p>Incorrect Login Info</p>"


UML Diagram


![UML_Diagram](https://github.com/justinstoner2/User_Authentication_service/assets/20779045/08b0922b-5bc2-4bcc-b563-365fbe4c3e8f)
