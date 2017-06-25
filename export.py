from reports import *

output_file = "export.txt"
input_file = "game_stat.txt"


def clear_file():
    with open(output_file, "w"):
        pass


def write_in_file(answer):
    with open(output_file, "a") as output_stream:
        output_stream.write(str(answer)+"\n")


clear_file()

write_in_file(count_games(input_file))
write_in_file(decide(input_file, 2000))
write_in_file(get_latest(input_file))
write_in_file(count_by_genre(input_file, "First-person shooter"))
write_in_file(get_line_number_by_title(input_file, "Counter-Strike"))
write_in_file(sort_abc(input_file))
write_in_file(get_genres(input_file))
# Export functions
