import sys
from sklearn.metrics import classification_report

if __name__ == "__main__":
    p = sys.argv[1]
    base_path = "./datasets/" + p + "/"
    f = open(base_path + "label_names.txt", "r")
    lines = f.readlines()
    f.close()

    label_to_index = {}
    index_to_label = {}
    for i, l in enumerate(lines):
        lab = lines[i].strip()
        label_to_index[lab] = i
        index_to_label[i] = lab

    f = open(base_path + "out.txt", "r")
    pred_lines = f.readlines()
    f.close()

    f = open(base_path + "test_labels.txt", "r")
    true_lines = f.readlines()
    f.close()

    assert len(true_lines) == len(pred_lines)
    length = len(true_lines)

    preds = []
    true = []
    for i in range(length):
        preds.append(index_to_label[int(pred_lines[i].strip())])
        true.append(index_to_label[int(true_lines[i].strip())])

    print(classification_report(true, preds))
