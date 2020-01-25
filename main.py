from argparse import ArgumentParser
import os, random, subprocess, shutil

TMP_DIR = '.fns_frames_%s/' % random.randint(0,99999)
DEVICE = '/gpu:0'
BATCH_SIZE = 4

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--input-img', type=str,
                        dest='input_img', help='please include the input image',
                        metavar='input_img', required=True)
    return parser



def main():
    parser = build_parser()
    print("parser.parse_args()", parser.parse_args())
    # opts = parser.parse_args()
    # evaluate.ffwd_video(opts.in_path, opts.out, opts.checkpoint, opts.device, opts.batch_size)

 
if __name__ == '__main__':
    main()
