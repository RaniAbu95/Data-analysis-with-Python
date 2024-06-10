# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# login: abura
# id: 316396787
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Program: Regex usage
# Description:
# Q1:Process the file containing city names and extract the corresponding zip codes.
#
#         The function reads the file '2022_largest_cities.txt' that contains city names and states.
#         It then matches each city with its corresponding state and extracts the zip code from the file 'us_postal_codes.csv'.
# Q2:Extracts completed runs from the input file and writes them to the output file.
#
#        The function reads the contents of the input file ("atoms2.log") and searches for
#        matches of a specific regex pattern representing completed runs. It then writes
#        the matched run numbers and corresponding filenames to the output file
#        ("completed_runs.txt").
import re

def q1_func():
    """
        Process the file containing city names and extract the corresponding zip codes.

        The function reads the file '2022_largest_cities.txt' that contains city names and states.
        It then matches each city with its corresponding state and extracts the zip code from the file 'us_postal_codes.csv'.

        Args:
            - None

        Returns:
            None

        Raises:
            None
        """
    # Open the file containing city names
    with open('2022_largest_cities.txt', "r") as names_file:
        # Read and discard the first line
        names_file.readline()

        # Process the remaining lines
        for line in names_file:
            remaining_lines = names_file.readlines()

        # Iterate over each record in the remaining lines
        for record1 in remaining_lines:
            # Define the pattern to match the city name and state
            pattern1 = r'\t([A-Za-z\s]+)\t'
            match = re.search(pattern1, record1)
            if match:
                # Get the matched city name and state
                city_and_state = match.group(1)

                # Split the city and state using tab delimiter
                city = city_and_state.split('\t')[0]
                state = city_and_state.split('\t')[1]

                # Open the file containing zip codes
                with open('us_postal_codes.csv', 'r') as zip_file:
                    # Read and discard the first line
                    zip_file.readline()

                    for line in zip_file:
                        rest = zip_file.readlines()

                    # Process the remaining lines
                    for record2 in rest:
                        # Search for the state in the record
                        if re.search(state, record2):
                            # Define the pattern to match the zip code
                            pattern3 = r'[0-9]{5}'
                            match = re.search(pattern3, record2)
                            if match:
                                # Get the matched zip code
                                zip_code = match.group(0)

                                # Print the city name and zip code
                                print(city + " " + zip_code)
                                break


def q2_func():
    """
       Extracts completed runs from the input file and writes them to the output file.

       The function reads the contents of the input file ("atoms2.log") and searches for
       matches of a specific regex pattern representing completed runs. It then writes
       the matched run numbers and corresponding filenames to the output file
       ("completed_runs.txt").

       Input:
       - None

       Output:
       - None

       Side Effects:
       - Creates or overwrites the "completed_runs.txt" file with the run numbers and filenames.

       Example:
       >>> q2_func()
       (Assuming "atoms2.log" contains the following line)
       RUN 000001 COMPLETED. OUTPUT IN FILE hydrogen.
       (Assuming "completed_runs.txt" is created/written with the following content)
       000001 hydrogen.dat

       """
    # Define the input and output file paths
    input_file = "atoms2.log"
    output_file = "completed_runs.txt"

    # Define the regex pattern to extract the completed runs
    pattern = r"RUN (\d+) COMPLETED\. OUTPUT IN FILE (\w+)\."

    # Open the input and output files
    with open(input_file, "r") as input_f, open(output_file, "w") as output_f:
        # Read the contents of the input file
        content = input_f.read()

        # Find all matches of the pattern in the content
        matches = re.findall(pattern, content)

        # Write the completed runs to the output file
        for run, filename in matches:
            output_f.write(f"{run.zfill(6)} {filename + '.dat'}\n")


def main():
    """
    Executes the main control flow of the program.

    The function prompts the user to select a question by entering a choice number.
    Based on the user's choice, it calls the respective functions to perform the tasks.

    Input:
    - None

    Output:
    - None

    Side Effects:
    - Prints the result of the selected question or an error message for an invalid choice.

    Example:
    >>> main()
    Which question do you want to present? 1-Q1, 2-Q2: 1
    New York 12345
    Los Angeles 67890

    """
    # Take user input for selecting a question
    question_choice = input("Which question do you want to present? 1-Q1, 2-Q2: ")

    # Question 1
    if question_choice == "1":
        q1_func()

    # Question 2
    elif question_choice == "2":
        q2_func()

    # Invalid choice
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()







