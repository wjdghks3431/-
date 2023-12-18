import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 폰트 경로 설정
# macOS에서의 경로, 다른 OS에서는 폰트 경로를 적절히 수정하세요.
font_path = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# CSV 파일에서 데이터 읽어오기
df = pd.read_csv('data.csv', index_col='Unnamed: 0')

# 통화 기호와 쉼표를 제거하고 수치형으로 변환
for col in df.columns:
    df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)

# 행과 열을 바꾸기
df_transposed = df.transpose()

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))

# '총매출', '목표매출', '광고비용' 등 순서로 그리기
for category in ['총매출', '목표매출', '광고비용', '소셜네트워크비용', '1온스별단가']:
    ax.plot(df_transposed.index,
            df_transposed[category], marker='o', label=category)

ax.set_ylabel('Amount')
ax.set_title('Monthly Sales and Expenses')
ax.legend(title='Category')
ax.grid(axis='y')

plt.show()
