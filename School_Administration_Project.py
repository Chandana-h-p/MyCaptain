#School Administration Project
import csv
def write_to_csv(info):
    with open('stu_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","e-mail ID"])
        
        writer.writerow(info)
        
if __name__=='__main__':
    condition=True
    stu_num = 1
    
    while(condition):
        
        stu_info=input("Enter student information of student #{} in the format (Name Age Contact_number e-mail_ID :".format(stu_num))
        
        stu_info_list=stu_info.split(' ')
        print("\nEntered information is :\nName: {}\nAge: {}\nContact number: {}\ne-mail ID: {}".format(stu_info_list[0],stu_info_list[1],stu_info_list[2],stu_info_list[3]))
    
        correction=input("Is the entered information correct? (Y/N): ")
        if correction=="Y":
            write_to_csv(stu_info_list)
            continue_=input("Do you want to enter next student information ? (Y/N): ")
            if continue_=="Y":
                condition=True
                stu_num=stu_num+1
            elif continue_=="N":
                condition=False
        elif correction=="N":
            print("\nPlease re-enter the data!")
