import streamlit as st

import random
from streamlit.components.v1 import html
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, date, timedelta
import calendar
# stu_name='Lock'
# st.title("学生成绩看板")
# st.header(stu_name+'成绩单')
# data = [
#     # ['课程','成绩','GPA'],
#     ["物理", 90, 1],
#     ["化学", 80, 1],
#     ["英语", 70, 1],
#     ["数学", 85, 1],
#     ["历史", 75, 1]
# ]
#
# df = pd.DataFrame(data, columns=["科目", "成绩", "GPA"])
#
# categories = df["科目"].tolist()
# values = df["成绩"].tolist()
#
# # 创建雷达图
# fig = go.Figure()
#
# fig.add_trace(go.Scatterpolar(
#     r=values + [values[0]],  # 闭合雷达图
#     theta=categories + [categories[0]],
#     fill='toself',
#     name='Locke',
#     line=dict(color='royalblue', width=2),
#     fillcolor='rgba(65, 105, 225, 0.4)'
# ))
# st.plotly_chart(fig, use_container_width=True)
#
#
#
#
# st.dataframe(df,hide_index=True,column_config={
#         "科目": st.column_config.TextColumn("科目", width="medium"),
#         "成绩": st.column_config.NumberColumn(
#             "分数",
#             help="满分100分",
#             min_value=0,
#             max_value=100,
#             format="%d分"
#         ),
#         "GPA": st.column_config.NumberColumn(
#             "GPA",
#             help="4分制GPA",
#             min_value=0,
#             max_value=4,
#             format="%.1f"
#         )
#     },)
# st.subheader("成绩分析")
# col1, col2 = st.columns(2)
# with col1:
#     st.metric("平均分", f"{df['成绩'].iloc[::].mean():.1f}分")
# with col2:
#     st.metric("GPA", f"{df['GPA'].iloc[::].mean():.2f}")
#
# # 添加交互式图表
# st.bar_chart(df[:-1].set_index("科目")["成绩"])

st.set_page_config(
    page_title="公开课邀请",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 自定义CSS样式
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap');

body {
    background: #f9d8e0;
    overflow-x: hidden;
    font-family: 'Noto Sans SC', sans-serif;
}

/* 标题样式 */
.title {
    color: #ff69b4;
    text-align: center;
    font-size: 2.2rem;
    font-weight: 700;
    margin: 1.5rem 0;
}

/* 气球动画 */
@keyframes float {
    0% { transform: translateY(100vh) translateX(0); }
    100% { transform: translateY(-100vh) translateX(calc({0} * 100px)); }
}

.balloon {
    width: 50px;
    height: 60px;
    background: {color};
    border-radius: 50%;
    position: fixed;
    animation: float {duration}s linear infinite;
    opacity: 0.8;
    clip-path: ellipse(25px 30px at 50% 50%);
    cursor: pointer;
    transition: transform 0.2s;
}

.balloon:hover {
    transform: scale(1.1);
}

.balloon.popped {
    animation: pop 0.5s forwards;
    pointer-events: none;
}

@keyframes pop {
    0% { transform: scale(1); opacity: 0.8; }
    50% { transform: scale(1.2); opacity: 1; }
    100% { transform: scale(0); opacity: 0; }
}

/* 信息容器 */
.info-container {
    background: rgba(255, 255, 255, 0.85);
    border-radius: 12px;
    padding: 25px;
    margin: 20px auto;
    max-width: 500px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    position: relative;
    z-index: 10;
}

.info-item {
    margin: 18px 0;
    font-size: 1.1rem;
    color: #333;
    line-height: 1.6;
}

/* 图标样式 */
.info-item strong {
    color: #ff69b4;
}

/* 场景容器 */
.scene-container {
    display: flex;
    justify-content: center;
    margin: 30px auto;
    width: 100%;
}

.computer, .students {
    width: 120px;
    height: 120px;
    margin: 0 20px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
}

.computer {
    background-image: url('https://www.svgrepo.com/show/331309/coding.svg');
    animation: typing 2s infinite;
}

.students {
    background-image: url('https://www.svgrepo.com/show/331466/student.svg');
    animation: blink 3s infinite;
}

@keyframes typing {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.8; }
}
</style>
"""

# 气球点击爆裂的JavaScript
balloon_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const balloons = document.querySelectorAll('.balloon');
    balloons.forEach(balloon => {
        balloon.addEventListener('click', function() {
            this.classList.add('popped');
            // 播放爆裂音效
            const popSound = new Audio('https://assets.mixkit.co/sfx/preview/mixkit-balloon-pop-with-delay-2354.mp3');
            popSound.play();
            // 1秒后移除气球元素
            setTimeout(() => {
                this.remove();
            }, 1);
        });
    });
});
</script>
"""

# 生成随机气球
balloons = ""
colors = ["#ff69b4", "#7fffd4", "#ffd700", "#98fb98", "#87cefa"]
for _ in range(8):
    color = random.choice(colors)
    left = random.randint(0, 90)
    duration = random.randint(8, 15)
    balloons += f"""
    <div class="balloon" style="
        left: {left}%;
        animation: float {duration}s linear infinite;
        background: {color};
    "></div>
    """
# 公开课信息HTML
info_html = """
<div class="info-container">
    <div class="info-item">🗓 <strong>时间</strong>: 2025年04月23日 14:15-14:50</div>
    <div class="info-item">📍 <strong>地点</strong>: 四楼Y12-2</div>
    <div class="info-item">👨‍🏫 <strong>讲师</strong>: 张鸣晨</div>
    <div class="info-item">🎯 <strong>主题</strong>: Python入门——初始两种变量</div>
</div>
"""

# 组合HTML内容
htmls = f"""
{css}
<div class="title">诚邀您参加公开课</div>
{info_html}
<div class="scene-container">
    <div class="computer"></div>
    <div class="students"></div>
</div>
{balloons}
{balloon_js}
"""

# 渲染页面
html(htmls, height=800)