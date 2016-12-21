from flask import Flask, redirect, url_for, render_template
from urllib2 import Request, urlopen
import json

    # this:

app = Flask(__name__)

    # is how you start

values = """
    {
    "url": "http://iconnect.ls.lagaude.ibm.com/webaccess",
    "start_docked": "True",
    "follower_redirect_url": "http://iconnect.ls.lagaude.ibm.com/webaccess",
    "leader_redirect_url": "http://iconnect.ls.lagaude.ibm.com/webaccess"
    }
"""

headers = {
    'Content-Type': 'application/json'
}

@app.route('/Ohphieg6Nui0boodeiG0co0eigeeY2ohph3mohraiXa1aefaeShaeteerube')
def index():
    request = Request('https://api.surfly.com/v2/sessions/?api_key=0368dc51794e4a26ba9271c54820e096', data=values, headers=headers)
    response_body = urlopen(request).read()
    parsed_json = json.loads(response_body)
    return redirect(parsed_json["leader_link"])

    # this:

if __name__ == "__main__":
    app.run()

    # is how you end
