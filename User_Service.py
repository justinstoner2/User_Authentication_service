from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/checkLogin", methods=["POST"])
def checkLogIn():
    data = request.get_json()
    login_info = data.get("login_info", [])
    users = data.get("users", {})
    print(login_info[0])
    print(users)
    return jsonify(isActiveUser(users, login_info))


def isActiveUser(users, logIn):
    if logIn[0] in users:
        if logIn[1] == users[logIn[0]]:
            return True
    else:
        return False


if __name__ == '__main__':
    app.run(port=5001, debug=True)
