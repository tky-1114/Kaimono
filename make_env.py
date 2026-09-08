import getpass

password = getpass.getpass("Enter root password: ")

env_content = f"""DB_HOST =localhost
DB_USER =root
DB_PASSWORD ={password}
DB_NAME =shopping
"""

with open(".env", "w", encoding="utf-8") as f:
    f.write(env_content)