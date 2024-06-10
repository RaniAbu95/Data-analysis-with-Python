# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# login: abura
# id: 316396787
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Program: SQL to CSV Converter
# Description:
# This program reads a SQL file, analyzes its contents, and converts each SQL table into a corresponding CSV file. It
# handles errors and exceptions gracefully and provides meaningful error messages.
#
"""Error Handling:
- FileNotFoundError: Raised if the specified SQL file is not found.
- IOError: Raised if an error occurs while reading the SQL file.
- Exception: Raised if an error occurs during the conversion process or CSV file handling.

Example Usage:
1. Replace `old_file_name` with the path to your SQL file.
2. Run the program.

Note:
- Ensure the necessary permissions are granted to read the SQL file and write the CSV files in the specified directory.
"""
import io

"""
      add_values(str1, file1):
    - Description: Writes the values to the fields in the CSV file.
    - Parameters:
        - str1: String containing the INSERT INTO statement for a table.
        - file1: File object representing the CSV file.
    - Returns: None
    """


def add_values(str1, file1):

    file1.write("\n")
    start = 0
    end = 0
    start_adding_values = 0
    index = 0
    while index < len(str1):
        if str1[index] == "(":
            start = index
            index += 1
        elif str1[index] == ")":
            end = index
            start_adding_values = 1
            index += 1
        else:
            index += 1
        if start_adding_values == 1:
            newlst = str1[start:end + 1][1:-1]
            start_adding_values = 0
            file1.write(newlst.replace("'", ""))
            file1.write("\n")

"""
    - Description: Creates a CSV file and adds the desired headline for each field. Calls add_values to fill and add the values for each field.
    - Parameters:
        - str: String containing the CREATE TABLE statement for a table.
        - file1: File object representing the CSV file.
    - Returns: None
    """


def add_headlines(str, file1):

    start = 0
    print_start = 0
    newstr = []
    str = str.splitlines()
    for i in str:
        newstr.append(i.strip())

    for i in newstr:
        if i.startswith("`"):
            if start == 0:
                start = 1
                g1 = i.split("`")
                file_name3 = g1[1] + ".csv"
                file1 = open(file_name3, "w")
            else:
                g1 = i.split("`")
                if print_start == 1:
                    file1.write(",")
                    file1.write(g1[1])
                else:
                    file1.write(g1[1])
                    print_start = 1
        elif i.startswith("INSERT INTO"):
            add_values(i, file1)

"""
    - Description: Reads the SQL file, splits the text into blocks by CREATE TABLE, and yields CSV file objects for each table.
    - Parameters:
        - old_file_name: String representing the path to the SQL file.
    - Returns: Generator object that yields CSV file objects
    """


def convert_sql_to_csv(old_file_name):

    try:
        with open(old_file_name, 'r') as old_file:
            old_file_content = old_file.read()
            newtxt = old_file_content.split("CREATE TABLE")
            for index in newtxt:
                if "INSERT INTO" in index:
                    csv_file = io.StringIO()
                    add_headlines(index, csv_file)
                    csv_file.seek(0)
                    yield csv_file
    except FileNotFoundError as e:
        raise FileNotFoundError("File not found: " + old_file_name) from e
    except IOError as e:
        raise IOError("Error occurred while reading the file: " + old_file_name) from e
    except Exception as e:
        raise Exception("An error occurred while converting SQL to CSV: " + str(e))

"""
    1. Specify the path to the SQL file in the variable `old_file_name`.
    2. Call `convert_sql_to_csv` function with `old_file_name` as a parameter to obtain the generator object.
    3. Iterate over the generator object to get each CSV file object.
    4. Process or save each CSV file as desired.
    5. Handle exceptions and errors raised during the conversion process and provide meaningful error messages.
    """


def main():
    old_file_name = "/Users/raniaburaia/PycharmProjects/pythonProject/2023/ex7/demo.sql"  # Path to the SQL file
    try:
        csv_generator = convert_sql_to_csv(old_file_name)
        while True:
            try:
                csv_file = next(csv_generator)
                table_name = csv_file.readline().strip().split(",")
                print("CSV file generated:", table_name[0] + ".csv")
                # Process or save the CSV file
                csv_file.close()
            except StopIteration:
                print("All tables generated.")
                break
            except Exception as e:
                raise Exception("An error occurred while processing CSV file: " + str(e))
    except FileNotFoundError as e:
        raise FileNotFoundError("File not found:", str(e))
    except IOError as e:
        raise IOError
