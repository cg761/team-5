!pip install pymunk

import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util

space = pymunk.Space()
space.gravity = 0, -10  # 중력 설정

# 객체 생성
body = pymunk.Body(1, 1666)
body.position = 50, 100
shape = pymunk.Circle(body, 5)
space.add(body, shape)

# 시뮬레이션 실행
for i in range(100):
    space.step(0.02)
    print(body.position)
