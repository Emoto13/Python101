query_base_user = '''
                      CREATE TABLE IF NOT EXISTS BaseUser
                      (id INTEGER PRIMARY Key AUTOINCREMENT UNIQUE NOT NULL,
                      user_name VARCHAR(50) UNIQUE NOT NULL,
                      email VARCHAR(50) UNIQUE NOT NULL,
                      phone INTEGER NOT NULL,
                      address VARCHAR(150) NOT NULL);
                      '''

query_client = '''
                CREATE TABLE IF NOT EXISTS Client
                (base_id INTEGER UNIQUE NOT NULL,
                FOREIGN KEY (base_id) REFERENCES BaseUser(id));
                '''

query_mechanic = '''
                 CREATE TABLE IF NOT EXISTS Mechanic 
                 (base_id INTEGER UNIQUE NOT NULL,
                 title VARCHAR(50) NOT NULL,
                 FOREIGN KEY (base_id) REFERENCES BaseUser(id));
                 '''

query_vehicle = '''
                CREATE TABLE IF NOT EXISTS Vehicle
                (id INTEGER PRIMARY Key AUTOINCREMENT UNIQUE NOT NULL,
                category VARCHAR(50) NOT NULL,
                make VARCHAR(50) NOT NULL,
                model VARCHAR(50) NOT NULL,
                register_number VARCHAR(20) UNIQUE NOT NULL,
                gear_box VARCHAR(100),
                owner INTEGER NOT NULL,
                FOREIGN KEY (owner) REFERENCES Client(base_id));
                '''

query_repair_hour = '''
                    CREATE TABLE IF NOT EXISTS RepairHour
                    (id INTEGER PRIMARY Key AUTOINCREMENT UNIQUE NOT NULL,
                     date VARCHAR(15) NOT NULL,
                     start_hour VARCHAR(15) NOT NULL,
                     vehicle INTEGER,
                     bill REAL NOT NULL,
                     mechanic_service INTEGER UNIQUE NOT NULL,
                     FOREIGN KEY (vehicle) REFERENCES Vehicle(id),
                     FOREIGN KEY (mechanic_service) REFERENCES MechanicService(id));
                    '''

query_mechanic_service = '''
                        CREATE TABLE IF NOT EXISTS MechanicService 
                        (id INTEGER PRIMARY Key AUTOINCREMENT UNIQUE NOT NULL,
                        mechanic_id INTEGER NOT NULL,
                        service_id INTEGER NOT NULL,
                        FOREIGN KEY (mechanic_id) REFERENCES Mechanic(base_id),
                        FOREIGN KEY (service_id) REFERENCES Service(id));
                        '''

query_service = '''
                CREATE TABLE IF NOT EXISTS Service
                (id INTEGER PRIMARY Key AUTOINCREMENT UNIQUE NOT NULL,
                name VARCHAR(50) NOT NULL);
                 '''
queries = [query_base_user,
           query_client,
           query_mechanic,
           query_vehicle, query_repair_hour,
           query_mechanic_service,
           query_service]
