import psycopg2
import config

def connect(query):
    try: 

        conn = psycopg2.connect(
            dbname = config.DATABASE,
            user = config.USERNAME,
            password = config.PASSWORD,
            host = config.HOSTNAME,
            
        )

        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except psycopg2.Error as e:
        print('Error connecting', e)

    finally:
        if conn:
            cursor.close()
            conn.close()

class organiser:
    def __init__(self,name):
        self.name=name
        
        
    def data_org(self):
        self.name = input('name: ')
        query = f"INSERT INTO organiser (org_name) VALUES (\'{self.name}\')"
        connect(query)
    
    def data_prj(self):
        prj_name = input('project name: ')
        prj_description = input('description: ')
        prj_country = input('country: ')
        prj_city = input('city: ')
        prj_date_start = input('start (enter date as MM/DD/YYYY): ')
        prj_date_end = input('end (enter date as MM/DD/YYYY): ')
        prj_skills = input('skill needed (*optional): ')
        prj_job = input ('specific job (*optional): ')
        while True:
            prj_flight = input('Paying for the flight:\n(1) yes\n(2) no\n')
            prj_flight=='1'
            if prj_flight == '1' or prj_flight == '2':
                break
            else:
                print('Invalid answer')
        while True:
            prj_house = input('Paying for the house:\n(1) yes\n(2) no\n')
            if prj_house == '1' or prj_flight == '2':
                break
            else:
                print('Invalid answer')
        while True:
            prj_food = input('Paying for the food during the project:\n(1) yes\n(2) no\n')
            if prj_food == '1' or prj_food == '2':
                break
            else:
                print('Invalid answer')
        while True:
            prj_bus = input('Paying for the travel to the project:\n(1) yes\n(2) no\n')
            if prj_bus == '1' or prj_flight == '2':
                break
            else:
                print('Invalid answer')
        query = f'INSERT into project (prj_name, prj_description, prj_country, prj_city, prj_date_start, prj_date_end, prj_skills, prj_job, prj_flight, prj_house, prj_food, prj_bus, org_id) VALUES (\'{prj_name}\', \'{prj_description}\',\'{prj_country}\',\'{prj_city}\', \'{prj_date_start}\', \'{prj_date_end}\', \'{prj_skills}\', \'{prj_job}\', \'{prj_flight}\', \'{prj_house}\', \'{prj_food}\', \'{prj_bus}\', (SELECT org_id FROM organiser where org_name = \'{self.name}\'))'       
        connect(query)    

class volunteer:
    def __init__(self,name):
        self.name=name
        
    def vol_data(self):
        vol_fname = input('first name: ')
        vol_lname = input('last name: ')
        vol_country = input('country: ')
        vol_city = input('city: ')
        vol_date_start = input('start (enter date as MM/DD/YYYY): ')
        vol_date_end = input('end (enter date as MM/DD/YYYY): ')
        vol_job = input ('job (*optional): ')
        vol_skill = input('skill (*optional): ')
        vol_phone = input('phone number: ')
        vol_mail = input('email: ')
        while True:
            vol_flight = input('Paying for the flight:\n(1) yes\n(2) no\n(3) I don\'t care\n')
            vol_flight=='1'
            if vol_flight == '1' or vol_flight == '2' or vol_flight == '3':
                break
            else:
                print('Invalid answer')
        while True:
            vol_house = input('Paying for the house:\n(1) yes\n(2) no\n(3) I don\'t care\n')
            if vol_house == '1' or vol_flight == '2' or vol_flight == '3':
                break
            else:
                print('Invalid answer')
        while True:
            vol_food = input('Paying for the food during the project:\n(1) yes\n(2) no\n(3) I don\'t care\n')
            if vol_food == '1' or vol_food == '2' or vol_flight == '3':
                break
            else:
                print('Invalid answer')
        while True:
            vol_bus = input('Paying for the travel to the project:\n(1) yes\n(2) no\n(3) I don\'t care\n')
            if vol_bus == '1' or vol_flight == '2' or vol_flight == '3':
                break
            else:
                print('Invalid answer')
        query = f'INSERT INTO volunteer (vol_fname, vol_lname, vol_country, vol_city, vol_date_start, vol_date_end, vol_job, vol_skill, vol_phone, vol_mail, vol_flight, vol_house, vol_food, vol_bus) VALUES (\'{vol_fname}\', \'{vol_lname}\',\'{vol_country}\',\'{vol_city}\', \'{vol_date_start}\', \'{vol_date_end}\', \'{vol_job}\', \'{vol_skill}\', \'{vol_phone}\',\'{vol_mail}\', \'{vol_flight}\', \'{vol_house}\', \'{vol_food}\', \'{vol_bus}\')'       
        connect(query)    

class user(organiser,volunteer):
    def __call__(self,user):
        self.user=user
    def choice(self):
        self.user = int(input(f'(1) organiser\n(2) volunteer\n'))
        if self.user == 1:
            self.data_org()
            self.data_prj()
        elif self.user == 2:
            self.vol_data()
        else:
            print('invalid answer')
            
  

p=user('p')
p.choice()


