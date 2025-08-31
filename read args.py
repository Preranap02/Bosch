#Write a program to read command-line arguments using sys.argv.
import sys
print(f"Script name: {sys.argv[0]}")
if len(sys.argv) > 1:
        print("Command-line arguments passed:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
else:
        print("No command-line arguments were passed.")