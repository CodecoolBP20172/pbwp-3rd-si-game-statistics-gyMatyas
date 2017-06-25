def count_games(file_name):
    line_number = 0
    with open(file_name, "r") as file:
        for line in file:
            line_number += 1
    return line_number


def decide(file_name, year):
    current_line = []
    with open(file_name, "r") as file:
        for line in file:
            current_line = line.split("\t")
            current_line_year = int(current_line[2])
            if current_line_year == year:
                return True
    return False


def get_latest(file_name):
    current_line = []
    title = ""
    latest_year = 0
    with open(file_name, "r") as file:
        for line in file:
            current_line = line.split("\t")
            current_line_year = int(current_line[2])
            if current_line_year > latest_year:
                title = current_line[0]
                latest_year = current_line_year
    return title


def count_by_genre(file_name, genre):
    current_line = []
    count = 0
    with open(file_name, "r") as file:
        for line in file:
            current_line = line.split("\t")
            if current_line[3] == genre:
                count +=1
    return count


def get_line_number_by_title(file_name, title):
    try:
        current_line = []
        line_number = 0
        with open(file_name, "r") as file:
            for line in file:
                line_number +=1
                current_line = line.split("\t")
                if current_line[0] == title:
                    return line_number
        raise ValueError("Game not found")
    except ValueError:
        return ("Game not found")


def sort_abc(file_name):
    titles = []
    current_line = []
    with open(file_name, "r") as file:
        for line in file:
            current_line = line.split("\t")
            if titles:
                inserted = False
                for title in titles:
                    if current_line[0] < title:
                        inserted = True
                        titles.insert(titles.index(title), current_line[0])
                        break
                if not inserted:
                    titles.append(current_line[0])
            else:
                titles.append(current_line[0])
    return titles


def get_genres(file_name):
    genres = []
    current_line = []
    with open(file_name, "r") as file:
        for line in file:
            current_line = line.split("\t")
            if genres:
                inserted = False
                duplicate = False
                for genre in genres:
                    if not duplicate:
                        if str.capitalize(current_line[3]) < str.capitalize(genre):
                            inserted = True
                            genres.insert(genres.index(genre), current_line[3])
                            break
                        elif current_line[3] == genre:
                            duplicate = True
                if not inserted and not duplicate:
                    genres.append(current_line[3])
            else:
                genres.append(current_line[3])
    return genres
# Report functions
