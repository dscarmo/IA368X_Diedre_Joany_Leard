import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument(dest="desc", type=str)

# Variables to experiment with
parser.add_argument("-bs", type=int, required=True)
parser.add_argument("-opt", type=str, required=True)
parser.add_argument("-precision", type=int, required=True)

# Fixed arguments
parser.add_argument("-debug", action="store_true")
parser.add_argument("-lr", type=float, default=0.0005)
parser.add_argument("-wd", type=float, default=1e-5)
parser.add_argument("-test_bs", type=int, default=1)
parser.add_argument("-max_epochs", type=int, default=300)
parser.add_argument("-channel_factor", type=float, default=1)
parser.add_argument("-nin", type=int, default=7)  # flair, t1, t1ce, t2, WT, TC, EC
parser.add_argument("-nout", type=int, default=1)  # survival
parser.add_argument("-rseed", type=int, default=4321)
parser.add_argument("-forced_overfit", type=float, default=0)
parser.add_argument("-dataset", type=str, default="BRATS")
parser.add_argument("-dataset_year", type=str, default="2020")
parser.add_argument("-splits", type=str, default="(0.7, 0.1, 0.2)")
parser.add_argument("-kfold", type=str, default="None")
parser.add_argument("-fold", type=str, default="None")

hyperparameters = parser.parse_args()

with open("hparams.pkl", 'wb') as hp:
    pickle.dump(hyperparameters, hp)
