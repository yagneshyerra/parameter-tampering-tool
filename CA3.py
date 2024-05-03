import requests
import argparse

def send_request(method, url, headers=None, params=None, data=None):
    try:
        response = requests.request(method, url, headers=headers, params=params, data=data)
        return response
    except Exception as e:
        print("Error occurred:", e)
        return None

def detect_vulnerabilities(response):
    # Detect Parameter Tampering
    original_response_text = response.text
    modified_response_text = modify_response_text(original_response_text)
    if original_response_text != modified_response_text:
        print("Potential Parameter Tampering Detected!")

    # Detect Input Validation Bypass
    if "Error" in response.text:
        print("Input Validation Bypass Detected!")

    # Detect XSS
    if "<script>" in response.text:
        print("XSS Vulnerability Detected!")

    # Detect SQL Injection
    if "SQL error" in response.text:
        print("SQL Injection Vulnerability Detected!")

    # Detect Sensitive Data Exposure
    if "API_KEY" in response.text or "PASSWORD" in response.text or "EMAIL" in response.text:
        print("Sensitive Data Exposure Detected!")

def modify_response_text(original_text):
    # Modify response text to simulate parameter tampering
    modified_text = original_text.replace("example", "tampered_example")
    return modified_text

def main():
    parser = argparse.ArgumentParser(description='Parameter Tampering Tool')
    parser.add_argument('-m', '--method', choices=['GET', 'POST', 'PUT', 'DELETE'], required=True, help='HTTP method (GET, POST, PUT, DELETE)')
    parser.add_argument('-u', '--url', required=True, help='Target URL')
    parser.add_argument('-H', '--headers', nargs='*', metavar=('Header:Value'), help='Custom request headers')
    parser.add_argument('-p', '--params', nargs='*', metavar=('Param=Value'), help='URL parameters')
    parser.add_argument('-d', '--data', help='Request body data (for POST/PUT requests)')
    args = parser.parse_args()

    method = args.method
    url = args.url
    headers = {}
    params = {}
    data = args.data

    if args.headers:
        for header in args.headers:
            header_name, header_value = header.split(':', 1)
            headers[header_name.strip()] = header_value.strip()

    if args.params:
        for param in args.params:
            param_name, param_value = param.split('=', 1)
            params[param_name.strip()] = param_value.strip()

    print("Sending {} request to {}...".format(method, url))
    response = send_request(method, url, headers=headers, params=params, data=data)

    if response:
        print("\nResponse Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Body:", response.text)

        # Detect vulnerabilities in the response
        detect_vulnerabilities(response)

if __name__ == "__main__":
    main()
