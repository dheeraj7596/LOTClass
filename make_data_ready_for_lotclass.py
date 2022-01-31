import pickle, os


def from_c2f():
    df = pickle.load(open(pkl_dump_dir + "df_fine.pkl", "rb"))
    parent_to_child = pickle.load(open(pkl_dump_dir + "parent_to_child.pkl", "rb"))
    classes = parent_to_child["computer"]

    df = df[df.label.isin(classes)].reset_index(drop=True)

    f1 = open(lotclass_dump_dir + "classes.txt", "w")
    f2 = open(lotclass_dump_dir + "labels.txt", "w")
    f3 = open(lotclass_dump_dir + "dataset.txt", "w")

    label_to_idx = {}
    for i, l in enumerate(classes):
        label_to_idx[l] = i
        f1.write(l + "\n")

    for i, row in df.iterrows():
        f2.write(str(label_to_idx[row["label"]]) + "\n")
        f3.write(row["text"] + "\n")

    f1.close()
    f2.close()
    f3.close()


if __name__ == "__main__":
    basepath = "/Users/dheerajmekala/Work/WsupLD/data/nyt-coarse/"
    dataset = "nyt-coarse/"
    pkl_dump_dir = basepath
    lotclass_dump_dir = "/Users/dheerajmekala/Work/LOTClass/datasets/" + dataset
    os.makedirs(lotclass_dump_dir, exist_ok=True)

    df = pickle.load(open(pkl_dump_dir + "df.pkl", "rb"))
    classes = list(set(df["label"]))

    f1 = open(lotclass_dump_dir + "label_names.txt", "w")
    f2 = open(lotclass_dump_dir + "test_labels.txt", "w")
    f3 = open(lotclass_dump_dir + "train.txt", "w")
    f4 = open(lotclass_dump_dir + "test.txt", "w")

    label_to_idx = {}
    for i, l in enumerate(classes):
        label_to_idx[l] = i
        f1.write(l + "\n")

    for i, row in df.iterrows():
        f2.write(str(label_to_idx[row["label"]]) + "\n")
        f3.write(row["text"] + "\n")
        f4.write(row["text"] + "\n")

    f1.close()
    f2.close()
    f3.close()
    f4.close()
