from flask import Flask, render_template, request
import json

app = Flask(__name__)
base_url = "https://embeds.ismaeelakram.com"

@app.route('/')
def home():
    return 'Homepage coming soon..'

@app.route('/embed')
def embed():
    title = request.args.get('title') or ""
    author = request.args.get('author') or ""
    color = request.args.get('color') or ""
    image = request.args.get('image') or "https://cdn.ismaeelakram.com/1x1.png"
    url = request.args.get('url') or base_url
    oembed_url = ""

    if author != "":
        oembed_url = f"{base_url}/oembed?author={ author }".replace(' ', '%20')

    if image != "":
        image = image.replace('+', ' ').replace(' ', '%20')

    if color != "":
        color = color.replace('#', '')

    if url != base_url:
        url = url.replace(' ', '%20')

    return render_template('embed.html', title=title, color=color, image=image, author=author, url=url, oembed_url=oembed_url)

@app.route('/oembed')
def oembed():
    author = request.args.get('author') or ""
    oembed_dict = dict()
    oembed_dict["type"] = "photo"
    oembed_dict["author_name"] = author
    return oembed_dict

if __name__ == '__main__':
    app.run()
