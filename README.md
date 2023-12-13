# A crowdfunding platform built with django



- Create a virtual environment and install the required packages

```bash
python3 -m venv venv_name
```

- Activate the virtual enviroment

```bash
source venv_name/bin/activate
```
- Install the requirements 
```bash
pip install -r requirements.txt
```

- Setup the Mysql User and database

```sql
cat setup_mysql_dev.sql | sudo mysql -p
```