# CLIP_DDM
——Distinguish duck or mouse with CLIP

As you know, people have been debating endlessly whether the food in the picture is duck neck or mouse. Therefore, I want to see what artificial intelligence has to say. Here, I have used a pre-trained model called CLIP, which can effectively determine the textual information represented by an image.

## Usage
First, install PyTorch 1.7.1 (or later) and torchvision, as well as small additional dependencies, and then install this repo as a Python package. On a CUDA GPU machine, the following will do the trick:
```bash
$ conda install --yes -c pytorch pytorch=1.7.1 torchvision cudatoolkit=11.0
$ pip install ftfy regex tqdm
$ pip install git+https://github.com/openai/CLIP.git
```
Replace cudatoolkit=11.0 above with the appropriate CUDA version on your machine or cpuonly when installing on a machine without a GPU.

## Run
```bash
python main.py
```

## Output
```tex
It is a mouse
The probs of duck neck:  0.0012033392
The probs of a mouse:  0.9987966
```

## Video

You can watch my video about this code at https://www.bilibili.com/video/BV1Es4y1y71h on bilibili.

## Original CLIP

Thanks to [openai/CLIP](https://github.com/openai/CLIP)