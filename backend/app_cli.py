import argparse
import os
import time
from utils import parse_arg_boolean, parse_arg_dalle_version
from consts import ModelSize

print("--> Starting DALL-E Server. This might take up to two minutes.")

from dalle_model import DalleModel

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(
            f"readable_dir:{path} is not a valid path")

parser = argparse.ArgumentParser(description = "A DALL-E app to turn your textual prompts into visionary delights")
parser.add_argument("--model_version", type = parse_arg_dalle_version, default = ModelSize.MINI, help = "Mini, Mega, or Mega_full")
parser.add_argument(
    "--repro_dir",
    help=
    "Directory to which module files will be saved for reproduction or debugging.",
    type=dir_path,
    default="/tmp/")
args = parser.parse_args()

if __name__ == "__main__":
    print("setting up DallE")
    dalle_model = DalleModel(args.model_version)
    print("Generating images warm up")
    dalle_model.generate_images("warm-up", 1)
    text_prompt = "apple on the table"
    num_images = 1
    print("Generating actual images")
    generated_imgs = dalle_model.generate_images(text_prompt, num_images)
    print("Saving images")
    for idx, img in enumerate(generated_imgs):
        import pdb; pdb.set_trace()
        img.save(os.path.join(args.repro_dir, f'{idx}.jpeg'), format="JPEG")
