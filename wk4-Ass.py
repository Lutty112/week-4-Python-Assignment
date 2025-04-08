def modify_content(content):
    """
    This function modifies the content in some way.
    For example, let's convert all text to uppercase.
    """
    return content.upper()

try:
    # Ask the user to input a filename
    input_filename = input("Enter the name of the file to read: ")

    # Open the file in read mode
    with open(input_filename, 'r') as infile:
        content = infile.read()

    # Modify the content
    modified_content = modify_content(content)

    # Define the output file name
    output_filename = "modified_" + input_filename

    # Write the modified content to a new file
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"File processed successfully! Modified content saved in '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except IOError:
    print(f"Error: Could not read or write files properly.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
