from flask import Flask, request, redirect, jsonify
import string, random, os
import redis

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('url')
    if not long_url:
        return jsonify({'error': 'Missing URL'}), 400

    short_id = generate_short_url()
    r.set(short_id, long_url)
    return jsonify({'short_url': request.host_url + short_id})

@app.route('/<short_id>')
def redirect_to_url(short_id):
    long_url = r.get(short_id)
    if long_url:
        return redirect(long_url)
    return jsonify({'error': 'URL not found'}), 404

@app.route('/')
def index():
    return '''
    <h2>URL Shortener</h2>
    <p>Use <code>POST /shorten</code> with a JSON body like {"url": "https://example.com"}.</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
