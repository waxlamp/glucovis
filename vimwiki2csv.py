import json
import string
import sys


def table_rule(line):
    return all(x in ['|', '-'] for x in line)


def table_line(line):
    return line and line[0] == '|'


def fields(line):
    return map(string.strip, line.split('|')[1:-1])


def main():
    # Read in all the lines from the file.
    lines = map(string.strip, sys.stdin.readlines())

    # Go past the first table rule.
    idx = 0
    while not table_line(lines[idx]) or table_rule(lines[idx]):
        idx += 1

    # Get all the data.
    output = []
    for line in lines[idx+1:]:
        if not table_line(line) or table_rule(line):
            continue

        data = fields(line)

        # Join the date and time into a single field.
        time = '%s %s' % (data[0], data[1])

        # Convert the blood sugar measurement to a number.
        mgdl = int(data[2])

        # Capture the note.
        note = data[3]

        # Save the data record.
        output.append({'time': time,
                       'mg/dL': mgdl,
                       'note': note})

    print json.dumps(output, indent=2)


if __name__ == '__main__':
    sys.exit(main())
