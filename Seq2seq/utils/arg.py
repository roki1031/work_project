import argparse
import os
cur_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
print(cur_dir)
def parse_args():
    parser = argparse.ArgumentParser()
    # Required parameters
    parser.add_argument("--output_dir", default=f'{cur_dir}/output', type=str,
                        help="The output directory where the model checkpoints and predictions will be written.",
                        )
    parser.add_argument("--train_file", default=f'{cur_dir}/data/train.json', type=str,  help="The input training file.")
    parser.add_argument("--dev_file", default= f'{cur_dir}/data/train.json', type=str,  help="The input evaluation file.")
    parser.add_argument("--test_file", default= f'{cur_dir}/data/train.json', type=str,  help="The input testing file.")

    parser.add_argument("--model_type",
                        default="bert", type=str
                        )
    parser.add_argument("--model_checkpoint",
                        default=f'{cur_dir}/Helsinki-NLP', type=str,
                        help="Path to pretrained model or model identifier from huggingface.co/models",
                        )
    parser.add_argument("--max_input_length", default = 32, type=int)
    parser.add_argument("--max_target_length", default= 32, type=int)

    parser.add_argument("--do_train", default = 0, action="store_true", help="Whether to run training.")
    parser.add_argument("--do_test", action="store_true", help="Whether to run eval on the test set.")
    parser.add_argument("--do_predict", action="store_true", help="Whether to save predicted labels.")

    # Other parameters
    parser.add_argument("--learning_rate", default=1e-5, type=float, help="The initial learning rate for Adam.")
    parser.add_argument("--num_train_epochs", default=3, type=int, help="Total number of training epochs to perform.")
    parser.add_argument("--batch_size", default=4, type=int)
    parser.add_argument("--seed", type=int, default=42, help="random seed for initialization")

    parser.add_argument("--adam_beta1", default=0.9, type=float,
                        help="Epsilon for Adam optimizer."
                        )
    parser.add_argument("--adam_beta2", default=0.98, type=float,
                        help="Epsilon for Adam optimizer."
                        )
    parser.add_argument("--adam_epsilon", default=1e-8, type=float,
                        help="Epsilon for Adam optimizer."
                        )
    parser.add_argument("--warmup_proportion", default=0.1, type=float,
                        help="Proportion of training to perform linear learning rate warmup for,E.g., 0.1 = 10% of training."
                        )
    parser.add_argument("--weight_decay", default=0.01, type=float,
                        help="Weight decay if we apply some."
                        )
    args = parser.parse_args()
    return args
if  __name__ == '__main__':
    args = parse_args()
    print(args.train_file)