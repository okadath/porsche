import csv,sys

# #este no lo muevas, es solo el id desde el cual inicia django a guardar
# #internamente django busca el id mas grande e inicia a escribir desde ese

import random
import string

def get_random_code():
    a=""
    a=random.choice(string.ascii_letters).upper()
    a=a+str(random.randint(2, 7))
    for x in range(0,2):
        num1 = random.randint(0, 9)
        a=a+str(num1)
    # print(a)
    return a

# #users
from django.contrib.auth.hashers import PBKDF2PasswordHasher
hasher = PBKDF2PasswordHasher()



fields=["id","password","last_login","is_superuser","groups","user_permissions","username","first_name","last_name","email", "is_staff", "is_active","date_joined"]
# print(sys.argv[1])


def generate_data_from_csv(init_seed,lee="test_users.csv",escribe="test_users_feed_db.csv"):
    try:
        file_read=open(lee,"r")
    except Exception as e:
        raise e
        print("error leyendo el archivo de datos:"+lee)
    try:
        file_write=open(escribe,"w")
        csv_reader = csv.reader(file_read, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                writer=csv.DictWriter(file_write,fieldnames=fields)
                writer.writeheader()
                line_count += 1
            else:
                # print("asd:"+row[0]+"-"+row[4])
                # mail=>pass
                password = hasher.encode(password=row[3], salt='salt', iterations=150000)
                writer.writerow({"id":init_seed+line_count,"password":password, "last_login":"","is_superuser":0,"groups":"","user_permissions":"","username":row[3],"first_name":row[2],"last_name":"","email":row[1], "is_staff":0, "is_active":1,"date_joined":""})
                line_count += 1
        # print(line_count)
        file_read.close()
        file_write.close()
    except Exception as e:
        raise e
        print("error en el archivo de escritura:"+escribe)


def generate_new_codes(init_seed,num,escribe="new_codes.csv"):
    fields=["id","code","validity_begins","validity_expires","license", "is_event_code"]

    try:
        file_write=open(escribe,"w")
        # csv_reader = csv.reader(file_read, delimiter=',')
        for x in range(0,num):
            if x == 0:
                writer=csv.DictWriter(file_write,fieldnames=fields)
                writer.writeheader()
            else:
                code=get_random_code()
                writer.writerow({"id":init_seed+x,"code":code, "validity_begins":"2020-11-01","validity_expires":"2020-11-30","license":1,"is_event_code":1})
        file_write.close()
    except Exception as e:
        raise e
        print("error en el archivo de escritura:"+escribe)

def generate_codes_usercodes(init_seed,lee="test_users_feed_db.csv",escribe="codes.csv",escribe_u_c="user_codes.csv"):

    fields=["id","code","validity_begins","validity_expires","license", "is_event_code"]
    fields2=["id","code","user"]
    try:
        file_read=open(lee,"r")
    except Exception as e:
        raise e
        print("error leyendo el archivo de datos:"+lee)
    try:
        file_write=open(escribe,"w")
        file_write2=open(escribe_u_c,"w")
        csv_reader = csv.reader(file_read, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:

                writer=csv.DictWriter(file_write,fieldnames=fields)
                writer2=csv.DictWriter(file_write2,fieldnames=fields2)
                writer.writeheader()
                writer2.writeheader()
                line_count += 1
            else:
                # print("asd:"+row[0]+"-"+row[4])
                # mail=>pass
                # password = hasher.encode(password=row[3], salt='salt', iterations=150000)
                writer.writerow({"id":init_seed+line_count,"code":row[6], "validity_begins":"2020-11-01","validity_expires":"2020-11-30","license":1,"is_event_code":1})
                writer2.writerow({"id":init_seed+line_count,"code":init_seed+line_count,"user":row[0]}) 
                line_count += 1
        # print(line_count)
        file_read.close()
        file_write.close()
        file_write2.close()
    except Exception as e:
        raise e
        print("error en el archivo de escritura:"+escribe)


init_seed=100

# generate_codes_usercodes(init_seed)
init_seed=init_seed+50
generate_new_codes(init_seed,30)