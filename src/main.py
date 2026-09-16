# --- 组装并运行完整的 ReAct 智能体 ---
from ToolExecutor import ToolExecutor
from search import search
from LLM import HelloAgentsLLM
from ReActAgent import ReActAgent


if __name__ == '__main__':
    # 1. 初始化工具执行器，并注册实战搜索工具
    toolExecutor = ToolExecutor()
    search_description = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    toolExecutor.registerTool("Search", search_description, search)

    print("\n--- 可用的工具 ---")
    print(toolExecutor.getAvailableTools())

    # 2. 初始化LLM客户端与ReAct智能体
    llm = HelloAgentsLLM()
    agent = ReActAgent(llm_client=llm, tool_executor=toolExecutor)

    # 3. 提出一个需要实时信息的问题，跑完整的 Thought/Action/Observation 循环
    question = "英伟达最新的GPU型号是什么"
    print(f"\n--- 提问: {question} ---")
    answer = agent.run(question)
    print(f"\n--- 最终结果 ---\n{answer}")

# 以下是旧版手动调用 Search 工具（不经过LLM/ReAct循环）时的示例输出，保留作参考：
# >>>
# 工具 'Search' 已注册。

# --- 可用的工具 ---
# - Search: 一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。

# --- 执行 Action: Search['英伟达最新的GPU型号是什么'] ---
# 🔍 正在执行 [SerpApi] 网页搜索: 英伟达最新的GPU型号是什么
# --- 观察 (Observation) ---
# [1] GeForce RTX 50 系列显卡
# GeForce RTX™ 50 系列GPU 搭载NVIDIA Blackwell 架构，为游戏玩家和创作者带来全新玩法。RTX 50 系列具备强大的AI 算力，带来升级体验和更逼真的画面。

# [2] 比较GeForce 系列最新一代显卡和前代显卡
# 比较最新一代RTX 30 系列显卡和前代的RTX 20 系列、GTX 10 和900 系列显卡。查看规格、功能、技术支持等内容。

# [3] GeForce 显卡| NVIDIA
# DRIVE AGX. 强大的车载计算能力，适用于AI 驱动的智能汽车系统 · Clara AGX. 适用于创新型医疗设备和成像的AI 计算. 游戏和创作. GeForce. 探索显卡、游戏解决方案、AI ...
