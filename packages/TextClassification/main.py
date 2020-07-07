from argparse import ArgumentParser
import Unsupervised

if __name__ == "__main__":

# Arguments
    parser = ArgumentParser()
    parser.add_argument("--mode", dest="mode", default="train", required=True, help='Set mode (fine_tuning, train, predict)')
    parser.add_argument("--run_id_model", dest="run_id_model", default="", required=False, help='Set run id where the model to be used is found (predict mode only)')
    parser.add_argument("--number_of_topics", dest="number_of_topics", default=0, required=True, type=int, help='Set number of topics (train mode only)')
    parser.add_argument("--alpha", dest="alpha", default=0, required=False, type=float, help='Set alpha (train mode only)')
    parser.add_argument("--beta", dest="beta", default=0, required=False, type=float, help='Set beta (train mode only)')
    args = parser.parse_args()
    
    classifier = Unsupervised.Classifier(args)
    data = classifier.getSampleData()
    classifier.preProcess()
    classifier.run(args)