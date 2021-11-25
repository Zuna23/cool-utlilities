import sys
import os
import subprocess
import pandas as pd
import csv


def Host_Name_Ping(host_path_file):

     #empty arrays which we will convert to dictionaries later

     successful = []
     unsuccessful =[]

     scriptDir = sys.path[0]
     hosts = os.path.join(scriptDir,host_path_file)
     hostsFile = open(hosts,"r")

     lines = hostsFile.readlines()

     for line in lines:
         line = line.strip(' ')
         line = line.strip('\n')
         line = line.strip('\t')
         line = line.strip(' ,')


         param = '-n'

         command = ['ping',param,'3',line]

         if subprocess.call(command)==0:
             successful.append(line)
         else:
             unsuccessful.append(line)

         csv_columns = ['Successful','Unsuccessful','Success_Count','Fail_Count']
         dict_data = [{'Successful':successful,'Unsuccessful':unsuccessful,'Success_Count':len(successful),'Fail_Count':len(unsuccessful)}]
         
         csv_file = "Hosts_results.csv"
         try:
               with open(csv_file, 'w',newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)
         except IOError:
            print("I/O error")


Host_Name_Ping("C:\\Users\\T440P\\Documents\\Hosts.txt")          