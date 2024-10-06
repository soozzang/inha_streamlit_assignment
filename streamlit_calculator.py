# streamlit_calculator.py

import streamlit as st
import sympy as sp

st.title("한수현의 간단한 공학계산기")

expression = st.text_input("수식을 작성하세요. (ex. sin(pi/6) +  pi)")

expression = expression.replace('e', 'E')
x, y, z = sp.symbols('x y z')

if expression == "1557":
    st.success("근데 드레이븐🎅이 문제에요 이 와중에 진짜 예 타워🏦 안쪽 그래도 잭키러브🎅가 문제에요 케넨🌩없을때 그래도 이쪽도⏩⏩ 달려들어야되는거아닌가요 재키러브🎅가문제에요 예 스턴걸고 쫓아가자 재키러브🎅가 아아악😱😱 잭키러브🎅🎅가 문제에요 돈도왕창떨어졌고요💵💵💵💵 재키러브 어떡하나요😱😱😱😱 저 재키러브를 또 더블킬 케넨🌩이없어요🙅🙅 재키러브가 퍽퍽🤜🤜 케넨🌩🌩이 없어요 기다려라 근데 이겼어요 좀 그만죽여 나도좀 죽이자😈😈 더샤이 오고있습니다 트리플킬 그리고 밀면되나요 왜이렇게빨리끝내나요 아이지❓❓😰😰😰😢😢😢 이거 16분대 16분되기전에 이건아이지 이건 역대급인데요 와 아니 16분이 안됩니다 와 15분 50초 아이지 야 빨리 끝내자 기록🌟🌟이라도 세우자 끝났습니다 15분 55초 56초 쥐쥐🔥🔥")

if st.button("계산"):
    try:
        result = sp.sympify(expression).evalf()
        st.success(f"결과 값: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

st.sidebar.title("사용가능 연산 및 상수")
st.sidebar.write("""
- **기본 연산**: +, -, *, /
- **삼각함수 관련 연산**: sin, cos, tan
- **로그 연산**: log, ln
- **지수 연산**: exp
- **상수들**: pi, e
""")
