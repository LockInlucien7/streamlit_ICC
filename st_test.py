import streamlit as st
import pandas as pd
import plotly.graph_objects as go

stu_name='Lock'
st.title("学生成绩看板")
st.header(stu_name+'成绩单')
data = [
    # ['课程','成绩','GPA'],
    ["物理", 90, 1],
    ["化学", 80, 1],
    ["英语", 70, 1],
    ["数学", 85, 1],
    ["历史", 75, 1]
]

df = pd.DataFrame(data, columns=["科目", "成绩", "GPA"])

categories = df["科目"].tolist()
values = df["成绩"].tolist()

# 创建雷达图
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values + [values[0]],  # 闭合雷达图
    theta=categories + [categories[0]],
    fill='toself',
    name='Locke',
    line=dict(color='royalblue', width=2),
    fillcolor='rgba(65, 105, 225, 0.4)'
))
st.plotly_chart(fig, use_container_width=True)




st.dataframe(df,hide_index=True,column_config={
        "科目": st.column_config.TextColumn("科目", width="medium"),
        "成绩": st.column_config.NumberColumn(
            "分数",
            help="满分100分",
            min_value=0,
            max_value=100,
            format="%d分"
        ),
        "GPA": st.column_config.NumberColumn(
            "GPA",
            help="4分制GPA",
            min_value=0,
            max_value=4,
            format="%.1f"
        )
    },)
st.subheader("成绩分析")
col1, col2 = st.columns(2)
with col1:
    st.metric("平均分", f"{df['成绩'].iloc[::].mean():.1f}分")
with col2:
    st.metric("GPA", f"{df['GPA'].iloc[::].mean():.2f}")

# 添加交互式图表
st.bar_chart(df[:-1].set_index("科目")["成绩"])