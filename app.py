from flask import Flask, request, jsonify
app = Flask(__name__)

def json_make(type,msg):
    return {"type":type,"msg":msg}

license = {
    "DAC" : {
        "enable": "True",
        "ip": "127.0.0.1"
    }
}

@app.route('/api/license/<key>')
def api(key):
    key = str(key)
    try:
        if license[key] == None:
            # Not Found :(
            return json_make("error", "1"), 404
    except Exception as e:
        return json_make("error", "1"), 404
    else:
        if license[key]["enable"] != "True":
            return json_make("error", "2"), 423
        if license[key]["ip"] != request.remote_addr:
            return json_make("error", "3"), 403
        else:
            return json_make("license", "ok"), 200

if __name__ == '__main__':
    app.run(port=80)