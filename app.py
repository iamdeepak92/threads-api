from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Route 1: Fetch userid by username


@app.route("/userid/<username>", methods=["GET"])
def get_userid(username):
    try:
        url = "https://www.threads.net/ajax/bulk-route-definitions/"
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "sec-fetch-site": "same-origin",
            "x-fb-lsd": "4GaYIJW6lxs-XRVfHawU8K",
        }
        data = {
            "route_urls[0]": "/@" + username,
            "__user": "0",
            "__a": "1",
            "__comet_req": "29",
            "lsd": "4GaYIJW6lxs-XRVfHawU8K",
        }
        response = requests.post(url, headers=headers, data=data)
        result = response.text.replace("for (;;);", "")
        result = json.loads(result)
        userid = result["payload"]["payloads"]["/@" +
                                               username]["result"]["exports"]["rootView"]["props"]["user_id"]
        return jsonify({"userid": userid})

    except Exception as e:
        print("error", e)
        return jsonify({"error": "Internal Server Error"}), 500

# Route 2: Fetch user profile by userid


@app.route("/userprofile/<userid>", methods=["GET"])
def get_user_profile(userid):
    try:
        url = "https://www.threads.net/api/graphql"
        headers = {
            "x-fb-lsd": "BMckKFfB3JDIA2XkhD8-ez",
            "x-ig-app-id": "238260118697367",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "lsd": "BMckKFfB3JDIA2XkhD8-ez",
            "variables": json.dumps({"userID": userid}),
            "doc_id": "23996318473300828",
        }
        response = requests.post(url, headers=headers, data=data)
        result = response.json()
        return jsonify(result)

    except Exception as e:
        print("error", e)
        return jsonify({"error": "Internal Server Error"}), 500

# Route 3: Fetch threads or posts of userid


@app.route("/threads/<userid>", methods=["GET"])
def get_threads(userid):
    try:
        url = "https://www.threads.net/api/graphql"
        headers = {
            "x-fb-lsd": "A2LiqVjcY0jBE_DEsTaKNI",
            "x-ig-app-id": "238260118697367",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "dpr": "1",
            "lsd": "A2LiqVjcY0jBE_DEsTaKNI",
            "variables": json.dumps({"userID": userid}),
            "doc_id": "6451898791498605",
        }
        response = requests.post(url, headers=headers, data=data)
        result = response.json()
        return jsonify(result)

    except Exception as e:
        print("error", e)
        return jsonify({"error": "Internal Server Error"}), 500


# Start the server
if __name__ == "__main__":
    port = 3000
    app.run(port=port)
