from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
import re

app = Flask(__name__)
app.secret_key = 'change_this_secret_key'

RULES_FILE = 'rules.json'

def load_rules():
    if not os.path.exists(RULES_FILE):
        return {'blocked_ips': [], 'blocked_ports': []}
    with open(RULES_FILE, 'r') as f:
        return json.load(f)

def save_rules(rules):
    with open(RULES_FILE, 'w') as f:
        json.dump(rules, f, indent=4)

def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False

def is_valid_port(port):
    if port.isdigit():
        p = int(port)
        return 1 <= p <= 65535
    return False

def is_malicious(value):
    # Basic check for common attack strings
    blacklist = ['<script>', 'DROP TABLE', '--', '/*', '*/', 'OR 1=1', 'alert(']
    return any(b.lower() in value.lower() for b in blacklist)

@app.route('/')
def index():
    rules = load_rules()
    return render_template('firewall.html', rules=rules)

@app.route('/add', methods=['POST'])
def add_rule():
    rules = load_rules()
    ip = request.form.get('ip', '').strip()
    port = request.form.get('port', '').strip()

    if ip:
        if is_malicious(ip) or not is_valid_ip(ip):
            flash("Invalid or malicious IP address.")
            return redirect(url_for('index'))
        if ip not in rules['blocked_ips']:
            rules['blocked_ips'].append(ip)

    if port:
        if is_malicious(port) or not is_valid_port(port):
            flash("Invalid or malicious port number.")
            return redirect(url_for('index'))
        if port not in rules['blocked_ports']:
            rules['blocked_ports'].append(port)

    save_rules(rules)
    flash("Rule added successfully.")
    return redirect(url_for('firewall'))

@app.route('/remove', methods=['POST'])
def remove_rule():
    rules = load_rules()
    ip = request.form.get('ip', '').strip()
    port = request.form.get('port', '').strip()

    if ip and ip in rules['blocked_ips']:
        rules['blocked_ips'].remove(ip)
    if port and port in rules['blocked_ports']:
        rules['blocked_ports'].remove(port)

    save_rules(rules)
    flash("Rule removed successfully.")
    return redirect(url_for('firewall'))

if __name__ == '__main__':
    app.run(debug=True)
