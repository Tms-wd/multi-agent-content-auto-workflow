class BaseAgent:
    def __init__(self, name):
        self.name = name

    def log(self, msg):
        print(f"[{self.name}] {msg}")

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("PlannerAgent")

    def make_plan(self, topic):
        self.log(f"正在为主题 {topic} 制定计划")
        return ["生成", "审核", "发布"]

class AIGenAgent(BaseAgent):
    def __init__(self):
        super().__init__("AIGenAgent")

    def generate(self, prompt):
        self.log(f"正在生成：{prompt[:20]}...")
        return "生成完成的内容文本"
