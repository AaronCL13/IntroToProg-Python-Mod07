# ----------------------------------------------------------------------------#
# Title: Assignment 7
# Desc: Project Budget Tracker - Tracks items for your project and their cost
# Changed Log: (Who, When, What)
# ALanphear, 2.27.21, Created script
# ----------------------------------------------------------------------------#

import pickle
pickle_file = "Project_Pickle_Data.dat"
items_lst = []
unpickled_data = []
item_new = ""
choice = ""
cost_new = 0.0
quantity_new = 0


# Processing
class Processing:
    """Processes data"""

    @staticmethod
    def add_data_to_list(item, cost, quantity, list_table):
        """ Adds data provided by user as dictionary row into a list

        :param item: (string) item to add to list
        :param cost: (float) cost of the item
        :param quantity: (int) quantity of the items
        :param list_table: (list) you want filled with data
        :return: (list) of dictionary rows

        """
        row = {"Item": item, "Item Cost": cost, "Quantity": quantity, "Total Cost": float("%.2f" % (cost * quantity))}
        list_table.append(row)
        return list_table

    @staticmethod
    def get_project_cost(list_table):
        """ Sums up total cost from all rows in the list

        :param list_table: (list) you want perform sum on
        :return: (float) cost sum

        """
        cost = 0.0
        for row in list_table:
            cost += row["Total Cost"]
        return cost

    @staticmethod
    def present_list_data(data):
        """ Present list data and nicer format

        :param data: (list) the data you want to present
        :return: list in presentable format

        """
        table = ""
        for row in data:
            row_dic = row["Item"] + " | " + str(row["Item Cost"]) + " | " + str(row["Quantity"]) \
                      + " | " + str("%.2f" % row["Total Cost"]) + "\n"
            table += row_dic
        return table

    @staticmethod
    def pickle_list(file, list_table):
        """ Writes data to a pickle file

        :param file: (string) with name of file
        :param list_table: (list) data that you want written to file

        """
        with open(file, "wb") as p:  # Does not need to call close()
            pickle.dump(list_table, p)

    @staticmethod
    def unpickle_file(file):
        """ Read data from a pickle file

        :param file: (string) with name of file
        :return: (list) data from file

        """
        with open(file, "rb") as p:  # Does not need to call close()
            data = pickle.load(p)
            return data


# IO
class IO:
    """ Performs input/output functions"""

    @staticmethod
    def get_user_input():
        """ Gets user input data

        :return: string, float, int

        """
        item = input("What item do you need to add?: ")
        cost = float(input("How much does it cost?: "))  # ValueError Exception
        quantity = int(input("How many do you need?: "))  # ValueError Exception
        return item, cost, quantity

    @staticmethod
    def show_total_project_cost(cost):
        """ Prints total project cost

        :param cost: (float)
        :return: nothing

        """
        print("Your total project cost is now $%.2f " % cost)


# Main Program

while True:  # Ask the user if they want to continue
    choice = input("Press [Enter] to Continue or Type 'exit' to end the program.\n")
    if choice.lower() == "exit":
        break
    else:
        try:
            unpickled_data = Processing.unpickle_file(pickle_file)  # Get the data from the file
            items_lst = unpickled_data  # Add it to the list
        except FileNotFoundError as e:  # Display this error if the file has not been created yet
            print(e)
            print("File could not be located! Are you sure you saved one?")
            print("Enter data so that a file can be saved!\n")
        except Exception as e:  # Display for non-specific error
            print("There was a general error!")
            print("Python Details Below: ")
            print(e, e.__doc__, type(e), sep='\n')
        else:  # Run this code if no errors
            print("Your current pickled data is:\n")
            print("Item", "|", "Item Cost", "|", "Quantity", "|", "Total Cost")
            present_items = Processing.present_list_data(unpickled_data)  # Make data presentable
            print(present_items)  # Print the presentable data

        try:
            item_new, cost_new, quantity_new = IO.get_user_input()  # Get user input
        except ValueError as e:  # Display this error if string inputted for quantity or cost
            print("\nPython", e)  # and/or if float entered for quantity
            print("Cost and Quantity must both be numbers!\n"
                  "Quantity must be a whole number!\n")
        except Exception as e:  # Display for non-specific error
            print("There was a general error!")
            print("Python Details Below: ")
            print(e, e.__doc__, type(e), sep='\n')
        else:  # Run this code if no errors
            Processing.add_data_to_list(item_new, cost_new, quantity_new, items_lst)  # Add data to list
            project_cost = Processing.get_project_cost(items_lst)  # Get project cost from list data
            IO.show_total_project_cost(project_cost)  # Print total project cost
            Processing.pickle_list(pickle_file, items_lst)  # Pickle the new list data
            print("\nYour Data has been Pickled!")