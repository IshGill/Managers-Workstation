from tkinter import*
import tkinter.messagebox
import datetime
import time
import random
import os
import tempfile
import Managers_Work_Station_BE

# ------------------#
#Managers data class
# ------------------#
class Manager:
    def __init__(self, head):
        self.head = head
        self.head.title("Managers Workstation")
        self.head.geometry("1361x635+0+0")
        self.head['background'] = "pale goldenrod"
        # -----------------------------------------#
        #Border of GUI using RIDGE border decoration
        # -----------------------------------------#
        mainFrame = Frame(self.head, bd=10, width=1350, height=700, bg="pale goldenrod",relief=RIDGE)
        mainFrame.grid()
        # -------------------------#
        #Outermost frames for the GUI
        # -------------------------#
        topFrame1 = Frame(mainFrame, bd=7, width=1340, height=50, relief=RIDGE)
        topFrame1.grid(row=2, column=0)
        topFrame2 = Frame(mainFrame, bd=7, width=1340, height=100, relief=RIDGE)
        topFrame2.grid(row=1, column=0)
        topFrame3 = Frame(mainFrame, bd=7, width=1340, height=500, relief=RIDGE)
        topFrame3.grid(row=0, column=0)
        # -------------------------#
        #Inner frames for the GUI
        #-------------------------#
        #LEFT SECTION FRAMES
        #padx puts some space between the buttons (padding)
        leftFrame = Frame(topFrame3, bd=5, width=1340, height=400, padx=2, bg="pale goldenrod", relief=RIDGE)
        leftFrame.pack(side=LEFT)
        leftFrame1 = Frame(leftFrame, bd=5, width=600, height=180, padx=4, pady=4, bg="pale goldenrod", relief=RIDGE)
        leftFrame1.pack(side=TOP)
        leftFrame2 = Frame(leftFrame, bd=5, width=600, height=180, padx=2, bg="pale goldenrod", relief=RIDGE)
        leftFrame2.pack(side=TOP)
        leftFrame2Left = Frame(leftFrame2, bd=5, width=300, height=170, padx=2, bg="pale goldenrod", relief=RIDGE)
        leftFrame2Left.pack(side=LEFT)
        leftFrame2Right = Frame(leftFrame2, bd=5, width=300, height=170, padx=2, bg="pale goldenrod", relief=RIDGE)
        leftFrame2Right.pack(side=RIGHT)

        #RIGHT SECTION FRAMES
        rightFrame1 = Frame(topFrame3, bd=5, width=320, height=400, padx=2, bg="pale goldenrod", relief=RIDGE)
        rightFrame1.pack(side=RIGHT)
        rightFrame1a = Frame(rightFrame1, bd=5, width=310, height=300, padx=2, bg="pale goldenrod", relief=RIDGE)
        rightFrame1a.pack(side=TOP)
        rightFrame2 = Frame(topFrame3, bd=5, width=300, height=400, padx=2, bg="pale goldenrod", relief=RIDGE)
        rightFrame2.pack(side=RIGHT)
        rightFrame2a = Frame(rightFrame2, bd=5, width=280, height=50, padx=2, bg="pale goldenrod", relief=RIDGE)
        rightFrame2a.pack(side=TOP)
        rightFrame2b = Frame(rightFrame2, bd=5, width=280, height=180, padx=2, bg="pale goldenrod", relief=RIDGE)
        rightFrame2b.pack(side=TOP)
        rightFrame2c = Frame(rightFrame2, bd=5, width=280, height=100, padx=2, bg="pale goldenrod", relief=RIDGE)
        rightFrame2c.pack(side=TOP)
        rightFrame2d = Frame(rightFrame2, bd=5, width=280, height=50, padx=2, bg="pale goldenrod", relief=RIDGE)
        rightFrame2d.pack(side=TOP)

        # -----------------------------------------#
        #Database Variables
        # -----------------------------------------#
        global managers_variables
        firstname = StringVar()
        surname = StringVar()
        address = StringVar()
        reference = StringVar()
        mobile = StringVar()
        base_salary = IntVar()
        overtime = IntVar()
        holiday_pay = IntVar()
        grosspay = StringVar()
        netpay = StringVar()
        tax = StringVar()
        kiwisaver = StringVar()
        deductions = StringVar()
        payday = StringVar()
        taxPeriod = StringVar()
        IRDnumber = StringVar()
        taxablePay = StringVar()
        kiwisaverPay = StringVar()
        otherPaymentsDue = IntVar()
        taxCode = StringVar()
        studentLoan = StringVar()
        ACC = StringVar()
        ACC_levy = StringVar()
        gender = StringVar()
        email_address = StringVar()
        # -----------------------------------------#
        # Functions
        # -----------------------------------------#
        # Function for the adding data button in the program
        def input_data():
            if len(reference.get()) != 0:
                Managers_Work_Station_BE.add_employee_record(reference.get(), firstname.get(), surname.get(), address.get(), email_address.get(), mobile.get(),
                                                        IRDnumber.get(), studentLoan.get(), tax.get(), kiwisaver.get(), deductions.get(), netpay.get(), grosspay.get())
                employee_variable.delete(0, END)
                employee_variable.insert(END, (reference.get(), firstname.get(), surname.get(), address.get(), email_address.get(), mobile.get(),\
                                                IRDnumber.get(), studentLoan.get(), tax.get(), kiwisaver.get(), deductions.get(), netpay.get(), grosspay.get()))

        # Function for the displaying the data
        def display_data():
            employee_variable.delete(0, END)
            for row in Managers_Work_Station_BE.view_data():
                employee_variable.insert(END,row,str(""))

        # Function for the deleting the inputted data
        def del_data():
            global managers_variables
            if len(reference.get()) != 0:
                display_data()

        # Function for the search for previous data added
        def search_data():
            employee_variable.delete(0, END)
            for i in Managers_Work_Station_BE.search_records(reference.get(), firstname.get(), surname.get(),
                                                         address.get(), email_address.get(), mobile.get(), IRDnumber.get(), studentLoan.get(), tax.get(), kiwisaver.get(),
                                                         netpay.get(), grosspay.get()):
                employee_variable.insert(END,i,str(""))

        # Function for the updating the variables stored in references
        def update():
            if len(reference.get()) != 0:
                Managers_Work_Station_BE.add_employee_record(reference.get(), firstname.get(), surname.get(),
                                                         address.get(), email_address.get(), mobile.get(), IRDnumber.get(), studentLoan.get(), tax.get(), kiwisaver.get(),
                                                         netpay.get(), grosspay.get())
                employee_variable.delete(0, END)
                employee_variable.insert(END, (reference.get(), firstname.get(), surname.get(),
                address.get(), email_address.get(), mobile.get(), IRDnumber.get(), studentLoan.get(), tax.get(), kiwisaver.get(),
                netpay.get(), grosspay.get()))

        #Function for the print button in the program
        def print_values():
            pay_slip_file = self.payslip.get('1.0',"end-1c")
            filename = tempfile.mktemp('.doc')
            open(filename, 'w').write(pay_slip_file)
            os.startfile(filename, 'print')

        # Function for the reset button in the program GOOD!
        def reset():
            firstname.set("")
            surname.set("")
            address.set("")
            reference.set("")
            surname.set("")
            mobile.set("")
            base_salary.set(0)
            overtime.set(0)
            holiday_pay.set(0)
            grosspay.set("")
            netpay.set("")
            tax.set("")
            kiwisaver.set("")
            deductions.set("")
            payday.set("")
            taxPeriod.set("")
            IRDnumber.set("")
            taxablePay.set("")
            kiwisaverPay.set("")
            taxCode.set("")
            studentLoan.set("")
            ACC.set("")
            ACC_levy.set("")
            gender.set("")
            email_address.set("")
            otherPaymentsDue.set("0")
            self.payslip.delete("1.0", END)

        # Function for the exit button in the program
        def exit():
            exit = tkinter.messagebox.askyesno("Managers Workstation", "Would you like to exit?")
            if exit > 0:
                head.destroy()
                return

        # Function to return random 7 digit pay ref value and other odd jobs
        def pay_references():
            payday.set(time.strftime("%d/%m/%y"))
            pay_reference = random.randint(1000000, 99999999)
            pay_reference_fin = str(pay_reference)
            reference.set(pay_reference_fin)
            date_var = datetime.datetime.now()
            taxPeriod.set(date_var.month)
            ACC_levy.set("$1.21")

        # Function to calculate all payments
        def monthly_salary():
            pay_references()
            base_salary_calc = base_salary.get()
            over_time_calc = overtime.get()
            other_payment_due_calc = otherPaymentsDue.get()
            holiday_pay_calc = holiday_pay.get()
            sum_of_payments = base_salary_calc + over_time_calc + other_payment_due_calc + holiday_pay_calc
            tax_calc = sum_of_payments
            if tax_calc <= 14000:
                tax_calc *= 0.105
            elif tax_calc > 14000 and tax_calc <= 48000:
                first_14 = 14000 * 0.105
                tax_calc -= 14000
                tax_calc *= 0.175
                tax_calc += first_14
            elif tax_calc > 48000 and tax_calc <= 70000:
                first_48 = 48000 * 0.175
                tax_calc -= 48000
                tax_calc *= 0.3
                tax_calc += first_48
            else:
                first_48 = 48000 * 0.175
                tax_calc -= 48000
                tax_calc *= 0.33
                tax_calc += first_48
            total_tax = "$" + str('%.2f'%(tax_calc))
            tax.set(total_tax)

            kiwisaver_cal = sum_of_payments * 0.04
            total_kiwisaver = "$" + str('%.2f'%(kiwisaver_cal))
            kiwisaver.set(total_kiwisaver)

            student_loan_calc = sum_of_payments * 0.12
            total_student_loan = "$" + str('%.2f'%(student_loan_calc))
            studentLoan.set(total_student_loan)

            ACC_payments = sum_of_payments * 0.014
            total_acc_payment = "$" + str('%.2f' % (ACC_payments))
            ACC.set(total_acc_payment)

            Deduct = (tax_calc + kiwisaver_cal + student_loan_calc + ACC_payments)
            Deduct_payment = "$" + str('%.2f' % (Deduct))
            deductions.set(Deduct_payment)
            Gross_pay = "$" + str('%.2f' % sum_of_payments)
            grosspay.set(Gross_pay)

            NetPayAfter = sum_of_payments - Deduct
            NetAfter = "$" + str('%.2f' % (NetPayAfter))
            netpay.set(NetAfter)

            taxPeriod.set("31st March")
            taxablePay.set(total_tax)
            kiwisaverPay.set(total_kiwisaver)

            # Variable for printing display in second main text box. Need to simplify and debug WIP!
            employee_variable.insert(END, "" + "  " + str(reference.get()) + "                              "
                             + str(firstname.get()) + "                                  " +
                             str(surname.get()) + "                            " + str(address.get()) +
                             "                " + str(mobile.get()) + "              " + str(email_address.get())
                             + "                " + str(netpay.get()[:-3]) + "                           " +
                             str(grosspay.get()[:-3]))

        # -----------------------------------------#
        # Payslip display
        # -----------------------------------------#
            self.payslip.insert(END,'\t'+"            "+' Monthly Pay Slip' + '\n\n')
            self.payslip.insert(END, 'Reference: \t\t\t' + reference.get() +'\n')
            self.payslip.insert(END, 'Reference: \t\t\t' + payday.get() +'\n')
            self.payslip.insert(END, 'Employee Surname: \t\t\t' + surname.get() +'\n')
            self.payslip.insert(END, 'Employee Firstname: \t\t\t' + firstname.get() +'\n''\n')
            self.payslip.insert(END, 'Address: \t\t\t' + address.get() + '\n')
            self.payslip.insert(END, 'Mobile: \t\t\t' + mobile.get() + '\n')
            self.payslip.insert(END, 'Email Address: \t\t\t' + email_address.get() + '\n')
            self.payslip.insert(END, 'IRD Number: \t\t\t' + IRDnumber.get() + '\n')
            self.payslip.insert(END, 'Tax: \t\t\t' + tax.get() +'\n')
            self.payslip.insert(END, 'Tax Code: \t\t\t' + taxCode.get() + '\n')
            self.payslip.insert(END, 'KiwiSaver: \t\t\t' + kiwisaver.get() +'\n')
            self.payslip.insert(END, 'Student Loan: \t\t\t' + studentLoan.get() +'\n')
            self.payslip.insert(END, 'Holiday Pay: \t\t\t' + str("${:.2f}".format(holiday_pay.get())) +'\n')
            self.payslip.insert(END, 'Deductions: \t\t\t' + deductions.get() +'\n')
            self.payslip.insert(END, 'ACC Levy: \t\t\t' + ACC_levy.get() + '\n')
            self.payslip.insert(END, 'ACC Payment: \t\t\t' + ACC.get() +'\n')
            self.payslip.insert(END, '\nTax Paid:\t\t\t' + str("${:.2f}".format(base_salary.get())) + '\n')
            self.payslip.insert(END, 'Overtime:\t\t\t' + str("${:.2f}".format(overtime.get())) + '\n')
            self.payslip.insert(END, 'Net Pay:\t\t\t' + str(netpay.get()) + '\n')
            self.payslip.insert(END, 'Gross Pay: \t\t\t' + str(grosspay.get()) + '\n')
            input_data()

        # -----------------------------------------#
        # GUI
        # -----------------------------------------#
        #Payslip widget in rightFrame1a
        self.payslip = Text(rightFrame1a, height=24, width=40, bd=10, font=("Arial",9,"bold"))
        self.payslip.grid(row=0, column=0)

        #Heading in topFrame2
        self.label = Label(topFrame2, font=("Arial",10,"bold"), bg='white', padx=6, pady=2,text="Reference\t"+"             "+\
        "\tFirstname\t"+"     "+"\tSurname\t\t"+"    "+"Address\t"+"             "+"\t\tMobile\t\t"
        + "        " + "\tEmail\t \t"+"      "+"\tNet Pay\t\t" + "            "+ "\tGross Pay")
        self.label.grid(row=0, column=0, columnspan=17)

        #Scrollbar
        scrollbar = Scrollbar(topFrame2)
        scrollbar.grid(row=1, column=1, sticky="ns")

        #Listbox employee widget
        employee_variable = Listbox(topFrame2, width=145, height=5, font=("Arial", 12, "bold"), bg='white', yscrollcommand=scrollbar.set)
        employee_variable.bind("<<ListboxSelect>>")
        employee_variable.grid(row=1, column=0, padx=1, sticky="nsew")
        scrollbar.config(command = employee_variable.xview)

        # -------------------------#
        #Leftframe1
        # -------------------------#
        #Reference widget
        self.reference = Label(leftFrame1, font=("Arial", 12, "bold"), text="Reference", bd=7, anchor="w", bg="pale goldenrod")
        self.reference.grid(row=0, column=0,sticky="w", padx=5)
        #Reference textbox
        self.reference_txt = Entry(leftFrame1, font=("Arial", 12, "bold"), bd=5, width=60, justify="left",
                                   textvariable=reference)
        self.reference_txt.grid(row=0, column=1)

        #Firstname widget
        self.firstname = Label(leftFrame1, font=("Arial", 12, "bold"), text="Firstname", bd=7, anchor="w", bg="pale goldenrod")
        self.firstname.grid(row=1, column=0, sticky="w", padx=5)
        #Firstname textbox
        self.firstname_txt = Entry(leftFrame1, font=("Arial", 12, "bold"), bd=5, width=60, justify="left",
                                   textvariable=firstname)
        self.firstname_txt.grid(row=1, column=1)

        #Surname widget
        self.surname = Label(leftFrame1, font=("Arial", 12, "bold"), text="Surname", bd=7, justify="left", bg="pale goldenrod")
        self.surname.grid(row=2, column=0, sticky="w", padx=5)
        #Surname textbox
        self.surname_txt = Entry(leftFrame1, font=("Arial", 12, "bold"), bd=5, width=60, justify="left",
                                   textvariable=surname)
        self.surname_txt.grid(row=2, column=1)

        #address widget
        self.address = Label(leftFrame1, font=("Arial", 12, "bold"), text="Address", bd=7, bg="pale goldenrod")
        self.address.grid(row=3, column=0, sticky="w", padx=5)
        #address textbox
        self.address_txt = Entry(leftFrame1, font=("Arial", 12, "bold"), bd=5, width=60, justify="left",
                                 textvariable=address)
        self.address_txt.grid(row=3, column=1)

        #Mobile widget
        self.mobile = Label(leftFrame1, font=("Arial", 12, "bold"), text="Mobile", bd=7, bg="pale goldenrod")
        self.mobile.grid(row=4, column=0, sticky="w", padx=5)
        #Mobile textbox
        self.mobile_txt = Entry(leftFrame1, font=("Arial", 12, "bold"), bd=5, width=60,
                                 textvariable=mobile)
        self.mobile_txt.grid(row=4, column=1)

        # Gender widget
        self.gender = Label(leftFrame1, font=("Arial", 12, "bold"), text="Email", bd=7, bg="pale goldenrod")
        self.gender.grid(row=5, column=0, sticky="w", padx=5)
        # Gender textbox
        self.gender_txt = Entry(leftFrame1, font=("Arial", 12, "bold"), bd=5, width=60,
                                textvariable=email_address)
        self.gender_txt.grid(row=5, column=1)

        # -------------------------#
        #Leftframe2 - Left Portion
        # -------------------------#
        #Basic Salary widget
        self.basic_salary = Label(leftFrame2Left, font=("Arial", 12, "bold"), text="Basic Salary", bd=7, anchor="e",
                                  bg="pale goldenrod")
        self.basic_salary.grid(row=0, column=0, sticky="w")
        #Basic Salary textbox
        self.basic_salary_txt = Entry(leftFrame2Left, font=("Arial", 12, "bold"), bd=5, width=20, justify="left",
                                      textvariable=base_salary)
        self.basic_salary_txt.grid(row=0, column=1)

        #Overtime widget
        self.overtime = Label(leftFrame2Left, font=("Arial", 12, "bold"), text="Overtime", bd=7, anchor="e", justify="left",
                                  bg="pale goldenrod")
        self.overtime.grid(row=1, column=0, sticky="w")
        #Overtime textbox
        self.overtime_txt = Entry(leftFrame2Left, font=("Arial", 12, "bold"), bd=5, width=20, justify="left",
                                      textvariable=overtime)
        self.overtime_txt.grid(row=1, column=1)

        #Holiday pay widget
        self.holiday_pay = Label(leftFrame2Left, font=("Arial", 12, "bold"), text="Holiday Pay", bd=7, anchor="e",
                              justify="left", bg="pale goldenrod")
        self.holiday_pay.grid(row=2, column=0, sticky="w")
        #Holiday pay textbox
        self.holiday_pay_txt = Entry(leftFrame2Left, font=("Arial", 12, "bold"), bd=5, width=20, justify="left",
                                  textvariable=holiday_pay)
        self.holiday_pay_txt.grid(row=2, column=1)

        #Other payments widget
        self.Other = Label(leftFrame2Left, font=("Arial", 12, "bold"), text="Other Payment", bd=7, anchor="w",
                              justify="left", bg="pale goldenrod")
        self.Other.grid(row=3, column=0, sticky="w")
        #Other payments textbox
        self.Other_txt = Entry(leftFrame2Left, font=("Arial", 12, "bold"), bd=5, width=20, justify="left",
                                  textvariable=otherPaymentsDue)
        self.Other_txt.grid(row=3, column=1)

        # -------------------------#
        # Leftframe2 - Right Portion
        # -------------------------#
        #Tax widget
        self.tax = Label(leftFrame2Right, font=("Arial", 12, "bold"), text="Tax", bd=7, anchor="e",
                                  bg="pale goldenrod")
        self.tax.grid(row=0, column=0, sticky="w")
        #Tax textbox
        self.tax_txt = Entry(leftFrame2Right, font=("Arial", 12, "bold"), bd=5, width=20, justify="left",
                                      textvariable=tax)
        self.tax_txt.grid(row=0, column=1)

        #Kiwisaver widget
        self.kiwisaver = Label(leftFrame2Right, font=("Arial", 12, "bold"), text="KiwiSaver", bd=7, anchor="e",
                         bg="pale goldenrod")
        self.kiwisaver.grid(row=1, column=0, sticky="w")
        #Kiwisaver textbox
        self.kiwisaver_txt = Entry(leftFrame2Right, font=("Arial", 12, "bold"), bd=5, width=20, justify="left",
                             textvariable=kiwisaver)
        self.kiwisaver_txt.grid(row=1, column=1)

        #Student Loan widget
        self.std = Label(leftFrame2Right, font=("Arial", 12, "bold"), text="Student Loan", bd=7, anchor="e",
                               bg="pale goldenrod")
        self.std.grid(row=2, column=0, sticky="w")
        #Student Loan textbox
        self.std_txt = Entry(leftFrame2Right, font=("Arial", 12, "bold"), bd=5, width=20, justify="left",
                                   textvariable=studentLoan)
        self.std_txt.grid(row=2, column=1)

        #ACC widget
        self.ACC = Label(leftFrame2Right, font=("Arial", 12, "bold"), text="ACC Payment", bd=7, anchor="e",
                         bg="pale goldenrod")
        self.ACC.grid(row=3, column=0, sticky="w")
        #ACC textbox
        self.ACC_txt = Entry(leftFrame2Right, font=("Arial", 12, "bold"), bd=5, width=20, justify="left",
                         textvariable=ACC)
        self.ACC_txt.grid(row=3, column=1)

        # -------------------------#
        #Rightframe2a - Payday
        # -------------------------#
        #Payday widget
        self.pay_day = Label(rightFrame2a, font=("Arial", 12, "bold"), text="Payday", bd=11, anchor="e",
                         bg="pale goldenrod")
        self.pay_day.grid(row=0, column=0, sticky="w")
        #Payday textbox
        self.pay_day_txt = Entry(rightFrame2a, font=("Arial", 12, "bold"), bd=5, width=20, justify="left",
                         textvariable=payday)
        self.pay_day_txt.grid(row=0, column=1)

        # -------------------------#
        #Rightframe2b
        # -------------------------#
        #Tax Period widget
        self.tax_period = Label(rightFrame2b, font=("Arial", 12, "bold"), text="Tax Period", bd=7, anchor="w",
                             justify="left", bg="pale goldenrod")
        self.tax_period.grid(row=0, column=0, sticky="w")
        #Tax Period textbox
        self.tax_period_txt = Entry(rightFrame2b, font=("Arial", 12, "bold"), bd=5, width=17, justify="left",
                             textvariable=taxPeriod)
        self.tax_period_txt.grid(row=0, column=1)

        #Tax Code widget
        self.tax_Code = Label(rightFrame2b, font=("Arial", 12, "bold"), text="Tax Code", bd=7, anchor="w",
                                justify="left", bg="pale goldenrod")
        self.tax_Code.grid(row=1, column=0, sticky="w")
        #Tax Code textbox
        self.tax_Code_txt = Entry(rightFrame2b, font=("Arial", 12, "bold"), bd=5, width=17, justify="left",
                                textvariable=taxCode)
        self.tax_Code_txt.insert(0, 'Please Enter Code')
        self.tax_Code_txt.grid(row=1, column=1)

        #IRD Number widget
        self.ird = Label(rightFrame2b, font=("Arial", 12, "bold"), text="IRD Number", bd=7, anchor="w",
                                justify="left", bg="pale goldenrod")
        self.ird.grid(row=2, column=0, sticky="w")
        #IRD Number textbox
        self.ird_txt = Entry(rightFrame2b, font=("Arial", 12, 'bold'), bd=5, width=17, justify="left",
                                textvariable=IRDnumber)
        self.ird_txt.insert(0, 'Please Enter IRD')
        self.ird_txt.grid(row=2, column=1)

        #ACC Levy widget
        self.ACC_levy = Label(rightFrame2b, font=("Arial", 12, "bold"), text="ACC Levy", bd=7, anchor="w",
                         justify="left", bg="pale goldenrod")
        self.ACC_levy.grid(row=3, column=0, sticky="w")
        #ACC Levy textbox
        self.ACC_levy_txt = Entry(rightFrame2b, font=("Arial", 12, "bold"), bd=5, width=17, justify="left",
                         textvariable=ACC_levy)
        self.ACC_levy_txt.grid(row=3, column=1)

        # -------------------------#
        #Rightframe2c
        # -------------------------#
        #Taxable pay widget
        self.taxable_pay = Label(rightFrame2c, font=("Arial", 12, "bold"), text="Taxable Pay", bd=0, anchor="w",
                                justify="left", bg="pale goldenrod")
        self.taxable_pay.grid(row=0, column=0, sticky="w")
        #Taxable pay textbox
        self.taxable_pay_txt = Entry(rightFrame2c, font=("Arial", 12, "bold"), bd=5, width=17, justify="left",
                                    textvariable=taxablePay)
        self.taxable_pay_txt.grid(row=0, column=1)

        #Kiwisaver pay widget
        self.kiwisaver_pay = Label(rightFrame2c, font=("Arial", 12, "bold"), text="KiwiSaver Pay", bd=0, anchor="w",
                                 justify="left", bg="pale goldenrod")
        self.kiwisaver_pay.grid(row=1, column=0, sticky="w")
        #Kiwisaver pay textbox
        self.kiwisaver_pay_txt = Entry(rightFrame2c, font=("Arial", 12, "bold"), bd=5, width=17, justify="left",
                                     textvariable=kiwisaverPay)
        self.kiwisaver_pay_txt.grid(row=1, column=1)

        # -------------------------#
        #Rightframe2d
        # -------------------------#
        #Net pay widget
        self.net_pay = Label(rightFrame2d, font=("Arial", 12, "bold"), text="Net Pay", bd=7, anchor="w",
                                justify="left", bg="pale goldenrod")
        self.net_pay.grid(row=0, column=0, sticky="w")
        #Net pay textbox
        self.net_pay_txt = Entry(rightFrame2d, font=("Arial", 12, "bold"), bd=5, width=18, justify="left",
                                    textvariable=netpay)
        self.net_pay_txt.grid(row=0, column=1)

        #Gross pay widget
        self.gross = Label(rightFrame2d, font=("Arial", 12, "bold"), text="Gross Pay", bd=7, anchor="w",
                                justify="left", bg="pale goldenrod")
        self.gross.grid(row=1, column=0, sticky="w")
        #Gross pay textbox
        self.gross_txt = Entry(rightFrame2d, font=("Arial", 12, "bold"), bd=5, width=18, justify="left",
                                    textvariable=grosspay)
        self.gross_txt.grid(row=1, column=1)

        #Deductions widget
        self.Deductions = Label(rightFrame2d, font=("Arial", 12, "bold"), text="Deductions", bd=7, anchor="w",
                                justify="left", bg="pale goldenrod")
        self.Deductions.grid(row=2, column=0, sticky="w")
        #Deductions textbox
        self.Deductions_txt = Entry(rightFrame2d, font=("Arial", 12, "bold"), bd=5, width=18, justify="left",
                                    textvariable=deductions)
        self.Deductions_txt.grid(row=2, column=1)

        # ==========================================Buttons======================================================
        #Add new button
        self.addNewTotal = Button(topFrame1, pady=1, padx=24,  bd=4, bg='white', font=("arial", 16, "bold"),
                                  width=8, text="Add", command=monthly_salary).grid(row=0, column=0, padx=1)

        #Print button
        self.print_button = Button(topFrame1, pady=1, padx=24, bd=4, bg='white', font=("arial", 16, "bold"),
                                  width=8, text="Print", command=print_values).grid(row=0, column=1, padx=1)

        #Display button
        self.display_button = Button(topFrame1, pady=1, padx=24, bd=4, bg='white', font=("arial", 16, "bold"),
                                  width=8, text="Display", command=display_data).grid(row=0, column=2, padx=1)

        #Update button
        self.update_button = Button(topFrame1, pady=1, padx=24, bd=4, bg='white', font=("arial", 16, "bold"),
                                  width=8, text="Update", command=update).grid(row=0, column=3, padx=1)
        #Delete button
        self.del_button = Button(topFrame1, pady=1, padx=24, bd=4, bg='white', font=("arial", 16, "bold"),
                                  width=8, text="Delete", command=del_data).grid(row=0, column=4, padx=1)

        #Search button
        self.search_button = Button(topFrame1, pady=1, padx=24, bd=4, bg='white', font=("arial", 16, "bold"),
                                  width=8, text="Search", command=search_data).grid(row=0, column=5, padx=1)

        #Reset button
        self.reset_button = Button(topFrame1, pady=1, padx=24, bd=4, bg='white', font=("arial", 16, "bold"),
                                  width=8, text="Reset",command=reset).grid(row=0, column=6, padx=1)

        #Exit button
        self.exit_button = Button(topFrame1, pady=1, padx=24, bd=4, bg='white', font=("arial", 16, "bold"),
                                  width=8, text="Exit", command=exit).grid(row=0, column=7, padx=1)

if __name__ == '__main__':
    head = Tk()
    application = Manager(head)
    head.mainloop()

