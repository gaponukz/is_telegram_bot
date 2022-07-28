import itertools

output_data: list[list[bool]] = []
metric_data = ['avatar', 'username', 'lastname', 'bio', 'url_in_bio', 'message']

for item in itertools.product([0, 1], repeat=6):
    item = list(item)
    string = '; '.join([f"{metric_data[i]}{'+' if item[i] else '-'}" for i in range(len(item))]) + " : "
    item.append(int(bool(input(string))))
    output_data.append(item)

for item in output_data:
    print(str(item).replace(', ', ',').replace('[', '').replace(']', ''))