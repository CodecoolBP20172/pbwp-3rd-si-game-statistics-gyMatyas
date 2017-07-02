import math

# Constants for more readable working with lists.
TITLE = 0
COPIES = 1
YEAR = 2
GENRE = 3
PUBLISHER = 4


def games_in_file(file_name):
    with open(file_name, "r") as read_file:
        try:
            game_list = [line.strip().split("\t") for line in read_file]
        except FileNotFoundError:
            sys.exit("File not found!")
        return game_list


def get_most_played(file_name):
    game_list = games_in_file(file_name)
    most_played_game = str()
    most_sold_copies = float()
    for current_line in game_list:
        if float(current_line[COPIES]) > float(most_sold_copies):
            most_played_game = current_line[TITLE]
            most_sold_copies = current_line[COPIES]
    return most_played_game


def sum_sold(file_name):
    game_list = games_in_file(file_name)
    total_sold = float()
    for current_line in game_list:
        total_sold += float(current_line[COPIES])
    return total_sold


def get_selling_avg(file_name):
    with open(file_name) as file:
        num_lines = sum(1 for line in file)
    return (sum_sold(file_name)/num_lines)


def count_longest_title(file_name):
    game_list = games_in_file(file_name)
    count_longest = float()
    for current_line in game_list:
        if count_longest < len(current_line[TITLE]):
            count_longest = len(current_line[TITLE])
    return count_longest


def get_date_avg(file_name):
    game_list = games_in_file(file_name)
    count_date = float()
    with open(file_name, "r") as file:
        num_lines = sum(1 for line in file)
        for current_line in game_list:
            count_date += float(current_line[YEAR])
    return math.ceil(count_date/num_lines)


def get_game(file_name, title):
    game_list = games_in_file(file_name)
    return_list = list()
    for current_line in game_list:
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
    game_list = games_in_file(file_name)
    for current_line in game_list:
        if current_line[GENRE] in genres.keys():
            genres[current_line[GENRE]] += 1
        else:
            genres[current_line[GENRE]] = 1
    return genres


def get_date_ordered(file_name):
    game_list = games_in_file(file_name)
    sorted_list = sorted(sorted(game_list), key=lambda game: game[YEAR], reverse=True)  # sorts first alphabetically, sorts again by date.
    titles = list()
    for current_line in sorted_list:
        titles.append(current_line[TITLE])
    return titles


# Report functions
