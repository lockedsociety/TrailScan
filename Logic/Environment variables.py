import os

for key, value in os.environ.items():
    # Check if the environment variable value contains a semicolon
    if ';' in value:
        # Split the value by semicolon and print each part with proper indentation
        values = value.split(';')
        indentation = ' ' * (len(key)+3)
        print(f'{key} = {values[0]}')
        for val in values[1:]:
            print(f'{indentation}{val.strip()}')
    else:
        # If there are no semicolons in the value, print it as is
        print(f'{key} = {value}')
