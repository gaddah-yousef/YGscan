import os

target_dir = r"c:\Users\HP\Desktop\scanning\ygscan"

for root, dirs, files in os.walk(target_dir):
    if 'venv' in root or '.git' in root or 'venv_win' in root:
        continue
    for file in files:
        if file.endswith(('.py', '.md', '.txt', 'Dockerfile', '.tpl', '.html', '.json', '.yml')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace occurrences case-sensitively
                new_content = content.replace("YGSCAN", "YGSCAN")
                new_content = new_content.replace("ygscan", "ygscan")
                new_content = new_content.replace("YGscan", "YGscan")
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Modified: {filepath}")
            except Exception as e:
                pass
                
print("Content replacement complete!")
