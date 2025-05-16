# app.py
from flask import Flask, render_template
import socket
from typing import Optional

app = Flask(__name__)

def find_open_port(desired_port: int, max_attempts: int = 100) -> Optional[int]:
    """
    Find an available port, prioritizing the desired port if ≥1024.
    
    Args:
        desired_port: The requested port number
        max_attempts: Maximum number of ports to check
    
    Returns:
        The first available port number (≥1024), or None if no ports are available
    """
    # If desired port is ≥1024, try it first
    if desired_port >= 1024:
        start_port = desired_port
    else:
        start_port = 1024
    
    for port in range(start_port, start_port + max_attempts):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(('', port))
            sock.close()
            return port
        except OSError:
            continue
        finally:
            sock.close()
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_port/<int:desired_port>')
def find_port(desired_port):
    open_port = find_open_port(desired_port)
    if open_port:
        return {
            'success': True,
            'port': open_port,
            'message': f'The next available port is {open_port}'
        }
    return {
        'success': False,
        'message': f'No open ports found'
    }, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=56789)
