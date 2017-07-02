from reports import *

output_file = "export.txt"
input_file = "game_stat.txt"


def clear_file():
    with open(output_file, "w"):
        pass


def write_in_file(answer):
    with open(output_file, "a") as output_stream:
        output_stream.write(str(answer)+"\n")

# main
clear_file()
write_in_file(get_most_played(input_file))
write_in_file(sum_sold(input_file))
write_in_file(get_selling_avg(input_file))
write_in_file(count_longest_title(input_file))
write_in_file(get_date_avg(input_file))
write_in_file(get_game(input_file, "Counter-Strike"))
write_in_file(count_grouped_by_genre(input_file))
write_in_file(get_date_ordered(input_file))
