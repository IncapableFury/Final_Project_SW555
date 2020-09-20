from prettytable import PrettyTable
import datetime

##change the format from "day month(in str type) year" to "year-month-day"
def change_date_format(month_list, str_input):
    date_list = str_input.split(" ")
    date_list[1] = str(month_list.index(date_list[1])+1)
    temp = date_list[0]
    date_list[0] = date_list[2]
    date_list[2] = temp
    return "-".join(date_list)


##no build-in age variable, calculate age
def get_age(month_list, now_time, str_input):
    date_list = change_date_format(month_list, str_input).split("-")
    Age = now_time.year - int(date_list[0])
    if(now_time.month - int(date_list[1]) < 0): Age -= 1
    if(now_time.month - int(date_list[1]) == 0 and now_time.day - int(date_list[2]) < 0): Age -= 1
    return Age

##read file
ged_file = open('Jiashu_Wang.ged', "r")
##get now date
now_time = datetime.datetime.now()

#swap key from reading files
swap_list = ["INDI", "FAM"]
#map of the symbol month to its index + 1
month_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

##create two pretty table for output
indi_chart = PrettyTable()
indi_chart.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

family_chart = PrettyTable()
family_chart.field_names = ["ID", "Merried", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

##flags for first INDI, FAM
##flags for birthday, death, marry, divorse, because ged has all the key word into two lines of input
##EX: input looks like "MARR \n DATE xx xxx xxxx"
INDI_flag = False
FAM_flag = False
birt_flag = False
death_flag = False
marr_flag = False
div_flag = False

##variable for saving each person, all its spouse and children
indi = {}
famc_list = []
fams_list = []
##save all data of people, for future class + family data
all_indi = []

##variable for saving each families, all its children
fam = {}
children_list = []
##save all data of families, for future class
all_fam = []

##readfile line by line
for line in ged_file:

    ##read line, delete \n, swap if in swap list, bind everything after key
    split_part = line.split(" ")
    split_part[-1] = split_part[-1][:-1]

    if(len(split_part) >= 3 and split_part[2] in swap_list):
        tag = split_part[2]
        split_part[2] = split_part[1]
        split_part[1] = tag

    if(len(split_part[2:]) != 0):
        out_line = " ".join(split_part[2:])
        split_part[2] = out_line

    ##saving INDI 
    if(split_part[1] == 'INDI' or INDI_flag):
        ##If hit INDI for the first time
        if(not INDI_flag):
            INDI_flag = True
            FAM_flag = False
            indi = {}
            famc_list = []
            fams_list = []
            indi['ID'] = split_part[2][1:-1]
            continue
        ##if hit INDI from second time forward
        if(split_part[1] == "INDI"):
            all_indi.append(indi)
            input_line = []
            input_line.append(indi['ID'])
            input_line.append(indi['Name'])
            try:
                input_line.append(indi['Gender'])
            except:
                input_line.append("NA")
            input_line.append(indi['Birthday'])
            input_line.append(indi['Age'])
            try:
                input_line.append(indi['Alive'])
            except:
                input_line.append(True)
            try:
                input_line.append(indi['Death'])
            except:
                input_line.append("NA")


            if(len(famc_list) != 0):
                input_line.append(famc_list)
                famc_list = []
            else: input_line.append("NA")
            if(len(fams_list) != 0):
                input_line.append(fams_list)
                fams_list = []
            else: input_line.append("NA")
            indi_chart.add_row(input_line)
            indi = {}
            indi['ID'] = split_part[2][1:-1]
        ##saving info into indi dictionary
        if(split_part[1] == 'NAME'): indi['Name'] = split_part[2]
        if(split_part[1] == 'SEX'): indi['Gender'] = split_part[2]
        if(split_part[1] == 'BIRT'): birt_flag = True
        if(split_part[1] == 'DEAT'):
            indi['Alive'] = False
            death_flag = True
        if(split_part[1] == 'DATE'): 
            if(birt_flag):
                indi['Birthday'] = change_date_format(month_list, split_part[2])
                indi['Age'] = get_age(month_list, now_time, split_part[2])
                birt_flag = False
                death_flag = False
            if(death_flag):
                indi['Death'] = change_date_format(month_list, split_part[2])
                birth_flag = False
                death_flag = False
        if(split_part[1] == 'SEX'): indi['Gender'] = split_part[2]
        if(split_part[1] == 'FAMC'): famc_list.append(split_part[2][1:-1])
        if(split_part[1] == 'FAMS'): fams_list.append(split_part[2][1:-1])

    ##saving FAM
    if(split_part[1] == 'FAM' or FAM_flag):
        ##hit FAM for the first time
        if(not FAM_flag):
            FAM_flag = True
            INDI_flag = False
            fam = {}
            children_list = []
            fam['ID'] = split_part[2][1:-1]
            continue
        ##hit FAM from second time forward
        if(split_part[1] == "FAM"):
            all_fam.append(fam)
            input_line = []
            input_line.append(fam['ID'])
            try: 
                input_line.append(fam['Married'])
            except: 
                input_line.append("No date given")
            try: 
                input_line.append(fam['Divorced'])
            except: 
                input_line.append("NA")
            try:
                input_line.append(fam['Husband ID'])
            except:
                input_line.append("ER")
            try:
                input_line.append(fam['Husband Name'])
            except:
                input_line.append("Does not Exist")
            try:
                input_line.append(fam['Wife ID'])
            except:
                input_line.append("ER")
            try:
                input_line.append(fam['Wife Name'])
            except:
                input_line.append("Does not Exist")
            if(len(children_list) == 0): input_line.append("NA")
            else: input_line.append(children_list)

            family_chart.add_row(input_line)
            fam = {}
            children_list = []
            fam['ID'] = split_part[2][1:-1]


        ##saving info into fam dictionary
        
        if(split_part[1] == "HUSB"):
            fam["Husband ID"] = split_part[2][1:-1]
            for person in all_indi:
                if(person['ID'] == split_part[2][1:-1]):
                    fam['Husband Name'] = person['Name']
        if(split_part[1] == "WIFE"): 
            fam["Wife ID"] = split_part[2][1:-1]
            for person in all_indi:
                if(person['ID'] == split_part[2][1:-1]):
                    fam['Wife Name'] = person['Name']
        if(split_part[1] == "MARR"): marr_flag = True
        if(split_part[1] == "DIV"): div_flag = True
        if(split_part[1] == 'DATE'):
            if(marr_flag):
                fam["Married"] = change_date_format(month_list, split_part[2])
                marr_flag = False
                div_flag = False
            if(div_flag):
                fam["Divorced"] = change_date_format(month_list, split_part[2])
                marr_flag = False
                div_flag = False
        if(split_part[1] == "CHIL"): children_list.append(split_part[2][1:-1])


if __name__ == "__main__":
    print("Individuals")
    print(indi_chart)
    print("Families")
    print(family_chart)