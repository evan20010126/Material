import cv2
import numpy as np
import argparse
import os


class CustomParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument("--model_type", default="vit_h", type=str)
        self.parser.add_argument("--ckpt_point", default="./sam_vit_h_4b8939.pth", type=str)

        self.parser.add_argument(
            "--img", default="./demo/src/assets/data/dogs.jpg", type=str)
        self.parser.add_argument("--prompt_point", nargs="+", type=int, required=True)
        self.parser.add_argument("--prompt_label", nargs="+", type=int, required=True, help="label: 0 is background; 1 is foreground")
        self.parser.add_argument("--erode_iter", type=int, default=2)
        self.parser.add_argument("--dilate_iter", type=int, default=5)

        self.parser.add_argument("--output_folder", default="./outputs")
        self.parser.add_argument("--output_trimap", action='store_true')
        self.parser.add_argument("--output_all_mask", action='store_true')

    def make_parser(self):
        args = self.parser.parse_args()
        self.model_type = args.model_type
        self.ckpt_point = args.ckpt_point
        
        self.img = args.img
        self.prompt_point = args.prompt_point
        self.prompt_label = args.prompt_label
        self.erode_iter = args.erode_iter
        self.dilate_iter = args.dilate_iter

        self.output_folder = args.output_folder
        self.output_trimap = args.output_trimap
        self.output_all_mask = args.output_all_mask

if __name__ == '__main__':
    ARGS = CustomParser()
    ARGS.make_parser()
    os.makedirs(ARGS.output_folder, exist_ok=True)
    cropped_image, cropped_mask = generate_crop(ARGS)
    trimap = generate_trimap(ARGS, cropped_mask)

    # Pass "cropped_image", "trimap" to next part