# procurement_main_gui.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox

# #################################################
# Import any of your classes defined in other files
# #################################################

# Import all the GUI classes implementing each menu option
# e.g. EmployeeGUI, ProductGUI, SupplierGUI, PurchaseOrderGUI
# Each GUI class will import the corresponding data access class 
# to communicate with the database
# The GUI classes also import a single Validation class containing 
# all necessary validation methods

# From file xxx.py import class Xxxx
from customer_gui import CustomerGUI
from movie_gui import MovieGUI
#from product_gui import ProductGUI
#from supplier_gui import SupplierGUI # ==> Not implemented
#from purchase_order_gui import PurchaseOrderGUI

# Reports GUI
#from product_report_gui import ProductReportGUI
#from category_report_gui import CategoryReportGUI


# ################
# Global Constants 
# ################


# ####################
# ProcurementGui Class
# ####################

class ProcurementGUI():

    def __init__(self):   

        print("Creating Procurement GUI ...")

        self.current_gui = None # Reference to current GUI 

        # Step 1. Create main window of the application
        # 900x500 pixels in the middle of the screen
        # Can minimise to 0x0 pixels
        self.root = tk.Tk()
        self.root.title("Procurement System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinates (width, height, x, y) :", 
              width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        # Step 2. Add a menu

        # Create a toplevel menu
        menubar = tk.Menu(self.root)

        # File menu (pulldown)
        # Create a pulldown menu
        filemenu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        filemenu.add_command(label="Open", command="")
        filemenu.add_command(label="Save", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="File", menu=filemenu)
       
        # Employee menu (pulldown)
        # Create a pulldown menu
        customer_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        # do not use self.create_employee_gui()
        customer_menu.add_command(label="Customer", 
            command=self.create_customer_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Customer", menu=customer_menu)
      
        # Product menu (pulldown)
        # Create a pulldown menu
        movie_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        movie_menu.add_command(label="Movie", 
            command=self.create_movie_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Movie", menu=movie_menu)

        '''
        # Supplier menu (pulldown) ==> Not implemented
        # Create a pulldown menu
        supplier_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        supplier_menu.add_command(label="Supplier", 
            command=self.create_supplier_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Supplier", menu=supplier_menu)
        '''
        
        # Purchase order menu (pulldown)
        #purchase_order_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        #purchase_order_menu.add_command(label="Purchase-Order", 
        #    command=self.create_purchase_order_gui) 
        # Add pulldown menu to toplevel menu
        #menubar.add_cascade(label="Purchase-Order", menu=purchase_order_menu)

        # Reports menu (pulldown)
        #reports_menu = tk.Menu(menubar, tearoff=0)
        #reports_menu.add_command(label="Product Report", 
         #                        command=self.create_product_report_gui)
        #reports_menu.add_command(label="Product Category Report", 
         #                        command=self.create_category_report_gui)
        #menubar.add_cascade(label="Reports", menu=reports_menu)

        # Display the menu
        self.root.config(menu=menubar)

        pass
            
    # Functions to create child frames 
    # when menu options are selected

    def create_customer_gui(self):
        if self.current_gui:
            self.current_gui.destroy()

        customer_gui = CustomerGUI()
        self.current_gui = customer_gui.create_gui(self.root)
        pass
        

    def create_movie_gui(self):
        if self.current_gui:
            self.current_gui.destroy()
        
        movie_gui = MovieGUI()
        self.current_gui = movie_gui.create_gui(self.root)
        pass


# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """

    # Instantiate the main application gui 
    # it will create all the necessary GUIs
    gui = ProcurementGUI()

    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()
    pass        