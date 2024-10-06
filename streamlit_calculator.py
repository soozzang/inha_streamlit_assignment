# streamlit_calculator.py

import streamlit as st
import sympy as sp

st.title("한수현의 간단한 공학계산기")

expression = st.text_input("수식을 작성하세요. (ex. sin(pi/6) +  pi)")

expression = expression.replace('e', 'E')
expression = re.sub(r'ln(\d+)', r'ln(\1)', expression)
expression = re.sub(r'(\s*)ln(\d+)(\s*\+)', r'\1ln(\2)\3', expression)

x, y, z = sp.symbols('x y z')

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
