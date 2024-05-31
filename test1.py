import csv
import time


import pandas as pd




class code:
    @staticmethod
    def update_csv(filename, roll, new_date):                                                            #fun
        updated_rows = []

        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  

            updated_rows.append(header)  

            for row in reader:
                rol=row[1]
                
               
                if roll==rol:
                    new_date = code.date1(True)
                    mrng = new_date + "mrng"  # Assuming this concatenation is correct
            
                    if mrng in header:  # Check if the mrng column header exists in the header list
                        row_index = header.index(mrng)
                        if row[row_index] == 'A':
                            x = code.date1(False)
                            row[row_index] = x
                        else:
                            evng = new_date + "evng"
                            if evng in header:  # Check if the evng column header exists in the header list
                                row_index = header.index(evng)
                                x = code.date1(False)
                                row[row_index] = x

                
                updated_rows.append(row)                                        

        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_rows)
   









    @staticmethod
    def date1(con): # Generates date and time                                                                   #fun
        t = time.time()
        if con:
            ft = time.strftime('%d_%m_%Y', time.localtime(t))
            return ft

        pt = time.strftime('%H:%M:%S', time.localtime(t))
  
        return pt










    @staticmethod
    def adddate(new_date): # Adds new date to CSV                                                               #fun
        csv_file = 'atten.csv'

        with open(csv_file, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)
        
        data[0].append(new_date)
        for i in range(1,len(data)):
            s=""
            data[i].append(s)
            

        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
 












    @staticmethod
    def row1(): # Checks if the date is present or not                                                       #fun
        
        csv_file = 'atten.csv'
        tim = code.date1(True)                                                                              #fun
        temp1=tim+"mrng"
        Already = True
     
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            fr = next(csv_reader)
            for i in fr:
                if temp1 == i:
                    Already = False
                 
                
            if Already:
         
                temp=code.date1(True)                                                                           #fun
                temp1=temp+"mrng"
                code.adddate(temp1) 
                temp1=temp+"evng"
                code.adddate(temp1)#fun
                code.update_column_to_A(csv_file,temp+"mrng")
                
        #add
        
      

    def update_column_to_A(csv_file, column_name):
    
        df = pd.read_csv("atten.csv")

        df[column_name] = 'A'
        df.to_csv(csv_file, index=False)











    @staticmethod
    def check(st): # Checks if username is present or not
        code.row1()
        target_column = 'Names'
        dat = code.date1(True)
        with open('atten.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                nam = row[target_column]
                rol=row["Roll"]
                name=nam+"_"+rol
                
                if st == name:
                    code.update_csv("atten.csv", rol, dat)






