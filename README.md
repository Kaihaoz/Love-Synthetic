# Love, Synthetic：AI 递进式情感生成与可视化产品
🔗 **在线演示**：https://kaihaoz.github.io/Love-Synthetic/

## 📖 项目概述 (Project Overview)
本项目是一个端到端的 **AI 情感交互产品原型**。
针对日常情感表达中“缺乏层次感、递进式表达能力”的痛点，我利用 GPT-2 微调技术，构建了一套**“递进式情感生成+情感轨迹可视化”**系统。

它不仅仅是生成一句情话，而是通过算法模拟情感的**生成、递进与沉淀**，验证了 AI 在个性化情感表达与文创交互场景中的落地潜力。

## 🎯 核心痛点与产品定位 (Problem & Positioning)
### ❌ 核心痛点
1. **表达断层**：现有的 AI 写作工具多为单次文本生成，缺乏情绪的**递进式叙事**（如从害羞到深情的过程）。
2. **感知模糊**：用户无法直观理解 AI 是如何根据输入生成对应情感的，缺乏**透明度**。

### ✅ 产品目标
1. **功能创新**：实现 30 天递进式情感情书生成，模拟真实情感波动。
2. **体验优化**：通过 Sentence-BERT 与 t-SNE 可视化，让用户**看见**情感的变化轨迹。
3. **探索落地**：总结 AI 情感内容生成的产品化模式（Pattern）。

## 🔨 核心工作流 (Core Workflow)
作为独立开发者，我完成了从需求到落地的全流程：

1. **需求与策略设计**
   - 定义 **6 维情感递进曲线**（Love-Journey），规划 30 天的情感演变逻辑。
   - 设计 **Prompt 策略池**，控制 GPT-2 在不同日期的生成风格（甜蜜、思念、深情）。

2. **模型与数据处理**
   - 基于 GPT-2 进行 Fine-tuning，学习特定的情感语料风格。
   - 运用 **Sentence-BERT** 生成情感向量，利用 **t-SNE** 降维，实现情感轨迹的高维可视化。

3. **交互与可视化落地**
   - 设计并部署 **情感趋势可视化方案**，将抽象的情感向量转化为直观的视觉曲线。
   - 实现 GitHub Pages 在线演示，验证产品化可行性。

## 📊 技术栈 (Tech Stack)
*核心技术：* Python, PyTorch, GPT-2 (Fine-tuning)
*可视化与部署：* Sentence-BERT, t-SNE, Matplotlib/Seaborn, GitHub Pages

## 🌟 项目价值与亮点 (Project Value)
1. **产品化思维验证**：证明了**“AI 生成内容 + 情感可视化”**的产品形态在文创场景的可行性。
2. **递进式创新**：打破了 AI 生成仅局限于“单次输出”的现状，探索了**“时间序列情感交互”**的新路径。
3. **AI 落地参考**：提供了一套从模型训练到前端可视化展示的完整闭环，可复用至心理咨询、恋爱教育等垂直领域。

## 🚀 快速体验 (Quick Start)
1. **在线体验**：直接点击上方链接 [https://kaihaoz.github.io/Love-Synthetic/](https://kaihaoz.github.io/Love-Synthetic/)。
2. **本地运行**：
   ```bash
   git clone https://github.com/Kaihaoz/Love-Synthetic.git
   cd Love-Synthetic
   # 安装依赖
   pip install -r requirements.txt
   # 运行可视化脚本
   python code/plot_sentiment_trend.py
