from flask import Flask, jsonify, request
import csv

app = Flask(__name__)


@app.route("/checkLogin", methods=["POST"])
def checkLogIn():
    data = request.get_json()
    login_info = data.get("login_info", [])
    usersDict = {}
    with open ('active_users.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader)
        for row in reader:
            
            usersDict[row['\ufeffusername']]=row['password']
    
    
    print(login_info[0])
    print(usersDict)
    return jsonify(isActiveUser(usersDict,login_info))


def isActiveUser(users, logIn):
    if logIn[0] in users:
        if logIn[1] == users[logIn[0]]:
            return True
    else:
        return False


if __name__ == '__main__':
    app.run(port=5001, debug=True)
