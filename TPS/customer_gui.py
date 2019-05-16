# employee_gui.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox

from database import getSession
from customer_dao import CustomerDAO# To communicate with Employee table
from customer_validation import Validation # To validate the entries made on the form

# #################
# CustomerGUI Class
# #################
getSession = getSession()
class CustomerGUI():

    def __init__(self):   
      
        self.customer_dao = CustomerDAO()

        self.validator = Validation()

        self.customer_id = tk.StringVar()
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()
        self.email = tk.StringVar()
        self.phone_no = tk.StringVar()
        self.dob = tk.StringVar()


        self.lb_ids = None

        self.mb_title_bar = "Customer CRUD"

        pass 

    def create_gui(self, root):
     
        print("Creating customer GUI ...")


        customer_frame = tk.Frame(root)
        customer_frame.pack()

        form_frame = tk.Frame(customer_frame)
        form_frame.pack()
    
        tk.Label(form_frame, font=('arial', 10), 
                 text = "Customer").grid(row=0, column=0, columnspan=3)

        # row 1: firstname label, firstname entry and listbox of ids
        tk.Label(form_frame, text= "Customer ID", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=1, column=0)
        tk.Entry(form_frame, textvariable=self.customer_id, width=30, bd=1, 
                 state=tk.DISABLED).grid(row=1, column=1)

        # row 2: firstname label, firstname entry and listbox of ids
        tk.Label(form_frame, text= "Firstname", font=('arial', 10), 
                 width=20, anchor="e", bd=1, pady=10, padx=10).grid(row=2, column=0)
        tk.Entry(form_frame, textvariable=self.firstname, 
                 width=30, bd=1).grid(row=2, column=1)
        
        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=2, column=4, rowspan=5) 

        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)
        # row 3: lastname label and entry (the listbox will go through)
        tk.Label(form_frame, text= "Lastname", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=3, column=0)
        tk.Entry(form_frame, textvariable=self.lastname, 
                 width=30, bd=1).grid(row=3, column=1)

        # row 4: title label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Email", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=4, column=0)
        tk.Entry(form_frame, textvariable=self.email, 
                 width=30, bd=1).grid(row=4, column=1)


        # row 5: email label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Phone number", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=5, column=0)
        tk.Entry(form_frame, textvariable=self.phone_no, 
                 width=30, bd=1).grid(row=5, column=1)
        
        
        # row 6: work_phone label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Date of birth", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=6, column=0)
        tk.Entry(form_frame, textvariable=self.dob, 
                 width=30, bd=1).grid(row=6, column=1)

        button_frame = tk.Frame(customer_frame, pady=10) 
        button_frame.pack()
   
        tk.Button(button_frame, width=10, text="Clear", 
                  command=self.clear_fields).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Save", 
                  command=self.save).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Delete", 
                  command=self.delete).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Load", 
                  command=self.load).pack(side=tk.LEFT)       

        return customer_frame

    def clear_fields(self):

        # Just blank all the fields
        self.customer_id.set("")
        self.firstname.set("")
        self.lastname.set("")
        self.email.set("")
        self.phone_no.set("")
        self.dob.set("")
        pass

    def save(self):
       
        print("Saving a customer ...")

        # Get the data
        data = self.get_fields()   

        # Validate the data
        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['customer_id'])==0):
                # If nothing has been entered in employee_id 
                # i.e. its length is zero characters
                print("Calling create() as customer_id is absent")
                self.create(data)
            else:
                print("Calling update() as customer_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message 
            messagebox.showwarning(self.mb_title_bar, message_text, icon="warning")
            pass

    def get_fields(self):


        customer = {}
        # employee_id is ignored when creating a record
        customer['customer_id'] = self.customer_id.get() 
        customer['firstname'] = self.firstname.get()
        customer['lastname'] = self.lastname.get()
        customer['phone_no'] = self.phone_no.get()
        customer['email'] = self.email.get()
        customer['dob'] = self.dob.get()
        return customer  

    def validate_fields(self, data):
      
           
        # By default set to true, anything wrong will turn it to false   
        valid_data = True 
        # Instantiate an empty list to contain the messages
        message_list = [] 
        # Check for blank fields
        # Do not check employee_id as this is generated by the database
        #if len(data['employee_id']==0:
        #    valid_data = False
        #    message_list.append("employee_id is empty")
        if len(data['firstname'])==0:
            valid_data = False
            message_list.append("firstname is empty")
        if len(data['lastname'])==0:
            valid_data = False
            message_list.append("lastname is empty")
        if len(data['phone_no'])==0:
            valid_data = False
            message_list.append("phone number is empty")
        if len(data['email'])==0:
            valid_data = False
            message_list.append("email is empty")
        if len(data['dob'])==0:
            valid_data = False
            message_list.append("date of birth is empty")

        # Other possible checks

        # Implement these as functions in the Validation class so that 
        # other classes can call them
         
        # Check if firstname and lastname contain  
        # only alphabetic characters (and may be certain special characters)
        if not self.validator.is_alphabetic(data['firstname']):
            valid_data = False
            message_list.append("invalid firstname")

        if not self.validator.is_alphabetic(data['lastname']):
            valid_data = False
            message_list.append("invalid lastname")
    
        # Check if title is in a list [Mr, Ms, Mrs, Dr, etc]
        # Alternatively could use a dropbox/combobox to do this
        # However, if the combobox is not set to a default value 
        # (to force the user to select something)
        # A blank value can get through

        # Check if email follows a certain pattern 
        # i.e contains an @ followed by a dot
        if not self.validator.is_email(data['email']):
            valid_data = False
            message_list.append("invalid email format")

        if not self.validator.is_dob(data['dob']):
            valid_data = False
            message_list.append("invalid date of birth format eg. dd/mm/YYYY")

        # Check if work_phone follows a certain pattern 
        # i.e. (02) 99999999 or (02) 9999 9999 or +61 3 9999 9999 (international)
        if not self.validator.is_phone_number(data['phone_no']):
            valid_data = False
            message_list.append("invalid phone number format eg. 0400 000 000")
        
            
        # Join the items in the list as a string separated with a comma and a space    
        message = ', '.join(message_list) 

        return valid_data, message # return 2 values

    def create(self, data):
       

        print("Creating an customer ...")
        print(data)

        session = getSession.get_db_session() # Get a session (database.py)
        result = self.customer_dao.create(session, data) 
    
        session.close() # Close the session

        messagebox.showinfo(self.mb_title_bar, result)
 
        pass

    def update(self, data):

        print("Updating an customer ...")
        print(data)

        session = getSession.get_db_session() # Get a session (database.py)
        result = self.customer_dao.update(session, data['customer_id'], data)
        session.close() # close the session

        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def delete(self):
        
        print("Deleting a customer ...")
        customer_id = self.customer_id.get() 
        print(id)
        
        # Call the data access object to do the job
        # Pass the id as parameter to the delete() method
        session = getSession.get_db_session() # Get a session (database.py)
        result = self.customer_dao.delete(session, customer_id)
        session.close() # Close the session

        # Display the returned message to the user - use a messagebox    
        # Display everything that is returned in the result    
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def load(self):
       
        session = getSession.get_db_session() # Get a session (database.py)
        result = self.customer_dao.find_ids(session) # {"employee_ids": [1, 2, 3]}
        session.close() # Close the session
        print("result", result)
        # Check if there is an entry in the result dictionary
        
        if "customer_ids" in result: 
            list_ids = result['customer_ids'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_ids.delete(0,tk.END)
            print("Setting customer_id in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                #print(x)
            pass

    def on_list_select(self, evt):
       
        # For more information on 'tkinter events', 
        # refer to http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        w = evt.widget
        index = int(w.curselection()[0]) 
          # index = position of the item clicked in the list, first item is item 0 not 1
        value = w.get(index) 
          # value of the item clicked, in our case it's the employee_id
        print(index) 
        print(value)

        # Call find_by_id and populate the stringvars of the form
        session = getSession.get_db_session() # Get a session (database.py)
        result = self.customer_dao.find_by_id(session, value)   
        session.close() # close the session
        print("result", result) 
           # { "employee" : {"employee_id": "", "firstname": "", etc}}
        customer = result['customer']
        self.populate_fields(customer)
        pass

    def populate_fields(self, customer):
       

        # Set the values from the dict to the stringvars
        self.customer_id.set(customer['customer_id'])
        self.firstname.set(customer['firstname'])
        self.lastname.set(customer['lastname'])
        self.phone_no.set(customer['phone_no'])
        self.email.set(customer['email'])
        self.dob.set(customer['dob'])
        pass

# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """
     
    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("Procurement System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = CustomerGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass