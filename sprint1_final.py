from prettytable import PrettyTable

def pretty_print(indi_list, fam_list, err_list) -> None:
    write_file = open("sprint1_output.txt", "w")
    indi_chart = PrettyTable()
    fam_chart = PrettyTable()
    err_chart = PrettyTable()

    indi_chart.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Death", "Family", "Parents"]
    for key in indi_list:
        indi = indi_list[key]
        add_indi_list = [indi.get_id(), indi.get_name(), indi.get_gender(), indi.get_birthDate(),
                         indi.get_age()]
        death_info = indi.get_deathDate()
        add_indi_list.append(death_info)
        fam_id_list = []
        for fam in indi.get_family():
            fam_id_list.append(fam.get_id())
        add_indi_list.append(fam_id_list)
        if(not indi.get_parent_family()): add_indi_list.append(None)
        else: add_indi_list.append(indi.get_parent_family().get_id())
        indi_chart.add_row(add_indi_list)


    fam_chart.field_names = ["ID", "Merried", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for key in fam_list:
        fam = fam_list[key]
        add_fam_list = [fam.get_id(), fam.get_marriedDate(), fam.get_divorcedDate()]
        if(not fam.get_husband()): 
            add_fam_list.append(None)
            add_fam_list.append(None)
        else: 
            add_fam_list.append(fam.get_husband().get_id())
            add_fam_list.append(fam.get_husband().get_name())
        
        if(not fam.get_wife()):
            add_fam_list.append(None)
            add_fam_list.append(None)
        else:
            add_fam_list.append(fam.get_wife().get_id())
            add_fam_list.append(fam.get_wife().get_name())
        children_id_list = []
        for child in fam.get_children():
            children_id_list.append(child.get_id())
        add_fam_list.append(children_id_list)
        fam_chart.add_row(add_fam_list)



    err_chart.field_names = ["ID", "Error Message"]
    i = 1
    for key in err_list:
        err_chart.add_row([i, err_list[key]])
        i += 1
    
    write_file.write("Individual\n")
    write_file.write(indi_chart.get_string() + "\n")
    write_file.write("Family\n")
    write_file.write(fam_chart.get_string() + "\n")
    write_file.write("Error\n")
    if(i == 1):write_file.write("\nNo Errors found!")
    else: write_file.write(err_chart.get_string())

    write_file.close()

    


if __name__ == "__main__":
    from models import Individual
    from models import Family
    indi_1 = Individual.Individual("01")
    indi_2 = Individual.Individual("02")
    fam_1 = Family.Family("10")
    fam_2 = Family.Family("20")
    indi_1.add_to_family(fam_1)
    indi_2.add_to_family(fam_2)
    fam_1.set_husband(indi_1)
    fam_1.set_wife(indi_2)
    fam_2.set_husband(indi_2)
    fam_2.set_wife(indi_1)
    print_pretty_table([indi_1, indi_2], [fam_1, fam_2], [])
