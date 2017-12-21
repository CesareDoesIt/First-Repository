from aocd import get_data
import re

session="53616c7465645f5f4812c0eed899485e9e63507b133fcfbe379ae7ec1e1b079ec98f2fb252334cca442f15e78dd50899"
#my_data = get_data(session, day=2, year=2017)
#print(my_data)


my_data = get_data(session, day=5, year=2017)
#print(my_data)


def escape_game(numbers):

    list_of_strings = numbers.split("\n")
    list_of_numbers = []
    current_position = 0
    count = 0
    for item in list_of_strings:
        list_of_numbers.append(int(item))

    while current_position < len(list_of_numbers):
            movement = list_of_numbers[current_position]
            new_position_number = list_of_numbers[current_position]
            if list_of_numbers[current_position] >= 3:
                list_of_numbers[current_position] += -1
                new_position_number = list_of_numbers[current_position]
            if list_of_numbers[current_position] < 3:
                if movement == new_position_number:
                    list_of_numbers[current_position] += 1
            current_position = movement + current_position
            count += 1
            if current_position >= len(list_of_numbers):
                break

    print(count)
    print(list_of_numbers)

# escape_game("0\n3\n0\n1\n-3")

escape_game(my_data)

# Day 4 -----------------------------------------------------------------

"""
my_data = get_data(session, day=4, year=2017)
#print(my_data)


def passphrase_possibilities(letter_sequences):

    rows_list = []
    word_rows_split = []
    sorted_lines = []
    sorted_words_in_lines = []
    joined_sorted_words = []
    count = 0

    for item in letter_sequences:
        rows_list = letter_sequences.split("\n")
    for item in rows_list:
        word_rows_split.append(item.split(" "))
    for item in word_rows_split:
        sorted_words_line = []
        for word in item:
            sorted_words_line.append(sorted(word))
        sorted_words_in_lines.append(sorted_words_line)
    for item in sorted_words_in_lines:
        joined_words = []
        for list in item:
            joined_words.append("".join(list))
        joined_sorted_words.append(joined_words)
    for item in joined_sorted_words:
        sorted_lines.append(sorted(item))
    for item in sorted_lines:
        x = -1
        y = 0
        while x + 2 < len(item):
            x += 1
            y = x + 1
            if item[x] == item[y]:
                count += 1
                x = -1
                y = x + 1
                break
    print(len(rows_list))
    valid_phrases_count = len(rows_list) - count
    print(valid_phrases_count)
    print(joined_sorted_words)


passphrase_possibilities(my_data)
"""

# Day 3 -------------------------------------------------------------------------

"""
def number_of_steps(data_square):

    a = 0
    b = 0
    c = 0
    d = 0
    side_adding_count = 1
    block_move_lists = []
    iteration = 1
    block_number = 2
    side_to_add_to = 1
    side_adding_count_variables = []
    for item in range(data_square):
        side_adding_count_variables.append(item + 1)
        side_adding_count_variables.append(item + 1)

    while block_number < data_square:
        if side_adding_count % 2 != 0:
            if iteration % 2 != 0:
                side_adding_count = side_adding_count_variables[iteration - 1]
                while side_to_add_to % 2 != 0:
                    while side_adding_count > 0:
                        each_block_number = [0, 0, 0, 0, 0]
                        a += 1
                        each_block_number[0] = block_number
                        each_block_number[1] = a
                        each_block_number[2] = b
                        each_block_number[3] = c
                        each_block_number[4] = d
                        block_move_lists.append(each_block_number)
                        block_number += 1
                        side_adding_count -= 1
                    if side_adding_count == 0:
                        side_to_add_to += 1
                        iteration += 1
                side_adding_count = side_adding_count_variables[iteration - 1]
                while side_to_add_to % 2 == 0:
                    while side_adding_count > 0:
                        each_block_number = [0, 0, 0, 0, 0]
                        b += 1
                        each_block_number[0] = block_number
                        each_block_number[1] = a
                        each_block_number[2] = b
                        each_block_number[3] = c
                        each_block_number[4] = d
                        block_move_lists.append(each_block_number)
                        block_number += 1
                        side_adding_count -= 1
                    if side_adding_count == 0:
                        side_to_add_to += 1
                        iteration += 1
            side_adding_count = side_adding_count_variables[iteration - 1]
            if side_adding_count % 2 == 0:
                if iteration % 2 != 0:
                    side_adding_count = side_adding_count_variables[iteration - 1]
                    while side_to_add_to % 2 != 0:
                        while side_adding_count > 0:
                            each_block_number = [0, 0, 0, 0, 0]
                            c += 1
                            each_block_number[0] = block_number
                            each_block_number[1] = a
                            each_block_number[2] = b
                            each_block_number[3] = c
                            each_block_number[4] = d
                            block_move_lists.append(each_block_number)
                            block_number += 1
                            side_adding_count -= 1
                        if side_adding_count == 0:
                            iteration += 1
                            side_to_add_to += 1
                    while side_to_add_to % 2 == 0:
                        side_adding_count = side_adding_count_variables[iteration - 1]
                        while side_adding_count > 0:
                            each_block_number = [0, 0, 0, 0, 0]
                            d += 1
                            each_block_number[0] = block_number
                            each_block_number[1] = a
                            each_block_number[2] = b
                            each_block_number[3] = c
                            each_block_number[4] = d
                            block_move_lists.append(each_block_number)
                            block_number += 1
                            side_adding_count -= 1
                        if side_adding_count == 0:
                            iteration += 1
                            side_to_add_to += 1
                    side_adding_count = side_adding_count_variables[iteration - 1]

    for item in block_move_lists:
        if item[0] == data_square:
            selected_moves = item

    perpendicular_moves = max(selected_moves[1], selected_moves[3]) - min(selected_moves[1], selected_moves[3])
    parallel_moves = max(selected_moves[2], selected_moves[4]) - min(selected_moves[2], selected_moves[4])
    number_of_moves = perpendicular_moves + parallel_moves
    print(block_move_lists)
    print(number_of_moves)
    return number_of_moves


number_of_steps(265149)
"""

# Day 2 ---------------------------------------------------------

"""my_data = get_data(session, day=2, year=2017)


def checksum(input):

    numbers = input
    split_rows = numbers.split("\n")
    string_lists = []
    number_lists = []
    sorted_lists = []
    divided_list = []
    sum = 0

    for item in split_rows:
        split_list = item.split("\t")
        string_lists.append(split_list)
    for item in string_lists:
        formatted_numbers = []
        for string_numbers in item:
            formatted_numbers.append(int(string_numbers))
        number_lists.append(formatted_numbers)
    for item in number_lists:
        sorted_lists.append(sorted(item, key=int, reverse=True))
    for item in sorted_lists:
        x = -1
        while x < len(item):
            x += 1
            y = x + 1
            while y < len(item):
                if item[x] % item[y] == 0:
                    divided_list.append(item[x]/item[y])
                    x = len(item) + 1
                    break
                else:
                    y += 1
    for item in divided_list:
        sum +=item

    print(number_lists)
    print(sum)


checksum(my_data)"""

# Day 1 ---------------------------------------------------------------------------------------

"""def duplicate_extractor(sequence):

    numbers_to_string = str(sequence)
    individual_numbers = []
    duplicates = []
    length = len(numbers_to_string)
    x = 0
    sum = 0

    for item in numbers_to_string:
        individual_numbers.append(int(item))
    while x < (length - 1):
        if x == 0:
            if individual_numbers[x] == individual_numbers[x + int(length / 2)]:
                duplicates.append(individual_numbers[x])
        x += 1
        y = (x + int(length / 2))
        if y <= (length - 1):
            if individual_numbers[x] == individual_numbers[y]:
                duplicates.append(individual_numbers[x])
        else:
            z = y - length
            if individual_numbers[x] == individual_numbers[z]:
                duplicates.append(individual_numbers[x])
    for item in duplicates:
        sum += item

    print(sum)
    return sum

duplicate_extractor(1212)  # 6
duplicate_extractor(1221)  # 0
duplicate_extractor(123425)  # 4
duplicate_extractor(123123)  # 12
duplicate_extractor(12131415)  # 4
duplicate_extractor(21752342814933766938172121674976879111362417653261522357855816893656462449168377359285244818489723869987861247912289729579296691684761143544956991583942215236568961875851755854977946147178746464675227699149925227227137557479769948569788884399379821111382536722699575759474473273939756348992714667963596189765734743169489599125771443348193383566159843593541134749392569865481578359825844394454173219857919349341442148282229689541561169341622222354651397342928678496478671339383923769856425795211323673389723181967933933832711545885653952861879231537976292517866354812943192728263269524735698423336673735158993853556148833861327959262254756647827739145283577793481526768156921138428318939361859721778556264519643435871835744859243167227889562738712953651128317624673985213525897522378259178625416722152155728615936587369515254936828668564857283226439881266871945998796488472249182538883354186573925183152663862683995449671663285775397453876262722567452435914777363522817594741946638986571793655889466419895996924122915777224499481496837343194149123735355268151941712871245863553836953349887831949788869852929147849489265325843934669999391846286319268686789372513976522282587526866148166337215961493536262851512218794139272361292811529888161198799297966893366553115353639298256788819385272471187213579185523521341651117947676785341146235441411441813242514813227821843819424619974979886871646621918865274574538951761567855845681272364646138584716333599843835167373525248547542442942583122624534494442516259616973235858469131159773167334953658673271599748942956981954699444528689628848694446818825465485122869742839711471129862632128635779658365756362863627135983617613332849756371986376967117549251566281992964573929655589313871976556784849231916513831538254812347116253949818633527185174221565279775766742262687713114114344843534958833372634182176866315441583887177759222598853735114191874277711434653854816841589229914164681364497429324463193669337827467661773833517841763711156376147664749175267212562321567728575765844893232718971471289841171642868948852136818661741238178676857381583155547755219837116125995361896562498721571413742
)
"""