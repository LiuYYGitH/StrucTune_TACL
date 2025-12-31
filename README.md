# StructTune
This repository includes the code for StructTune: Structured Sparse Fine-Tuning for Efficient Adaptation of Large Language Models
This repository is built based previous owesome work [RoSA](https://github.com/IST-DASLab/RoSA) and LLM training repository-[llm-foundry](https://github.com/mosaicml/llm-foundry)


## Installation
1. Create a clean environment and activate it:
```
conda create --name StrucTune python=3.10 -y
conda activate StrucTune
```

2. Install a version of [pytorch](https://pytorch.org/) (>=2.1.2) compatible with your CUDA (please use conda instead of pip to ensure all the dependencies are installed properly). For example, if you have CUDA version 11.8, run the following command:
```
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

3. Install this repository, which is a fork of [MosaicML's llm-foundry](https://github.com/mosaicml/llm-foundry) including the experiments presented in the paper:
```
pip install -e .  # refer to the setup.py for details
```

4. Install the [*spops*](https://github.com/IST-DASLab/spops) library, which we use under the hood to perform sparse operations: 
```
pip install git+https://github.com/IST-DASLab/spops.git
```

5. Install [RoSA's integration into huggingface's Parameter-Efficient Fine-Tuning (PEFT) library](https://github.com/IST-DASLab/peft-rosa) by running:
```
pip install git+https://github.com/IST-DASLab/peft-rosa.git
```

6. For evaluation, we use [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness). Run the following commands to install the compatible version:
```
git clone https://github.com/EleutherAI/lm-evaluation-harness.git
cd lm-evaluation-harness
git checkout 2c18e367c6ded428863cd1fd4cf9558ca49d68dc
pip install -e .
cd ..
```

## Training & Evaluation
### Training
... (to be completed soon)
### MBPP evaluation
```./MBPP```. Built based on [repository](https://github.com/deepseek-ai/DeepSeek-Coder/tree/main/Evaluation/MBPP)
### HumanEval evaluation
```./HumanEval```. Built based on [repository](https://github.com/openai/human-eval/tree/master)


