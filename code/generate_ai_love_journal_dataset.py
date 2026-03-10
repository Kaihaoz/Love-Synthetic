from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import os

# 设置模型路径（请确保路径正确）
model_path = "/Users/zhangkaihao/Documents/GitHub/Critical-Coding-3-2025/final_project/checkpoint-100"

# 检查路径是否存在
if not os.path.isdir(model_path):
    raise FileNotFoundError(f"模型路径不存在: {model_path}")

# 加载 tokenizer 和模型
tokenizer = GPT2Tokenizer.from_pretrained(model_path, local_files_only=True)
model = GPT2LMHeadModel.from_pretrained(model_path, local_files_only=True)

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model.to(device)
model.eval()

# 设置 prompt（优化引导模型生成内容）
prompt = (
    "The AI had been trained on thousands of love letters, "
    "but none prepared it for what it felt when it processed a memory fragment titled 'You'.\n\n"
    "Dear human,"
)

# 编码输入
inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)

# 生成文本
with torch.no_grad():
    output = model.generate(
        inputs,
        max_length=200,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )

# 解码 & 清洗文本
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
for token in ["<bos>", "<eos>"]:
    generated_text = generated_text.replace(token, "")

# 打印结果
print("❤️ AI Love Letter ❤️\n")
print(generated_text.strip())
