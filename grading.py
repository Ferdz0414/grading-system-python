import tkinter as tk
import gradingsystem
from tkinter import messagebox



#Gobal Variable
userid = "Admin"
password = "Admin1234"
attemp = 0




def login():


    userid = "Admin"
    password = "Admin1234"

    global attemp
    userid_input = userid_entry.get()
    password_input = password_entry.get()

    if userid_input == userid and password_input == password:
        messagebox.showinfo(title="Login Success", message="Log in Successfully.")
        login_window.destroy()
        grading_proceed()

        #Validated dito kung ilan na try kana sa pag input ng password
    else:
        ##kapg hindi match yun password mo papaulitin ka ng tatlong beses
        
        attemp +=1
        remaining = 3 - attemp
        messagebox.showinfo(title="Invalid Login", message="Your Password or User ID does not match.")

        if attemp == 3:

       

            lock_ui()
            

def lock_ui():
    
    #lock yun system ng 3 seconds
    messagebox.showinfo(title="Lock System", message="So many Try to log in")
    userid_entry.config(state="disabled")
    password_entry.config(state="disabled")
    btn.config(state="disabled")

    login_window.after(3000, login_window.destroy)
                
    

login_window = tk.Tk()
login_window.title("Grading System")
login_window.geometry("1000x500")
login_window.configure(bg="#333333")

#Log in Page

frame = tk.Frame(login_window, bg="#333333")
frame.pack(pady=20)

label = tk.Label(frame, text="Login", bg="#333333", font=("Arial", 30))
userid_label = tk.Label(frame, text="User ID", bg="#333333", font=("Arial", 15))
userid_entry = tk.Entry(frame, font=("Arial", 15))
password_label = tk.Label(frame, text="Password", bg="#333333", font=("Arial", 15))
password_entry = tk.Entry(frame, show="*", font=("Arial", 15))

#Input Userid and Password
label.grid(row=0, column=0, columnspan=2, pady=40, padx=100)
userid_label.grid(row=1, column=0, pady=10, padx=20)
userid_entry.grid(row=1, column=1, pady=5, padx=20)
password_label.grid(row=2, column=0, pady=5, padx=20)
password_entry.grid(row=2, column=1, pady=5, padx=20)
      
btn = tk.Button(frame, text="Log In", font=("Arial", 15), command=login)
btn.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

#Grading Process

def grading_proceed():

    global studentname_entry, yearlevel_entry
    global pre_quiz_entry, pre_activity_entry, pre_assignment_entry, pre_exam_entry
    global mid_quiz_entry, mid_activity_entry, mid_assignment_entry, mid_exam_entry
    global final_quiz_entry, final_activity_entry, final_assignment_entry, final_exam_entry


    gradeprocess = tk.Tk()
    gradeprocess.title("Grade Process")
    gradeprocess.geometry("1000x500")
    gradeprocess.configure(bg ="#333333")

    title_label = tk.Label(gradeprocess, text="Student Information", bg="#333333",fg="white", font=("Arial", 35) ,pady=10,padx=5)
    title_label.grid(row=0, column=2, columnspan=2, pady=40, padx=100)

    studentname_label = tk.Label(gradeprocess, text="Student Name: ", bg="#333333", font=("Arial", 15) ,pady=10,padx=5)
    studentname_entry = tk.Entry(gradeprocess, font=("Arial", 15))
    studentname_label.grid(row=1, column=0, pady=10, padx=7)
    studentname_entry.grid(row=1, column=1, pady=5, padx=7)
   

    yearlevel_label = tk.Label(gradeprocess, text="Year Level: ", bg="#333333", font=("Arial", 15))
    yearlevel_entry = tk.Entry(gradeprocess, font=("Arial", 15))
    yearlevel_label.grid(row=2, column=0, pady=5, padx=15)
    yearlevel_entry.grid(row=2, column=1, pady=5, padx=15)


    #PRELIM
    
    pre_quiz_label = tk.Label(gradeprocess, text="Prelim Quiz: ", bg="#333333", font=("Arial", 15))
    pre_quiz_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    pre_quiz_label.grid(row=1, column=2, pady=0, padx=2, sticky="e")
    pre_quiz_entry.grid(row=1, column=3, pady=0, padx=2, sticky="w")

    pre_activity_label = tk.Label(gradeprocess, text="Prelim Activity: ", bg="#333333", font=("Arial", 15))
    pre_activity_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    pre_activity_label.grid(row=2, column=2, pady=1, padx=2, sticky="e")
    pre_activity_entry.grid(row=2, column=3, pady=2, padx=2, sticky="w")

    pre_assignment_label = tk.Label(gradeprocess, text="Prelim Assignment: ", bg="#333333", font=("Arial", 15))
    pre_assignment_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    pre_assignment_label.grid(row=3, column=2, pady=1, padx=2, sticky="e")
    pre_assignment_entry.grid(row=3, column=3, pady=1, padx=2, sticky="w")

    pre_exam_label = tk.Label(gradeprocess, text="Prelim Exam: ", bg="#333333", font=("Arial", 15))
    pre_exam_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    pre_exam_label.grid(row=4, column=2, pady=1, padx=2, sticky="e")
    pre_exam_entry.grid(row=4, column=3, pady=1, padx=2, sticky="w")


    #MIDTERM

    mid_quiz_label = tk.Label(gradeprocess, text="Midterm Quiz: ", bg="#333333", font=("Arial", 15))
    mid_quiz_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    mid_quiz_label.grid(row=5, column=0, pady=5, padx=7, sticky="e")
    mid_quiz_entry.grid(row=5, column=1, pady=5, padx=7, sticky="w")

    mid_activity_label = tk.Label(gradeprocess, text="Midterm Activity: ", bg="#333333", font=("Arial", 15))
    mid_activity_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    mid_activity_label.grid(row=6, column=0, pady=5, padx=7, sticky="e")
    mid_activity_entry.grid(row=6, column=1, pady=5, padx=7, sticky="w")

    mid_assignment_label = tk.Label(gradeprocess, text="Midterm Assignment: ", bg="#333333", font=("Arial", 15))
    mid_assignment_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    mid_assignment_label.grid(row=7, column=0, pady=5, padx=7, sticky="e")
    mid_assignment_entry.grid(row=7, column=1, pady=5, padx=7, sticky="w")

    mid_exam_label = tk.Label(gradeprocess, text="Midterm Exam: ", bg="#333333", font=("Arial", 15))
    mid_exam_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    mid_exam_label.grid(row=8, column=0, pady=0, padx=7, sticky="e")
    mid_exam_entry.grid(row=8, column=1, pady=1, padx=7, sticky="w")



    #FINAL

    final_quiz_label = tk.Label(gradeprocess, text="FinalQuiz: ", bg="#333333", font=("Arial", 15))
    final_quiz_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    final_quiz_label.grid(row=6, column=2, pady=5, padx=7, sticky="e")
    final_quiz_entry.grid(row=6, column=3, pady=5, padx=7, sticky="w")

    final_activity_label = tk.Label(gradeprocess, text="Final Activity: ", bg="#333333", font=("Arial", 15))
    final_activity_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    final_activity_label.grid(row=7, column=2, pady=5, padx=7, sticky="e")
    final_activity_entry.grid(row=7, column=3, pady=5, padx=7, sticky="w")

    final_assignment_label = tk.Label(gradeprocess, text="Final Assignment: ", bg="#333333", font=("Arial", 15))
    final_assignment_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    final_assignment_label.grid(row=8, column=2, pady=5, padx=7, sticky="e")
    final_assignment_entry.grid(row=8, column=3, pady=5, padx=7, sticky="w")

    final_exam_label = tk.Label(gradeprocess, text="Final Exam: ", bg="#333333", font=("Arial", 15))
    final_exam_entry = tk.Entry(gradeprocess, font=("Arial", 8))
    final_exam_label.grid(row=9, column=2, pady=5, padx=7, sticky="e")
    final_exam_entry.grid(row=9, column=3, pady=5, padx=7, sticky="w")

    btn_grade_process = tk.Button(gradeprocess, text="Grading Process", font=("Arial", 15), command=gradesprocess)
    btn_grade_process.grid(row=20, column=0, columnspan=2, pady=10, padx=20)


    
    



def gradesprocess():
    
    stdname = studentname_entry.get()
    year = yearlevel_entry.get()
    prequiz = pre_quiz_entry.get()
    preactivity = pre_activity_entry.get()
    preassignment = pre_assignment_entry.get()
    preexam = pre_exam_entry.get()
    midquiz = mid_quiz_entry.get()
    midactivity = mid_activity_entry.get()
    midassignment = mid_assignment_entry.get()
    midexam = mid_exam_entry.get()
    finalquiz = final_quiz_entry.get()
    finalactivity = final_activity_entry.get()
    finalassignment = final_assignment_entry.get()
    finalexam = final_exam_entry.get()
    
    if (not stdname or not year or not prequiz.isdigit() or not preactivity.isdigit() or not preassignment.isdigit() or
    not preexam.isdigit() or not midquiz.isdigit() or not midactivity.isdigit() or not midassignment.isdigit() or not midexam.isdigit()
    or not finalquiz.isdigit() or not finalactivity.isdigit() or not finalassignment.isdigit() or not finalexam.isdigit()):
        
        messagebox.showinfo(title="Error", message="Fill out all fields Correctly")

        return
    else:
        messagebox.showinfo(title="Successfully Process", message="Successfully Grades Computation")
        

    prelim = gradingsystem.prelim(int(prequiz), int(preactivity), int(preassignment), int(preexam))/4
    midterm = gradingsystem.midterm(int(midquiz), int(midactivity), int(midassignment), int(midexam))/4
    final = gradingsystem.final(int(finalquiz), int(finalactivity), int(finalassignment), int(finalexam))/4
    gwa = gradingsystem.grades(prelim,midterm,final)/3
    passing = gwa



    displaygrading(stdname, year,prequiz,preactivity,preassignment,preexam,midquiz,midactivity,midassignment,midexam,finalquiz,finalactivity,finalassignment,finalexam,prelim,midterm,final,gwa,passing)

def displaygrading(stdname, year,prequiz,preactivity,preassignment,preexam,midquiz,midactivity,midassignment,midexam,finalquiz,finalactivity,finalassignment,finalexam,prelim,midterm,final,gwa,passing):
    gradingdisplay_window = tk.Toplevel()
    gradingdisplay_window.title("Grades Display System")
    gradingdisplay_window.geometry("1000x500")
    gradingdisplay_window.configure(bg="#333333")

    if 75<= passing <=99:
        passing="You Pass"
    elif 65<= passing <=74:
        passing="You Failed"
    else:
         passing="Error"

    grading_summary = (
        f"===============================\n"
        f"Student Information Card\n"
        f"Student Name: {stdname}\n"
        f"Student Year: {year}\n"
        f"===============================\n"
        f"Prelim\n"
        f"Prelim Quiz: {prequiz}\n"
        f"Prelim Activity: {preactivity}\n"
        f"Prelim Assignment: {preassignment}\n"
        f"Prelim Exam: {preexam}\n"
        f"Prelim Grades: {prelim}\n"
        f"===============================\n"
        f"Midterm\n"
        f"Midterm Quiz: {midquiz}\n"
        f"Midterm Activity: {midactivity}\n"
        f"Midterm Assignment: {midassignment}\n"
        f"Midterm Exam: {midexam}\n"
        f"Midterm Grades: {midterm}\n"
        f"===============================\n"
        f"Final\n"
        f"Final Quiz: {finalquiz}\n"
        f"Final Activity: {finalactivity}\n"
        f"Final Assignment: {finalassignment}\n"
        f"Final Exam: {finalexam}\n"
        f"Final Grades: {final}\n"
        f"===============================\n"
        f"General Average Weight\n"
        f"General Average Weight: {gwa}\n"
        f"General Average Result: {passing}\n"
        
        
    )

    #Output of Grading
    tk.Label(gradingdisplay_window, text="Grades Computation", font=("Arial", 30), bg="#333333", fg="white", pady=10, padx=100).pack(pady=10)
    tk.Label(gradingdisplay_window, text=grading_summary, bg="#333333", fg="white",font=("Arial", 13), justify="left").pack(pady=10)


    
        


login_window.mainloop()
        

            


