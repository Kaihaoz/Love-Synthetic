from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments
import torch

# 设置文件路径
dataset_path = "ai_love_journal_large_dataset.txt"
model_name = "gpt2"
output_dir = "./love_gpt2_finetuned"

# 加载 tokenizer 和模型
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # 处理 padding 问题
model = GPT2LMHeadModel.from_pretrained(model_name)

# 构建训练数据集
def load_dataset(file_path, tokenizer):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=128
    )

train_dataset = load_dataset(dataset_path, tokenizer)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# 设置训练参数
training_args = TrainingArguments(
    output_dir=output_dir,
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=100,
    save_total_limit=2,
    logging_steps=50,
    prediction_loss_only=True,
    fp16=torch.cuda.is_available(),
)

# 创建 Trainer 实例
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator,
)

# 训练模型
trainer.train()

# 保存模型
trainer.save_model(output_dir)
tokenizer.save_pretrained(output_dir)
