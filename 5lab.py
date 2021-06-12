import re


def main():
    file_with_logs = open("acces_log.txt", "r")
    count = 0
    searched_lines = (
        "\[(0[8-9]|10)/Mar/2004:(0[2-9]|1[0-8]):([1-3][1-9]|40|41)"
        ':(3[7-9]|4[0-9]|5[0-2]) -0800] ".*" 200'
    )

    for strings in file_with_logs:
        for certain_string in re.finditer(searched_lines, strings):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
    
