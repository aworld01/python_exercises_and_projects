def strftr(string):
    data = [] #empty list
    split_by_dot = string.split(".") #split by dot
    for line in split_by_dot:
        strip = line.lstrip() #to remove left-sided spaces

        split_by_comma = strip.split(",") #split by comma
        for line in split_by_comma:
            strip = line.lstrip()

            split_by_qmark = strip.split("?") #split by question mark
            for line in split_by_qmark:
                strip = line.lstrip()

                lower = strip.lower() #to change into lowercase
                data.append(lower) #to add into empty list
    return data

if __name__ == "__main__":
    s = "Hello there, how are you? My name is Abdul Zoha. What is your name? How old are you? What are you doing? Long long ago. There was a king"
    data = strftr(s)
    print(data)
