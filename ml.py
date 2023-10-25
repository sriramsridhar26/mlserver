from flask import Flask, request, Response
import datadriver
import notification

app = Flask(__name__)

@app.route("/statuscheck")
def test():
    return "<p>success</p>"

@app.route("/updatevital", methods=['POST'])
def updatevital():
    try:
        data = request.json
        userid = data.get("userid")
        heartrate = data.get("heartrate")
        dd = datadriver.datadriver()
        dd.update(userid,heartrate)
        if(heartrate<50):
            notif = notification.notification()
            notif.emailnotif("sriramsridhar26@gmail.com","Low BP alert","Your relative might pass out due to dehydration/low bp.\nContact them immediately")
            notif.mobilenotif("+15199929160","Your relative might pass out due to dehydration")
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=400)

# app.route("/send")

if __name__ == '__main__':
    app.run(debug=True)