# DEVELOPMENT SETUP

This setup is tested only on Mac and Linux.

## Dependencies

There is a package called torch(pyTorch) in the dependencies.
This has two versions.
    - GPU supported
    - CPU supported

On linux, by default, the GPU version gets installed, which is huge in size - close to 730+ MB. It crosses the package slug limit of 300MB on Heroku deployments.

Ro circumvent the problem, we need to install pyTorch-CPU only version. We need to add the following dependencies to the ```requirements.txt```

```bash
# requirements.txt
-f https://download.pytorch.org/whl/torch_stable.html
torch==1.6.0+cpu
torchvision==0.7.0+cpu
```

On Mac, there is no GPU support for pyTorch. adding ```+cpu``` will not work

But if we try to install the dependencies ```torch==1.6.0+cpu``` and ```torchvision==0.7.0+cpu``` on Mac, we get the following error

```text
Collecting torch==1.6.0+cpu (from -r requirements.txt (line 8))
  ERROR: Could not find a version that satisfies the requirement torch==1.6.0+cpu (from -r requirements.txt (line 8)) (from versions: 0.1.2, 0.1.2.post1, 0.1.2.post2, 0.4.1, 1.0.0, 1.0.1, 1.0.1.post2, 1.1.0, 1.1.0.post2, 1.2.0, 1.3.0, 1.3.0.post2, 1.3.1, 1.4.0, 1.5.0, 1.5.1, 1.6.0)
ERROR: No matching distribution found for torch==1.6.0+cpu (from -r requirements.txt (line 8))
```

So to keep the dependencies list separate for the two environments, we are using ```requirements.txt``` and ```requirements-dev.txt```

## Prerequisites

- Python >= 3.7
- [Poetry](https://python-poetry.org/)

## Getting Started

**Clone the repo**

```bash
git clone https://github.com/sravanrekandar/abhyasa.git & cd abhyasa
```

**Access Permissions to start_dev.sh**

```bash
chmod 777 start_dev.sh
```

**Start the application**

```bash
./start_dev.sh
```
