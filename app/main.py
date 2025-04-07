from flask import Flask, request, redirect, jsonify, render_template
import string, random, os
import redis

app = Flask(__name__, template_folder='templates')

# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('url')
    if not long_url:
        return render_template('index.html', error='Please provide a URL.')

    short_id = generate_short_url()
    r.set(short_id, long_url)
    short_url = request.host_url + short_id
    return render_template('index.html', short_url=short_url)

@app.route('/<short_id>')
def redirect_to_url(short_id):
    long_url = r.get(short_id)
    if long_url:
        return redirect(long_url)
    return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
