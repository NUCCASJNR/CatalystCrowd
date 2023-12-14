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

- Set the necessary environment variables needed in the ~/.bashrc file

```shell
echo "export CATALYST_DB='catalystcrowd_db'" >> ~/.bashrc
echo "export CATALYST_USER='catalyst_user'" >> ~/.bashrc
echo "export CATALYST_PWD='catalyst_pwd'" >> ~/.bashrc
echo "export CATALYST_HOST='localhost'" >> ~/.bashrc
```

- Source the ~/.bashrc file

```shell
source ~/.bashrc
```