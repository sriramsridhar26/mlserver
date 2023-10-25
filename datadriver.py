import psycopg2

class datadriver:
    def __init__(self):
        self.host = "db-postgresql-tor1-48594-do-user-14980657-0.c.db.ondigitalocean.com"
        self.port = 25060
        self.database = "ML_DATA"
        self.user = "doadmin"
        self.password = 

    def insert(self, userid, location, timestamp, heartrate):
        try:
            conn = psycopg2.connect(
                        host = self.host,
                        port = self.port,
                        database = self.database,
                        user = self.user,
                        password = self.password
                    )
            cursor = conn.cursor()
            sql_insert = "INSERT INTO realtime (userid,location,heartrate) VALUES"
            cursor.close()
            conn.close
        except psycopg2.Error as e:
             print("Error inserting data into PostgresSQL: ",e)

    def select(self):
            try:
                conn = psycopg2.connect(
                            host = self.host,
                            port = self.port,
                            database = self.database,
                            user = self.user,
                            password = self.password
                        )
                cursor = conn.cursor()
                #select operation
                cursor.close()
                conn.close()

            except psycopg2.Error as e:
                print("Error inserting data into PostgresSQL: ",e)

    def update(self,userid,new_hr):
            try:
                conn = psycopg2.connect(
                            host = self.host,
                            port = self.port,
                            database = self.database,
                            user = self.user,
                            password = self.password
                        )
                cursor = conn.cursor()
                sql_upd = "UPDATE vitals.patientvitals SET heartrate=ARRAY_APPEND(heartrate,%s) WHERE userid=%s;"
                cursor.execute(sql_upd,(new_hr,userid))
                conn.commit()
                cursor.close()
                cursor.close()
            except psycopg2.Error as e:
                print("Error inserting data into PostgresSQL: ",e)

# dt = datadriver()
# dt.update(75,3)