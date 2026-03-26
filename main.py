import json
import time
import random
from datetime import datetime

# 模拟大语言模型API调用（实际项目中替换为真实API）
class MockLLMClient:
    """模拟大语言模型客户端，用于语法分析和重述"""
    
    def analyze_grammar(self, user_sentence):
        """分析用户句子的语法错误并返回纠正后的句子"""
        # 模拟常见的语法错误模式
        error_patterns = [
            ("he go to school", "he goes to school"),
            ("i is a student", "i am a student"),
            ("she don't like it", "she doesn't like it"),
            ("yesterday i eat pizza", "yesterday i ate pizza"),
            ("they was happy", "they were happy")
        ]
        
        # 检查是否有匹配的错误模式
        user_sentence_lower = user_sentence.lower()
        for wrong, correct in error_patterns:
            if wrong in user_sentence_lower:
                return {
                    "original": user_sentence,
                    "corrected": correct,
                    "error_type": "语法错误",
                    "explanation": f"检测到动词形式错误，已纠正为: {correct}"
                }
        
        # 如果没有错误，返回原句
        return {
            "original": user_sentence,
            "corrected": user_sentence,
            "error_type": "无错误",
            "explanation": "句子语法正确！"
        }
    
    def generate_response(self, corrected_sentence):
        """基于纠正后的句子生成AI回应，保持对话连贯性"""
        responses = [
            f"很好！你说 '{corrected_sentence}'。我们继续对话吧。",
            f"明白了，'{corrected_sentence}'。接下来我们可以聊聊你的兴趣爱好。",
            f"不错！'{corrected_sentence}' 这个表达很地道。",
            f"好的，'{corrected_sentence}'。让我们练习下一个场景。"
        ]
        return random.choice(responses)

# 口语教练主类
class SpeakNowAICoach:
    """AI口语教练核心类，实现即时纠错功能"""
    
    def __init__(self):
        self.llm_client = MockLLMClient()
        self.session_start = datetime.now()
        self.conversation_history = []
        self.error_count = 0
        
    def process_user_input(self, user_sentence):
        """处理用户输入：分析语法并生成回应"""
        print(f"\n[用户] {user_sentence}")
        
        # 记录对话历史
        self.conversation_history.append({
            "role": "user",
            "content": user_sentence,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
        
        # 步骤1: 语法分析
        print("正在分析语法...")
        time.sleep(0.5)  # 模拟处理时间
        analysis_result = self.llm_client.analyze_grammar(user_sentence)
        
        # 步骤2: 显示纠错结果
        if analysis_result["error_type"] != "无错误":
            self.error_count += 1
            print(f"🔍 语法分析结果: {analysis_result['error_type']}")
            print(f"💡 建议: {analysis_result['explanation']}")
            print(f"✅ 正确表达: {analysis_result['corrected']}")
        else:
            print("✅ 语法正确！")
        
        # 步骤3: 生成AI回应
        print("生成AI回应...")
        time.sleep(0.3)
        ai_response = self.llm_client.generate_response(analysis_result["corrected"])
        
        # 记录AI回应
        self.conversation_history.append({
            "role": "ai",
            "content": ai_response,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
        
        print(f"[AI教练] {ai_response}")
        return ai_response
    
    def get_session_stats(self):
        """获取当前会话统计信息"""
        session_duration = (datetime.now() - self.session_start).seconds
        return {
            "duration_seconds": session_duration,
            "total_messages": len(self.conversation_history),
            "error_count": self.error_count,
            "accuracy_rate": 1 - (self.error_count / max(len(self.conversation_history)/2, 1))
        }
    
    def run_conversation_demo(self):
        """运行演示对话"""
        print("=" * 50)
        print("SpeakNow AI口语教练 - 即时语法纠错系统")
        print("=" * 50)
        print("开始对话练习（输入'退出'结束）\n")
        
        # 预设的演示对话
        demo_dialogue = [
            "he go to school every day",
            "i is a student from china",
            "yesterday i eat pizza with friends",
            "she don't like coffee"
        ]
        
        for sentence in demo_dialogue:
            self.process_user_input(sentence)
            
            # 模拟用户继续对话
            continue_prompt = input("\n按回车继续下一个句子，或输入'退出'结束: ")
            if continue_prompt.lower() == '退出':
                break
        
        # 显示会话统计
        self.show_session_summary()

    def show_session_summary(self):
        """显示会话总结"""
        stats = self.get_session_stats()
        print("\n" + "=" * 50)
        print("会话总结报告")
        print("=" * 50)
        print(f"会话时长: {stats['duration_seconds']}秒")
        print(f"对话轮次: {stats['total_messages']//2}轮")
        print(f"发现错误: {stats['error_count']}个")
        print(f"语法准确率: {stats['accuracy_rate']:.1%}")
        print(f"平均单次使用时长提升: 35% (模拟数据)")
        print(f"功能留存率提升: 20% (模拟数据)")
        print("=" * 50)

# 主函数
def main():
    """主程序入口"""
    try:
        # 创建AI口语教练实例
        ai_coach = SpeakNowAICoach()
        
        # 运行演示对话
        ai_coach.run_conversation_demo()
        
        print("\n感谢使用SpeakNow AI口语教练！")
        
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n程序运行出错: {e}")

if __name__ == "__main__":
    main()