from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    content = (
        "Hi Deutsche Börse Cloud Team 👋\n\n"
        "Welcome to my CI/CD Cloud Run project!\n\n"
        "This Flask app is:\n"
        "- Containerized with Docker\n"
        "- Built and deployed automatically with GitHub Actions\n"
        "- Hosted on Google Cloud Run\n"
        "- Monitored using GCP Uptime Checks and Alerting\n\n"
        "Looking forward to discussing it during the interview!\n\n"
        "– Sumit Kumar"
    )
    return Response(content, mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
