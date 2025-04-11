from flask import Flask, request, redirect, jsonify, render_template
import string, random, os
import redis
import logging

app = Flask(__name__, template_folder='templates')

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# --- Redis Setup ---
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
        logging.warning("No URL provided for shortening")
        return render_template('index.html', error='Please provide a URL.')

    short_id = generate_short_url()
    r.set(short_id, long_url)
    short_url = request.host_url + short_id
    logging.info(f"Shortened URL: {long_url} -> {short_url}")
    return render_template('index.html', short_url=short_url)

@app.route('/<short_id>')
def redirect_to_url(short_id):
    long_url = r.get(short_id)
    if long_url:
        logging.info(f"Redirected short ID: {short_id} -> {long_url}")
        return redirect(long_url)
    logging.error(f"Short ID not found: {short_id}")
    return jsonify({'error': 'URL not found'}), 404

# --- Main Entry Point ---
if __name__ == '__main__':
    logging.info("Starting URL shortener server...")
    app.run(host='0.0.0.0', port=5000)
