from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def invite():
    return redirect("https://discord.com/oauth2/authorize?client_id=832297955645063188&permissions=247808&scope=bot", code=302)

if __name__ == '__main__':
    #thread_one = Thread(target = client.run(api_key)).start()
    app.run(threaded=True, port = 5000)
    # thread_one.start()
    # thread_two.start()
