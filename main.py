import musicalbeeps
tab = []

def main():
    highest_string = 42
    notes = []
    biggest_line_len = 0

    with open('example.txt', 'r') as f:
        txt = f.readlines()
        flatten_notes = []
        for line in txt:
            if len(line) > biggest_line_len:
                biggest_line_len = len(line)
        flatten_notes = [[] for x in range(biggest_line_len)]
        for i, line in enumerate(txt):

            notes.append([])
            note = ''
            count = 0
            for char in line:
                if char.isnumeric():
                    note += char
                else:
                    if note != '':
                        nt = int(note)
                        pos = count - len(note)
                        notes[-1].append((nt, pos))
                        abs_nt = (highest_string - 5 * i) + nt
                        flatten_notes[pos].append(abs_nt)
                        note = ''
                count += 1
        ct = 0
        last_note_pos = -1
        for n in flatten_notes:
            if len(n) == 0:
                ct += 1
            else:
                if last_note_pos < 0:
                    last_note_pos = ct
                    ct = 0
                    continue
                #TODO: take care of polynotes
                flatten_notes[last_note_pos] = [ct, flatten_notes[last_note_pos][0]]
                last_note_pos += ct
                ct = 0

        return flatten_notes


def to_note(n: int):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = n // 12 + 1
    note = notes[n % 12]
    return f"{note[:1]}{octave}{note[1:]}"




if __name__ == '__main__':

    tab = main()

    player = musicalbeeps.Player(volume=0.3, mute_output=False)
    for n in tab:
        if len(n) > 0:
            for s in n:
                player.play_note(to_note(s))
