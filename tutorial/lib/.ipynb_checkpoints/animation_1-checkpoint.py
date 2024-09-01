import matplotlib.pyplot as plt
import numpy as np
import time

t = np.arange(0, 2 * np.pi, 0.1)
y = np.cos(t)
plt.plot(t, y)

# 그래프 위의 점이 움직이는 애니메이션 구현
# 그래프 위에 또 다른 그래프를 올리는 방식으로 구현되어있다
for i in range(len(y)):
    temp,  = plt.plot(t[i], y[i], color='green', marker='o', markersize=10)
    plt.pause(0.005) # 점이 다음 위치로 넘어가기 전에 일시 대기
    temp.remove() # 점이 다음 위치로 넘어가기 위해 이전 위치의 그래프를 삭제

time.sleep(6) # 6초 동안 기다린다
# plt.show()
plt.close()