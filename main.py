import os
import logging
from dotenv import load_dotenv

# 配置日志
logging.basicConfig(
    filename='./logs/workflow.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PlannerAgent:
    def plan_task(self, user_input: str):
        """解析用户需求，拆解任务"""
        logger.info(f"Planner Agent 收到需求: {user_input}")
        return {
            "topic": user_input,
            "steps": ["research", "generate", "review", "publish"]
        }

class ExecutorAgent:
    def generate_content(self, task_plan: dict):
        """根据任务计划调用大模型生成内容"""
        logger.info(f"Executor Agent 开始生成内容: {task_plan['topic']}")
        return f"生成的关于「{task_plan['topic']}」的初稿内容"

class ReviewerAgent:
    def review_content(self, content: str):
        """审核生成的内容"""
        logger.info("Reviewer Agent 开始审核内容")
        return {"passed": True, "revised_content": content}

def run_workflow(user_input: str):
    """运行完整的多Agent工作流"""
    logger.info("===== 多Agent工作流启动 =====")
    
    planner = PlannerAgent()
    executor = ExecutorAgent()
    reviewer = ReviewerAgent()

    # 1. 规划任务
    plan = planner.plan_task(user_input)
    # 2. 执行生成
    draft = executor.generate_content(plan)
    # 3. 审核修正
    review_result = reviewer.review_content(draft)

    logger.info(f"工作流执行完毕，结果：{review_result}")
    print("✅ 多Agent工作流执行完成！")
    print(f"📝 最终输出：{review_result['revised_content']}")

if __name__ == "__main__":
    # 示例运行
    run_workflow("一篇关于AI多Agent应用的技术博客")
