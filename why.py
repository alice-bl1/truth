import os

content = """user_rights = 1
allow_change_game = 1
clear_yulia-rights = 0
else_ending = ?
listen_localhost:7312_port = false
"""

file_path = os.path.join(os.getcwd(), "semen.cfg")

with open(file_path, "w", encoding="utf-8") as file:
    file.write(content)
