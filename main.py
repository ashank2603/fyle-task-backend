from flask import Flask, jsonify
from github import Github, UnknownObjectException
from flask_cors import CORS
from dotenv import dotenv_values

config = dotenv_values(".env")
access_token = config["GITHUB_API_KEY"]

HTTP_404_NOT_FOUND = 404 
HTTP_500_INTERNAL_SERVER_ERROR = 500

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.errorhandler(HTTP_404_NOT_FOUND)
def handle_404(e):
    return jsonify({'error': 'Not found'}), HTTP_404_NOT_FOUND

@app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
def handle_500(e):
    return jsonify({'error': 'Something went wrong, we are working on it'}), HTTP_500_INTERNAL_SERVER_ERROR

@app.route('/')
def home():
    data = {
        "status" : 200,
        "message" : "Welcome to GitHub API. Create a query (route: /api/<GITHUB_USERNAME>) to get results."
    }
    return jsonify(data),200

@app.route('/api/<string:requser>')
def api(requser):
    g = Github(access_token)
    try:
        user = g.get_user(requser)
        all_repos = list()
        name = user.name
        username = user.login
        avatar = user.avatar_url
        bio = user.bio
        twitter_username = user.twitter_username
        location = user.location
        repos = user.get_repos()
        for repo in repos:
            repo_data = dict()
            repo_data["id"] = repo.id 
            repo_data["name"] = repo.name
            repo_data["description"] = repo.description
            repo_data["repo_url"] = repo.html_url
            temp = repo.get_languages()
            languages = []
            for g in temp:
                languages.append(g)
            repo_data["languages"] = languages
            all_repos.append(repo_data)
        data = {
            "status" : 200,
            "userinfo" :  
            {
                "name" : name,
                "username" : username,
                "bio" : bio,
                "location" : location,
                "twitter_username" : twitter_username,
                "avatar_url" : avatar,
                "all_repos" : all_repos,
            }
            , 
            "total" : len(all_repos)
        }
        return jsonify(data),200
    except UnknownObjectException:
        data = {
            "status": 404,
            "message": "User Not Found!"
        }
        return jsonify(data),404

if __name__ == "__main__":
    app.run(debug=True)