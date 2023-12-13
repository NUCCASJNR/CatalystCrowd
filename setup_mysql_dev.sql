-- sql script


CREATE DATABASE IF NOT EXISTS catalystcrowd_db;
       CREATE USER IF NOT EXISTS 'catalyst_user'@'localhost' IDENTIFIED BY 'catalyst_pwd';
              GRANT ALL PRIVILEGES ON catalystcrowd_db.* TO 'catalyst_user'@'localhost';
                                      GRANT SELECT ON performance_schema.* TO 'catalyst_user'@'localhost';
FLUSH PRIVILEGES;