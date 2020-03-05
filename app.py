from flask import Flask, Response

app = Flask(__name__)

@app.route("/song")
def streamogg():
    def generate():
        with open("song.mp3", "rb") as fogg:
            data = fogg.read(1024)
            while data:
                yield data
                data = fogg.read(1024)
    return Response(generate(), mimetype="audio/mp3")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
