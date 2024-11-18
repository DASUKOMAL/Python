'''Given an email ID email = "john.doe@example.com", extract the username ("john.doe") and domain ("example.com") using slicing.
Extract only the top-level domain (".com") from the email using slicing with negative indexing.
'''

# Define the email ID
email_id = "john.doe@example.com"

# Find the position of the '@' symbol in the email
index = email_id.index("@")

# Find the position of the first '.' in the email (this could be used for getting the domain part)
index2 = email_id.index(".")

# Extract the username from the start of the email up to the '@' symbol
username = email_id[:index]

# Extract the domain part (from the '@' symbol onwards, excluding the '@')
domain_id = email_id[index+1:]

# Extract the top-level domain (TLD) using negative indexing, starting from the last '.' character
top_level_domain = email_id[-index2:]  # This slices from the last '.' to the end of the string

# Print the username
print("The username is:", username)

# Print the domain ID (which includes the domain and the TLD)
print("The domain ID is:", domain_id)

# Print the top-level domain (TLD) like ".com"
print("The top-level domain is:", top_level_domain)
