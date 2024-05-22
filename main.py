import psycopg2
import config

def connect(query, result = False):
    try: 

        conn = psycopg2.connect(
            dbname = config.DATABASE,
            user = config.USERNAME,
            password = config.PASSWORD,
            host = config.HOSTNAME,
            
        )

        cursor = conn.cursor()
        cursor.execute(query)
        
        if result: 
            return conn.fetchall()
        
        else:
            conn.commit()
            
        
    except psycopg2.Error as e:
        print('Error connecting', e)

    finally:
        if conn:
            cursor.close()
            conn.close()
            

class Organiser:
    def __init__(self,**kwargs):
        for key, value in kwargs.items():
            setattr(self,key,value)
        
    def data_org(self):
        self.name = input('name: ')
        query = f"INSERT INTO organiser (org_name) VALUES (\'{self.name}\')"
        connect(query)
    
    @classmethod
    def data_prj(self,cls):
        prj_name = ('project name: ')
        prj_description = ('description: ')
        prj_country = ('country: ')
        prj_city = ('city: ')
        prj_date_start = ('start (enter date as MM/DD/YYYY): ')
        prj_date_end = ('end (enter date as MM/DD/YYYY): ')
        prj_skills = ('skill needed (*optional): ')
        prj_job =  ('specific job (*optional): ')
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
        
        return Organiser(name=prj_name,description=prj_description)
          
    def check_event(self, volunteer_info):
        pass
        # country
        # city
        # date_start
        # date_end
        # skills
        # job
        
        
class Volunteer:
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
        query = f'INSERT INTO volunteer (vol_fname, vol_lname, vol_country, vol_city, vol_date_start, vol_date_end, vol_job, vol_skill, vol_phone, vol_mail) VALUES (\'{vol_fname}\', \'{vol_lname}\',\'{vol_country}\',\'{vol_city}\', \'{vol_date_start}\', \'{vol_date_end}\', \'{vol_job}\', \'{vol_skill}\', \'{vol_phone}\',\'{vol_mail}\')'
        connect(query) 
        organiser=[]  
        organiser.append
        
    def get_available_vol(self,organiser):
        match_query=f'''SELECT vol_country FROM volunteer WHERE 
        vol_country = {organiser['country']}
        AND {organiser['city']} = vol_city
        AND {organiser['skills']} = vol_skill
        AND {organiser['job']} = vol_job
        AND {organiser['start_date']} >= vol_start_date
        AND {organiser['end_date']} <= vol_end_date'''

        print(connect(match_query,result=True))
        

class User(Organiser,Volunteer):
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
 
a = Volunteer("p")
a.get_info()

org1 = Organiser(city=)

