# Get input from the awesome user!
file = input("Name and extension of the file: ").lower().lstrip(' ').rstrip(' ')

# file is of this type, print the corresponding http header!
if file.endswith(".gif"):
    print("image/gif")
# File type match, and print the finale!
elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
# File type match, and print the finale!
elif file.endswith(".png"):
    print("image/png")
# File type match, and print the finale!
elif file.endswith(".pdf"):
    print("application/pdf")
# File type match, and print the finale!
elif file.endswith(".txt"):
    print("text/plain")
# File type match, and print the finale!
elif file.endswith(".zip"):
    print("application/zip")
else:
    # Print other file type that does not match!
    print("application/octet-stream")
