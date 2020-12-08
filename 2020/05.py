def find_seats(place, char, deviation):
    if char == 'F' or char == 'L':
        place = [place[0], place[1] - deviation]
    if char == 'B' or char == 'R':
        place = [place[0] + deviation, place[1]]
    return place


def main():
    seat_ids = []
    with open('05_input') as file:
        file = list(file.readlines())
    for boarding_pass in file:
        count_rows_columns = [128, 8]
        seat = [[0, 127], [0, 7]]    # [row, column]
        for char in list(boarding_pass):
            if char == 'F' or char == 'B':
                count_rows_columns[0] /= 2
                seat[0] = find_seats(seat[0], char, count_rows_columns[0])
            else:
                count_rows_columns[1] /= 2
                seat[1] = find_seats(seat[1], char, count_rows_columns[1])
        seat_ids.append(int(seat[0][0] * 8 + seat[1][0]))
    print('Seat with highest ID:', max(seat_ids))
    for seat_id in range(max(seat_ids) - 1):
        if not seat_id == 1:
            if seat_id not in seat_ids and (seat_id - 1) in seat_ids and (seat_id + 1) in seat_ids:
                print('My seat: ', seat_id)
                break


if __name__ == '__main__':
    main()
