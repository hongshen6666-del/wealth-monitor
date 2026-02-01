import requests
import yfinance as yf
from urllib.parse import quote

# --- 核心配置 ---
# 已填入你提供的 Server酱 Key
MY_SCT_KEY = "SCT312361TSgF68tD65zMJj6NQPyto9vV1" 
# 设定你关注的金银比抄底水位
TARGET_RATIO = 50.0

def wealth_agent_final():
    print("🚀 财富代理启动：正在抓取全球实时行情...")
    try:
        # 1. 抓取实时数据 (GC=F 为黄金期货, SI=F 为白银期货)
        gold = yf.Ticker("GC=F").fast_info['last_price']
        silver = yf.Ticker("SI=F").fast_info['last_price']
        ratio = gold / silver
        
        print(f"---------------------------")
        print(f"📊 当前金价: ${gold:.2f}")
        print(f"📊 当前银价: ${silver:.2f}")
        print(f"📈 当前比例: {ratio:.2f}")
        print(f"---------------------------")

        # 2. 逻辑判断：如果比例达到 75 或以上则发送通知
        if ratio >= TARGET_RATIO:
            title = "【初食财富告警】金银比已破75！"
            content = (f"老板，当前金银比为 {ratio:.2f}。\n"
                       f"根据历史经验（如贝尔斯登事件时期），白银目前极具性价比。\n"
                       f"建议关注支撑位，考虑分批布局。")
            
            # Server酱 发送接口
            url = f"https://sctapi.ftqq.com/{MY_SCT_KEY}.send?title={quote(title)}&desp={quote(content)}"
            
            res = requests.get(url)
            if res.status_code == 200:
                print("🎊 信号已触发！微信通知已成功发出。")
            else:
                print(f"❌ 发送失败，代码: {res.status_code}")
        else:
            print(f"✅ 当前比例尚未到达 {TARGET_RATIO}，系统继续保持监控。")
            
    except Exception as e:
        print(f"❌ 运行错误: {e}。请检查网络或稍后重试。")

# 执行代理
wealth_agent_final()
