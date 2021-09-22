import csv,sys

# #este no lo muevas, es solo el id desde el cual inicia django a guardar
# #internamente django busca el id mas grande e inicia a escribir desde ese

import random
import string

lee_users ="User-2021-02-08.csv"
lee_profiles="Profile-2021-02-08.csv"

fields=["id" , "password"   , "last_login" , "is_superuser",    "groups" , "user_permissions"    ,"username"  ,  "first_name" , "last_name" ,  "email"  , "is_staff" ,   "is_active"  , "date_joined"]
fields2=["id",  "user"   , "state"  , "city"]


def return_state(a):
    if a==0:
     return "Aguascalientes"
    if a==1:
         return "Baja California"
    if a==2:
         return "Baja California Sur"
    if a==3:
         return "Campeche"
    if a==4:
         return "Chiapas"
    if a==5:
         return "Chihuahua"
    if a==6:
         return "Coahuila"
    if a==7:
         return "Colima"
    if a==8:
         return "Distrito Federal"
    if a==9:
         return "Durango"
    if a==10:
         return "Guanajuato"
    if a==11:
         return "Guerrero"
    if a==12:
         return "Hidalgo"
    if a==13:
         return "Jalisco"
    if a==14:
         return "Estado de Mexico"
    if a==15:
         return "Michoacan"
    if a==16:
         return "Morelos"
    if a==17:
         return "Nayarit"
    if a==18:
         return "Nuevo Leon"
    if a==19:
         return "Oaxaca"
    if a==20:
         return "Puebla"
    if a==21:
         return "Queretaro"
    if a==22:
         return "Quintana Roo"
    if a==23:
         return "San Luis Potosi"
    if a==24:
         return "Sinaloa"
    if a==25:
         return "Sonora"
    if a==26:
         return "Tabasco"
    if a==27:
         return "Tamaulipas"
    if a==28:
         return "Tlaxcala"
    if a==29:
         return "Veracruz"
    if a==30:
         return "Yucatan"
    if a==31:
         return "Zacatecas" 
     


def normalize_data(lee1=lee_users,lee2=lee_profiles):
    try:
        file_read_1=open(lee1,"r")
    except Exception as e:
        raise e
        print("error leyendo el archivo de datos:"+lee1)
    try:
        file_read_2=open(lee2,"r")
    except Exception as e:
        raise e
        print("error leyendo el archivo de datos:"+lee2)

    file_write=open("a_separar.csv","w")
    csv_reader_users = csv.reader(file_read_1, delimiter=',')
    writer=csv.DictWriter(file_write,fieldnames=["id" ,"username" ,  "first_name" , "last_name" ,"state"  , "city", "last_login" ])
    writer.writeheader()
    for row in csv_reader_users: 
        file_read_2=open(lee2,"r")
        csv_reader_profiles = csv.reader(file_read_2, delimiter=',')
        for row2 in csv_reader_profiles:  
            if str(row[0])== str(row2[1]): 
                writer.writerow({"id": row[0],"username" :row[6],  "first_name" :row[7], "last_name":row[8], "state" :return_state( int(row2[2])) , "city":row2[3], "last_login":row[2] })

    file_read_1.close()
    file_read_2.close()
    file_write.close()

def split_loged_nologed_users(lee="a_separar.csv",logueados="logueados.csv",no_logueados="no_logueados.csv"):

    # fields=["id","code","validity_begins","validity_expires","license", "is_event_code"]
    # fields2=["id","code","user"]
    try:
        file_read=open(lee,"r")
    except Exception as e:
        raise e
        print("error leyendo el archivo de datos:"+lee)
    try:
        file_write=open(no_logueados,"w")
        file_write2=open(logueados,"w")
        csv_reader = csv.reader(file_read, delimiter=',')
        line_count = 0


        writer=csv.DictWriter(file_write,fieldnames=["id" ,"username" ,  "first_name" , "last_name" ,"state"  , "city", "last_login" ])
        writer2=csv.DictWriter(file_write2,fieldnames=["id" ,"username" ,  "first_name" , "last_name" ,"state"  , "city", "last_login" ])
        # writer.writeheader()
        # writer2.writeheader()
        for row in csv_reader:

                if row[6]=="":
                    # print(row)
                    writer.writerow({"id": row[0],"username" :row[1],  "first_name" :row[2], "last_name":row[3], "state" :row[4] , "city":row[5], "last_login":row[6] })
 
                else:
                    writer2.writerow({"id": row[0],"username" :row[1],  "first_name" :row[2], "last_name":row[3], "state" :row[4] , "city":row[5], "last_login":row[6] })
        file_read.close()
        file_write.close()
        file_write2.close()
    except Exception as e:
        raise e
        print("error en el archivo de escritura:"+escribe)


# normalize_data() 

split_loged_nologed_users()