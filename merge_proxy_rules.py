import requests

def read_custom_rules(filename):
    with open(filename, 'r') as file:
        return file.read()

def merge_proxy_rules(url, custom_rules_str, output_filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        remote_rules = response.text
    except Exception as e:
        return f"Error fetching remote rules: {e}"

    merged_rules = remote_rules + '\\n' + custom_rules_str

    with open(output_filename, 'w') as file:
        file.write(merged_rules)

url = "https://gitlab.com/lodepuly/vpn_tool/-/raw/main/Tool/Loon/Rule/OpenAI.list"
custom_rules_str = read_custom_rules('custom_rules.txt')

merge_proxy_rules(url, custom_rules_str, 'merged_rules.txt')
