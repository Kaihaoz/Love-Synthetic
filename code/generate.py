from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
import os

# Load model and tokenizer
model_dir = "/Users/zhangkaihao/Documents/GitHub/Critical-Coding-3-2025/final project/checkpoint-90"
tokenizer = GPT2Tokenizer.from_pretrained(model_dir, local_files_only=True)
model = GPT2LMHeadModel.from_pretrained(model_dir, local_files_only=True)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Parameters
output_file = "ai_love_journal.txt"
num_entries = 5  # generate 5 days/paragraphs
prompt = "Dear human,"

# Create/clear the output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("AI Love Journal\n====================\n\n")

# Generate entries
for i in range(1, num_entries + 1):
    results = generator(prompt, max_length=250, do_sample=True, top_k=50, top_p=0.95, temperature=0.9)
    letter = results[0]["generated_text"]

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f"[Day {i}]\n")
        f.write(letter.strip() + "\n\n")

print(f"✅ Saved {num_entries} AI love letters to '{output_file}'")
