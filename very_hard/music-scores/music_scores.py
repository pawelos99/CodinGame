import numpy as np


def get_note(h_line_len, h_line_pos, note_pos):
    '''get dimensions and positions of a vertical line,
    and return a note and a score of note
    h_line_len - dimensions of note vertical line
    h_line_pos - position of vertical line on the image
    note_pos - position of note according to vertical
            line, 0 - on the left side, 1 - on the right
    '''
    (ul, dl), (ur, dr) = h_line_len
    u = max(ul, ur)
    d = min(dl, dr)
    dd = w_line_sep // 2

    # if note is on the left or right side of vertical
    # line, get their score and note
    if note_pos == 1:
        x = np.sum(notes_no_lines[max(0, u - dd):
                                  u + dd,
                                  h_line_pos:
                                  h_line_pos + w_line_sep + h_line_thick])
        note = notes_list[int(round((u - w_lines_pos_no_lines[0]
                                    + w_line_sep_no_lines)
                                    / (w_line_sep_no_lines / 2) + 0.01))]
    else:
        x = np.sum(notes_no_lines[max(0, d - dd):d + dd,
                                  h_line_pos - w_line_sep:h_line_pos])
        note = notes_list[int(round((d - w_lines_pos_no_lines[0]
                                    + w_line_sep_no_lines)
                                    / (w_line_sep_no_lines / 2) + 0.01))]
    score = 'Q' if x > 0.5 * w_line_sep_no_lines**2 else 'H'
    return note + score


# get input
w, h = [int(x) for x in input().split()]
inp = input()

# list of all notes form high G to lower C
notes_list = ['', 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'G', 'F', 'E', 'D', 'C']


# decode DWE to image (image - matrix of values 0 - W, 1 - B)
notes = np.empty(shape=[w*h], dtype=int)
image = np.array(inp.split())
image = np.reshape(image, [-1, 2])
pl = 0
for pxs in image:
    px = pxs[0]
    px_bit = (0, 1)[px == 'B']
    px_c = int(pxs[1])
    notes[pl:pl + px_c] = [px_bit] * px_c
    pl += px_c
notes = np.reshape(notes, [h, w])


# cropp image
sums_w = np.sum(notes, axis=1)
sums_h = np.sum(notes, axis=0)

ind_w = sums_w.nonzero()[0]
notes = np.delete(notes, list(range(ind_w[0])), 0)
notes = np.delete(notes, list(range(ind_w[-1] + 1 - ind_w[0],
                  h + 1 - ind_w[0])), 0)

ind_h = sums_h.nonzero()[0]
notes = np.delete(notes, list(range(ind_h[0])), 1)
notes = np.delete(notes, list(range(ind_h[-1]+1-ind_h[0], w+1-ind_h[0])), 1)

# w, h after croppig
w = len(notes[0])
h = len(notes)


# search for horizontal lines and get positions of them
sums_w = np.sum(notes, axis=1)
w_lines = np.where(sums_w > 0.8 * w, 1, 0)
w_lines = w_lines.nonzero()[0]
w_lines_sorted = np.reshape(w_lines, [5, -1])
w_lines_pos = [x[0] for x in w_lines_sorted]

# get horizontal line thickness and average line separation
w_line_sep = int(np.average([w_lines_pos[x + 1] - w_lines_pos[x]
                             for x in range(len(w_lines_pos)-1)]))
w_line_thick = len(w_lines_sorted[0])

# if there are extra notes below bottom line, add 6-th line
if w_lines_pos[-1] + w_line_sep * 1.4 < h:
    w_lines = np.append(w_lines, [w_lines[-1] + w_line_sep + x
                                  for x in range(-w_line_thick + 1, 1)])
    w_lines_pos.append(w_lines[-w_line_thick])
    w_lines_sorted = np.reshape(w_lines, [6, -1])


# search for vertical lines, and get positions of them
sums_h = np.sum(notes, axis=0)
h_limit = 5 * w_line_thick + w_line_sep * 1.2
h_lines = np.where(sums_h > h_limit, 1, 0)
h_lines = h_lines.nonzero()[0]

# get only positions of first left pixel of note vertical line
h_lines_sorted = []
prev_pos = h_lines[0]
for x in h_lines:
    if x - 1 == prev_pos:
        h_lines_sorted[-1].append(x)
    else:
        h_lines_sorted.append([x])
    prev_pos = x
h_lines_sorted = np.array(h_lines_sorted)
h_lines_pos = [x[0] for x in h_lines_sorted]

# get vertical line thickness
h_line_thick = len(h_lines_sorted[0])


# delete horizontal lines from image
notes_no_lines = np.delete(notes, w_lines, 0)

# h_lines_len - vertical line dimensions
h_lines_len_b = [np.nonzero(notes_no_lines[:, x])[0] for x in h_lines_pos]
h_lines_len_e = [np.nonzero(notes_no_lines[:, x + h_line_thick - 1])[0]
                 for x in h_lines_pos]
h_lines_len_b = [[x[0], x[-1]] for x in h_lines_len_b]
h_lines_len_e = [[x[0], x[-1]] for x in h_lines_len_e]
h_lines_len = list(zip(h_lines_len_b, h_lines_len_e))

# get lines positions and separations after deleting lines in image
w_lines_pos_no_lines = [w_lines_pos[x] - x * w_line_thick
                        for x in range(len(w_lines_pos))]
w_line_sep_no_lines = w_lines_pos_no_lines[1] - w_lines_pos_no_lines[0]

# 0 if note is on the left, 1 if note is on the right side of vertical
# line
notes_l_r = [(0, 1)[np.sum(notes_no_lines[:, x - 1]) == 0]
             for x in h_lines_pos]


# calculate and print results
result = [get_note(h_lines_len[x], h_lines_pos[x], notes_l_r[x])
          for x in range(len(h_lines_pos))]
print(*result, sep=' ')
