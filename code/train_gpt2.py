from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments
import os

# Absolute path to your training text file
train_file_path = "/Users/zhangkaihao/Documents/GitHub/Critical-Coding-3-2025/final project/ai_love_letters_500.txt"

assert os.path.exists(train_file_path), f"❌ Training file not found: {train_file_path}"

print("🔹 Loading GPT-2 and tokenizer...")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

print("🔹 Loading training dataset...")
train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path=train_file_path,
    block_size=128,
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

training_args = TrainingArguments(
    output_dir="./trained_model",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=100,
    save_total_limit=1,
    logging_steps=50,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

print("🚀 Training started...")
trainer.train()
print("✅ Training complete! Model saved to ./trained_model")

model.save_pretrained("./trained_model")
tokenizer.save_pretrained("./trained_model")
