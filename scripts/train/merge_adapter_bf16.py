import os.path

import fire
#**************modified**************
# from peft import AutoPeftModelForCausalLM
try:
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from peft_m import AutoPeftModelForCausalLM
except ImportError:
    from peft import AutoPeftModelForCausalLM
#**************modified******************
from transformers import AutoTokenizer


def main(model_path):
    model = AutoPeftModelForCausalLM.from_pretrained(model_path)
    print('merging...')
    model = model.merge_and_unload()
    print('saving...')
    model.save_pretrained(os.path.join(model_path, 'merged'))
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    tokenizer.save_pretrained(os.path.join(model_path, 'merged'))


if __name__ == '__main__':
    fire.Fire(main)
