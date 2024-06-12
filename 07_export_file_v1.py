import pandas

# Frames and content for export

variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"],
    "Quantity": [300, 300, 50],
    "Price": [1, .5, .75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork", "Advertising"],
    "Price": [25, 35, 10]
}

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recommended_price = "$5.00"

print(variable_frame)

# change dataframe to string (so it can written to a txt file)
variable_txt = pandas.DataFrame.to_string(variable_frame)

# Write to file
# create file to hold data (add. txt extension)
file_names = "{}.txt".format(product_name)
text_file = open(file_names, "w+")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

text_file.write(variable_txt)

#


# close file
text_file.closed()
