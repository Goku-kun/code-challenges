import re

alignment = open("try_fasta", "r")
total_line_count = 0


def hamming_distance(str1, str2):
    i = 0
    count = 0

    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count


def clean_hyphens_and_stars(line):
    regex = r"-|\*"
    searched_result = re.search(regex, line)
    if searched_result is None:
        return line
    else:
        return "\n"


def extract_mid_sequence(line):
    regex = r"\s[A-Z]+\s"
    searched_result = re.findall(regex, line)
    if searched_result is None:
        return None
    return searched_result[0].strip()


with open('try_fasta') as file_one:
    ten_line_counter = 0
    line_list = file_one.readlines()
    clean_list_groups_of_ten = []
    running_group_of_ten = []
    for line in line_list:
        line = line.strip()
        if not line:
            continue
        ten_line_counter += 1
        running_group_of_ten.append(clean_hyphens_and_stars(line))
        if ten_line_counter == 10:
            clean_list_groups_of_ten.append(running_group_of_ten)
            running_group_of_ten = []
            ten_line_counter = 0


print(clean_list_groups_of_ten)
