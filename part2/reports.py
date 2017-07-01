import math


TITLE = 0
COPIES = 1
YEAR = 2
GENRE = 3
PUBLISHER = 4


def get_most_played(file_name):
    current_line = list()
    most_played_game = str()
    most_sold_copies = float()
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            current_line = line.split("\t")
            if float(current_line[COPIES]) > float(most_sold_copies):
                most_played_game = current_line[TITLE]
                most_sold_copies = current_line[COPIES]
    return most_played_game


def sum_sold(file_name):
    current_line = list()
    total_sold = float()
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            current_line = line.split("\t")
            total_sold += float(current_line[COPIES])
    return total_sold


def get_selling_avg(file_name):
    with open(file_name) as file:
        num_lines = sum(1 for line in file)
    return (sum_sold(file_name)/num_lines)


def count_longest_title(file_name):
    current_line = list()
    count_longest = float()
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            current_line = line.split("\t")
            if count_longest < len(current_line[TITLE]):
                count_longest = len(current_line[TITLE])
    return count_longest


def get_date_avg(file_name):
    current_line = list()
    count_date = float()
    with open(file_name, "r") as file:
        num_lines = sum(1 for line in file)
        file.seek(0)
        for line in file:
            line = line.strip()
            current_line = line.split("\t")
            count_date += float(current_line[YEAR])
    return math.ceil(count_date/num_lines)


def get_game(file_name, title):
    current_line = list()
    return_list = list()
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            current_line = line.split("\t")
            if title == current_line[TITLE]:
                for item in current_line:
                    try:
                        return_list.append(int(item))
                    except ValueError:
                        try:
                            return_list.append(float(item))
                        except ValueError:
                            return_list.append(item)
                return return_list
    return ("Game not found")


def count_grouped_by_genre(file_name):
    genres = dict()
    current_line = list()
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            current_line = line.split("\t")
            if current_line[GENRE] in genres.keys():
                genres[current_line[GENRE]] += 1
            else:
                genres[current_line[GENRE]] = 1
    return genres
# Report functions
