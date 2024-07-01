# ML2024

## Introduction
This repository contains the final project for the Spring 2024 Machine Learning course. The main content is the experimental reproduction of the class-incremental learning theoretical model from the WA [[paper](https://arxiv.org/abs/1911.07053)]. The code in this repo is based on the WA model from [PyCIL](https://github.com/G-U-N/PyCIL), with the addition of weight imbalance implementation and some minor modifications. Additionally, it includes a series of experimental results and plotting code.

## Method Reproduced
The code can only run the WA model. For running additional models, please refer to [PyCIL](https://github.com/G-U-N/PyCIL).

## How To Use

### Requirements
- torch >= 1.8.1
- torchvision  >= 0.6.0
- tqdm
- numpy
- scipy

Note: In versions of torch above 1.10.1, the weight matrix might not output properly.

### Running

1. Edit the `wa.json` file for global settings.
2. Edit the hyperparameters in the corresponding `wa.py` file.
3. Run:

```bash
python main.py
```

### Datasets
When training on `CIFAR100`, this framework will automatically download it. When training on `imagenet100/1000`, you should specify the folder of your dataset in `utils/data.py`.

```python
def download_data(self):
    assert 0,"You should specify the folder of your dataset"
    train_dir = '[DATA-PATH]/train/'
    test_dir = '[DATA-PATH]/val/'
```

## License
Please check the MIT [license](./LICENSE) that is listed in this repository.
